import os
import sys
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
def container(start_ip,count):
    ipBasenum=ipParse(start_ip)
    ip=( 0xffffffff >> 8 ) & ipBasenum
    nextIP = ip if ip > 0 else 1
    index=0
    #cmd="docker network create -d macvlan --subnet=10.100.0.0/8 --gateway=10.100.0.1 -o parent=eth0 mynet"
    for _ in range(count):
        _ip = "{}".format(ipAdd( nextIP, ipBaseNum=ipBasenum))
        nextIP += 1
        index+=1
        name="h"+str(index)
        print(_ip,end=" ")
        if(index%10==0):
            print("\n")
        #cmd="docker create -it --privileged --cap-add=NET_ADMIN --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --name {} --net=mynet --ip={} ubuntu".format(name,_ip)
        #os.system(cmd)
if __name__ == '__main__':
    container("10.100.0.1",100000)
