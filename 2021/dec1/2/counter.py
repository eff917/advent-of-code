#!/usr/bin/env python3
greater = 0
with open('../input.txt', 'r') as infile:
    linecount = 0
    A = 0
    B = 0
    C = 0
    for line in infile:
        if linecount % 3 == 0:
            if linecount > 1 :
                B += int(line)
                C += int(line)
                print(f"B: {B}, linecount: {linecount}")
                if B > A :
                    greater += 1
            A = int(line)
            pass
        elif linecount % 3 == 1:
            A += int(line)
            if linecount > 1 :
                C += int(line)
                if C > B :
                    greater += 1
                print(f"C: {C}, linecount: {linecount}")
            B = int(line)
            pass
        elif linecount % 3 == 2:
            A += int(line)
            B += int(line)
            print(f"A: {A}, linecount: {linecount}")
            if linecount > 2:
                if A > C :
                    greater += 1
                pass
            C = int(line)
        linecount += 1
        continue
print(greater)