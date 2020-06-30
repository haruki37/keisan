#!/usr/bin/env python3
#
import random
#
n = 40 
#
nap = 3 
nam = 1 
nbp = 10 
nbm = -10
ncp = 3
ncm = 1 
ndp = 10
ndm = -10
#
i = 1 
while i <= n:
    a = random.randrange(nam,nap)
    b = random.randrange(nbm,nbp)
    c = random.randrange(ncm,ncp)
    d = random.randrange(ndm,ndp)
#
    A = a*c
    B = a*d + b*c
    C = b*d
#
    if (A == 0 and B == 0) or (B == 0 and C == 0) or (C == 0 and A == 0) or (a == 0 and b == 1) or (c == 0 and d == 1):
        i = i - 1
    else:
        if a == c and b == d:
            if a == 1 and b > 0:
                ensyu = "(x+" + str(b) +")^2"
            elif a == 1 and b < 0:
                ensyu = "(x" + str(b) +")^2"
            elif a == -1 and b > 0:
                ensyu = "(-x+" + str(b) +")^2"
            elif a == -1 and b < 0:
                ensyu = "(-x" + str(b) +")^2"
            elif a != 1 and b > 0:
                ensyu = "(" + str(a) +"x+" + str(b) +")^2"
            elif a != 1 and b < 0:
                ensyu = "(" + str(a) +"x" + str(b) +")^2"
        else:
            if a == 0:
                fx = str(b)
            elif a == 1:
                if b == 0:
                    fx = "x"
                elif b > 0:
                    fx = "(x+" + str(b) + ")"
                elif b < 0:
                    fx = "(x" + str(b) + ")"
            elif a == -1:
                if b == 0:
                    fx = "-x"
                elif b > 0:
                    fx = "(-x+" + str(b) + ")"
                elif b < 0:
                    fx = "(-x" + str(b) + ")"
            else:
                if b == 0:
                    fx = str(a) + "x"
                elif b > 0:
                    fx = "(" + str(a) + "x+" + str(b) + ")"
                elif b < 0:
                    fx = "(" + str(a) + "x" + str(b) + ")"
 #   
            if c == 0:
                if d > 0:
                    gx = str(d)
                elif d < 0:
                    gx = "(" + str(d) + ")"
            elif c == 1:
                if d == 0:
                    gx = "x"
                elif d > 0:
                    gx = "(x+" + str(d) + ")"
                elif d < 0:
                    gx = "(x" + str(d) + ")"
            elif c == -1:
                if d == 0:
                    gx = "(-x)"
                elif d > 0:
                    gx = "(-x+" + str(d) + ")"
                elif d < 0:
                    gx = "(-x" + str(d) + ")"
            else:
                if d == 0:
                    if c > 0:
                        gx = str(c) + "x"
                    if c < 0:
                        gx = "(" + str(c) + "x)"
                elif d > 0:
                    gx = "(" + str(c) + "x+" + str(d) + ")"
                elif d < 0:
                    gx = "(" + str(c) + "x" + str(d) + ")"

            ensyu = fx + gx
#
        if A == 0:
            if B == 1:
                if C > 0:
                    ans = "x~+~" + str(C)
                elif C < 0:
                    ans = "x~" + str(C)
            elif B == -1:
                if C > 0:
                    ans = "-x~+~" + str(C)
                elif C < 0:
                    ans = "-x~" + str(C)
            else:
                if C > 0:
                    ans = str(B) + "x~+~" + str(C)
                elif C < 0:
                    ans = str(B) + "x~" + str(C)
        elif A == 1:
            if B == 0:
                if C > 0:
                    ans = "x^2~+~" + str(C) 
                elif C < 0:
                    ans = "x^2~" + str(C) 
            elif B == 1:
                if C == 0:
                    ans = "x^2~+~x" 
                elif C > 0:
                    ans = "x^2~+~x~+~" + str(C) 
                elif C < 0:
                    ans = "x^2~+~x~" + str(C) 
            elif B == -1:
                if C == 0:
                    ans = "x^2~-x" 
                elif C > 0:
                    ans = "x^2~-x~+~" + str(C) 
                elif C < 0:
                    ans = "x^2~-x~" + str(C) 
            elif B > 0:
                if C == 0:
                    ans = "x^2~+~" + str(B) + "x" 
                elif C > 0:
                    ans = "x^2~+~" + str(B) + "x~+~" + str(C) 
                elif C < 0:
                    ans = "x^2~+~" + str(B) + "x~" + str(C) 
            elif B < 0:
                if C == 0:
                    ans = "x^2~" + str(B) + "x" 
                elif C > 0:
                    ans = "x^2~" + str(B) + "x~+~" + str(C) 
                elif C < 0:
                    ans = "x^2~" + str(B) + "x~" + str(C) 
        elif A == -1:
            if B == 0:
                if C > 0:
                    ans = "-x^2~+~" + str(C) 
                elif C < 0:
                    ans = "-x^2~" + str(C) 
            elif B == 1:
                if C == 0:
                    ans = "-x^2~+~x" 
                elif C > 0:
                    ans = "-x^2~+~x~+~" + str(C) 
                elif C < 0:
                    ans = "-x^2~+~x~" + str(C) 
            elif B == -1:
                if C == 0:
                    ans = "-x^2~-x" 
                elif C > 0:
                    ans = "-x^2~-x~+~" + str(C) 
                elif C < 0:
                    ans = "-x^2~-x~" + str(C) 
            elif B > 0:
                if C == 0:
                    ans = "-x^2~+~" + str(B) + "x" 
                elif C > 0:
                    ans = "-x^2~+~" + str(B) + "x~+~" + str(C) 
                elif C < 0:
                    ans = "-x^2~+~" + str(B) + "x~" + str(C) 
            elif B < 0:
                if C == 0:
                    ans = "-x^2~" + str(B) + "x" 
                elif C > 0:
                    ans = "-x^2~" + str(B) + "x~+~" + str(C) 
                elif C < 0:
                    ans = "-x^2~" + str(B) + "x~" + str(C) 
        else:
            if B == 0:
                if C > 0:
                    ans = str(A) + "x^2~+~" + str(C) 
                elif C < 0:
                    ans = str(A) + "x^2~" + str(C) 
            elif B == 1:
                if C == 0:
                    ans = str(A) + "x^2~+~x" 
                elif C > 0:
                    ans = str(A) + "x^2~+~x~+~" + str(C) 
                elif C < 0:
                    ans = str(A) + "x^2~+~x~" + str(C) 
            elif B == -1:
                if C == 0:
                    ans = str(A) + "x^2~-x" 
                elif C > 0:
                    ans = str(A) + "x^2~-x~+~" + str(C) 
                elif C < 0:
                    ans = str(A) + "x^2~-x~" + str(C) 
            elif B > 0:
                if C == 0:
                    ans = str(A) + "x^2~+~" + str(B) + "x" 
                elif C > 0:
                    ans = str(A) + "x^2~+~" + str(B) + "x~+~" + str(C) 
                elif C < 0:
                    ans = str(A) + "x^2~+~" + str(B) + "x~" + str(C) 
            elif B < 0:
                if C == 0:
                    ans = str(A) + "x^2~" + str(B) + "x" 
                elif C > 0:
                    ans = str(A) + "x^2~" + str(B) + "x~+~" + str(C) 
                elif C < 0:
                    ans = str(A) + "x^2~" + str(B) + "x~" + str(C) 

#            print(a)
#            print(b)
#            print(c)
#            print(d)
        print("("+str(i)+")")
        print("$"+ensyu+"$\n")
#            print(A)
#            print(B)
#            print(C)
        print("$"+ans+"$\n\n") 
#
    i = i + 1
