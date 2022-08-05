from email.mime import image
import sys,asyncio,asyncssh,time
from threading import Thread
from functools import partial
class ASsh(object):
    def __init__(self, loop, host, port=22, username="root", client_keys="/root/.ssh/id_rsa",**params):
        self.run = True
        self.loop = loop
        self.host = host
        self.port = port
        self.username = username
        self.client_keys = client_keys
        self.task = None
        self.conn = None
    def connect(self):
        task = self.loop.create_task(self._connect(host=self.host, port=self.port))
    async def _connect(self, host, port):
        connect = partial(asyncssh.connect, known_hosts=None, client_keys=self.client_keys)
        if self.username is not None:
            connect = partial(connect, username=self.username)
        while True:
            async with connect(host=host, port=port) as conn:
                self.conn = conn
                while self.run:
                    await asyncio.sleep(1)

    def waitConnected(self):
        while not self.connected():
            time.sleep(0.001)
    def connected(self):
        return self.conn is not None

    def sendCmd(self, cmd):
        self.task = self.loop.create_task(self._run(cmd))
    async def _run(self, cmd):
        result = await self.conn.run(cmd)
        return result.stdout
    def waitOutput(self):
        if self.task==None:
            return 
        while not self.task.done():
            time.sleep(0.001)
        return self.task.result()
    def close(self):
        self.conn.close()
    
def ipStr( ip ):
    w = ( ip >> 24 ) & 0xff
    x = ( ip >> 16 ) & 0xff
    y = ( ip >> 8 ) & 0xff
    z = ip & 0xff
    return "%i.%i.%i.%i" % ( w, x, y, z )
def ipAdd( i, prefixLen=8, ipBaseNum=0x0a000000 ):
    imax = 0xffffffff >> prefixLen
    assert i <= imax, 'Not enough IP addresses in the subnet'
    mask = 0xffffffff ^ imax
    ipnum = ( ipBaseNum & mask ) + i
    return ipStr( ipnum )
def ipNum( w, x, y, z ):
        return ( w << 24 ) | ( x << 16 ) | ( y << 8 ) | z
def ipParse(ip):
        args = [ int( arg ) for arg in ip.split( '.' ) ]
        while len(args) < 4:
            args.insert( len(args) - 1, 0 )
        return ipNum( *args )

def container(loop,start_ip,count,image):
    ipBasenum=ipParse(start_ip)
    ip=( 0xffffffff >> 8 ) & ipBasenum
    nextIP = ip if ip > 0 else 1
    index=0
    nameToSsh={}
    for _ in range(count):
        _ip = "{}".format(ipAdd( nextIP, ipBaseNum=ipBasenum))
        nextIP += 1
        index+=1
        name="h"+str(index)
        cmd="docker create -it --privileged --cap-add=NET_ADMIN --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --name {} --net=testnet --ip={} {}".format(name,_ip,image)
        ssh=ASsh(loop,host="localhost")
        nameToSsh[name]=ssh
        ssh.connect()
        ssh.waitConnected()
        ssh.sendCmd(cmd)
    for value in nameToSsh.values():
        print(value.waitOutput())
        value.close()
    loop.stop()
def runforever(loop):
            time.sleep(0.001)       ### DSA - WTF ?????????????
            loop.run_forever()  
if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    thread = Thread(target=runforever, args=(loop,))
    thread.start()
    container(loop,sys.argv[1],int(sys.argv[2]),sys.argv[3])
