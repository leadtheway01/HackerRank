#!/usr/bin/env python3

if __name__ == '__main__':
    N = int (input())
    l = []
    for _ in range(N):
        # split the input string, delimiter is space
        s = input().split()
        cmd = s[0]
        arg = s[1:]
        if cmd != 'print':
            # ex) cmd = insert(0,5)
            cmd += "(" + ",".join(arg) + ")"
            #eval l.insert(0,5)
            eval("l."+cmd)
        else:
            print(l)
