#!/usr/bin/env python3
"""
Class
"""

def binary(num):

    return bin(num)[2:]

def msb_index(n):
    msb_p = -1
    while (n > 0):  
      
        n = n >> 1
        msb_p += 1
      
    return msb_p  

def raised(num):
    return 2**num


class Class:

    def __init__(self):
        super().__init__()

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        result = 0

        while m > 0  and n > 0 and msb_index(m) == msb_index(n) :
            num = raised(msb_index(m))

            result += num

            m -= num
            n -= num
            
        return result


def main(args):

    c = Class()

    result = c.rangeBitwiseAnd(5, 7)

    print(result)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-a', '--arg1',
                        help="An argument.",
                        type=str,
                        default='default')

    args = parser.parse_args()
    main(args)
