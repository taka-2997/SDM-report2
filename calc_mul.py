#!/usr/bin/python3

import re
                
def calc(A, B):
    try:
        #文字列型の入力を拒否
        if isinstance(A, str) or isinstance(B, str):
            return -1
        
        #整数型でない場合も拒否
        if not (isinstance(A, int) and isinstance(B, int)):
            return -1
        
        #1 <= A <= 999 かつ 1 <= B <= 999
        if 1 <= A <= 999 and 1 <= B <= 999:
            return A * B
        else:
            return -1
            
    except (ValueError, TypeError, AttributeError):
        return -1

        
def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        if A == 'end':
            break
        B = input('input B: ')
        if B == 'end':
            break
        print('input A * input B = ', calc(A, B))

if __name__ == '__main__':
    main()