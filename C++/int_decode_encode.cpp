#include <iostream>
#include <stdint.h>

using namespace std;
int encode(uint32_t in, uint8_t *out)
{
    //  set the memory to zero
    for(int i = 0; i < 5; i++) *(out + i) = 0;
    
    uint8_t cnt = 0, size = 0;
    uint8_t mask = 0xff;
    uint8_t cur_size = 0;
    while (in > 0)
    {
        mask = (in & 1) << cnt;
        *(out + cur_size) ^= mask;
        in >>= 1;
        cnt += 1;

        //  for every 7 bits, save it to out
        if (cnt == 7)
        {
            cur_size += 1;
            cnt = 0;
        }
    }

    // we need to set the "stop bit"
    *(out + cur_size) ^= 0x80;

    // return the actually used size of the out array
    return size;
}

int decode(const uint8_t *in, uint32_t *out)
{
    uint32_t value;
    uint32_t sum = 0;
    uint8_t index = 0;

    while(true)
    {
        // deal with every 8-bit value and sum it to sum;
        value = *(in + index);

        // if the value is bigger the 128, means it is the last 8-bit
        if (value >= 128) break;
        sum += value << (index * 7);
        index += 1;
    }

    // deal with the last 8-bit value
    //  carefully, discard the "stop bit"
    value &= 0x7f;
    sum += value << (index * 7);
    *out = sum;
    return 0;
}

void test()
{
    uint8_t out[5];
    uint32_t *in = new uint32_t;
    uint32_t inn[] = {0xffffffff, 2, 4,3432, 454,54543534,56456,65536,32432423,1,0};
    for(int i = 0; i < 10; i ++)
    {
        encode(inn[i], out);
        decode(out, in);
        cout << "the original value: "<< inn[i] << endl;
        cout << "the decoded value: " << *in << endl;
    }
}

int main()
{
    test();
    return 0;
}