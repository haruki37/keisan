#!/usr/bin/env python3
#
import random
#
n = 100
#
nal = 5
nas = -5
nbl = 10
nbs = -10
ncl = 5
ncs = -5
ndl = 10
nds = -10
#
with open("ensyu.tex","w") as f:
    print(r"\documentclass[a4j,twocolumn,10pt,fleqn]{jarticle}", file = f)
    print(r"\usepackage[dvipdfmx]{graphicx}", file = f)
    print(r"% \usepackage[dvipdfmx]{color}", file = f)
    print(r"\usepackage{here}", file = f)
    print(r"\usepackage{longtable}", file = f)
    print(r"\usepackage{bm}", file = f)
    print(r"\usepackage{amsmath,amssymb}", file = f)
    print(r"\usepackage{float}", file = f)
    print(r"\usepackage{txfonts}", file = f)
    print(r"\usepackage{mathrsfs}", file = f)
    print(r"\usepackage{subcaption}", file = f)
    print(r"\usepackage{lscape}", file = f)
    print(r"\usepackage{textcomp}", file = f)
    print(r"\usepackage{multirow}", file = f)
    print(r"\usepackage{afterpage}", file = f)
    print(r"\usepackage{color}", file = f)
    print(r"\usepackage{tabularx}", file = f)
    print(r"\usepackage{pythontex}", file = f)
    print(r"\begin{document}", file = f)
    print("tip: $P(ax + b)(cx + d) = Pacx^2 + P(ad + bc)x + Pbd$\n", file = f)
#
with open("ans.tex","w") as g:
    print(r"\documentclass[a4j,twocolumn,10pt,fleqn]{jarticle}", file = g)
    print(r"\usepackage[dvipdfmx]{graphicx}", file = g)
    print(r"% \usepackage[dvipdfmx]{color}", file = g)
    print(r"\usepackage{here}", file = g)
    print(r"\usepackage{longtable}", file = g)
    print(r"\usepackage{bm}", file = g)
    print(r"\usepackage{amsmath,amssymb}", file = g)
    print(r"\usepackage{float}", file = g)
    print(r"\usepackage{txfonts}", file = g)
    print(r"\usepackage{mathrsfs}", file = g)
    print(r"\usepackage{subcaption}", file = g)
    print(r"\usepackage{lscape}", file = g)
    print(r"\usepackage{textcomp}", file = g)
    print(r"\usepackage{multirow}", file = g)
    print(r"\usepackage{afterpage}", file = g)
    print(r"\usepackage{color}", file = g)
    print(r"\usepackage{tabularx}", file = g)
    print(r"\usepackage{pythontex}", file = g)
    print(r"\begin{document}", file = g)
    print("tip: $P(ax + b)(cx + d) = Pacx^2 + P(ad + bc)x + Pbd$\n", file = g)
#
i = 1
while i <= n:
    a = random.randrange(nas,nal)
    b = random.randrange(nbs,nbl)
    c = random.randrange(ncs,ncl)
    d = random.randrange(nds,ndl)
#
    A = a*c
    B = a*d + b*c
    C = b*d
#
    if (A == 0 and B == 0) or (B == 0 and C == 0) or (C == 0 and A == 0) or (a == 0 and b == 1) or c == 0 or d == 0:
        i = i - 1
    else:
        lp = 1
        if a == 0 or b == 0 or abs(a) == 1:
            if a == 0 or b == 0 or a == 1: 
                lp = lp
            else:
                a = -1 * a
                b = -1 * b
                lp = lp * (-1)
        else:
            j = 2
            while j <= min(abs(a),abs(b)):
                moda = a % j  
                modb = b % j  
                if moda == 0 and modb == 0:
                    a = a // j
                    b = b // j
                    lp = lp * j
                    j = j - 1
                else:
                    lp = lp
                j = j + 1    
            if a < 0:
                a = -1 * a
                b = -1 * b
                lp = lp * (-1)
        rp = 1
        if abs(c) == 1:
            if c == 1: 
                rp = rp
            else:
                c = -1 * c
                d = -1 * d
                rp = rp * (-1)
        else:
            k = 2
            while k <= min(abs(c),abs(d)):
                modc = c % k  
                modd = d % k  
                if modc == 0 and modd == 0:
                    c = c // k
                    d = d // k
                    rp = rp * k
                    k = k - 1
                else:
                    rp = rp
                k = k + 1    
            if c < 0:
                c = -1 * c
                d = -1 * d
                rp = rp * (-1)
        p = lp * rp
        if p == 1:
            if a == c and b == d:
                if a == 1 and b > 0:
                    insubunkai = "(x+" + str(b) +")^2"
                elif a == 1 and b < 0:
                    insubunkai = "(x" + str(b) +")^2"
                elif a != 1 and b > 0:
                    insubunkai = "(" + str(a) +"x+" + str(b) +")^2"
                elif a != 1 and b < 0:
                    insubunkai = "(" + str(a) +"x" + str(b) +")^2"
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
                else:
                    if b == 0:
                        fx = str(a) + "x"
                    elif b > 0:
                        fx = "(" + str(a) + "x+" + str(b) + ")"
                    elif b < 0:
                        fx = "(" + str(a) + "x" + str(b) + ")"
                if c == 1:
                    if d > 0:
                        gx = "(x+" + str(d) + ")"
                    elif d < 0:
                        gx = "(x" + str(d) + ")"
                else:
                    if d > 0:
                        gx = "(" + str(c) + "x+" + str(d) + ")"
                    elif d < 0:
                        gx = "(" + str(c) + "x" + str(d) + ")"
#
                insubunkai = fx + gx
#
        elif p == -1:
            if a == c and b == d:
                if a == 1 and b > 0:
                    insubunkai = "-(x+" + str(b) +")^2"
                elif a == 1 and b < 0:
                    insubunkai = "-(x" + str(b) +")^2"
                elif a != 1 and b > 0:
                    insubunkai = "-(" + str(a) +"x+" + str(b) +")^2"
                elif a != 1 and b < 0:
                    insubunkai = "-(" + str(a) +"x" + str(b) +")^2"
            else:
                if a == 0:
                    fx = str(-1*b)
                elif a == 1:
                    if b == 0:
                        fx = "-x"
                    elif b > 0:
                        fx = "-(x+" + str(b) + ")"
                    elif b < 0:
                        fx = "-(x" + str(b) + ")"
                else:
                    if b == 0:
                        fx = str(-1*a) + "x"
                    elif b > 0:
                        fx = "-(" + str(a) + "x+" + str(b) + ")"
                    elif b < 0:
                        fx = "-(" + str(a) + "x" + str(b) + ")"
                if c == 1:
                    if d == 0:
                        gx = "x"
                    elif d > 0:
                        gx = "(x+" + str(d) + ")"
                    elif d < 0:
                        gx = "(x" + str(d) + ")"
                else:
                    if d > 0:
                        gx = "(" + str(c) + "x+" + str(d) + ")"
                    elif d < 0:
                        gx = "(" + str(c) + "x" + str(d) + ")"
#
                insubunkai = fx + gx
#
        else:
            if a == c and b == d:
                if a == 1 and b > 0:
                    insubunkai = str(p) + "(x+" + str(b) +")^2"
                elif a == 1 and b < 0:
                    insubunkai = str(p) + "(x" + str(b) +")^2"
                elif a != 1 and b > 0:
                    insubunkai = str(p) + "(" + str(a) +"x+" + str(b) +")^2"
                elif a != 1 and b < 0:
                    insubunkai = str(p) + "(" + str(a) +"x" + str(b) +")^2"
            else:
                if a == 0:
                    fx = str(p*b)
                elif a == 1:
                    if b == 0:
                        fx = str(p) + "x"
                    elif b > 0:
                        fx = str(p) + "(x+" + str(b) + ")"
                    elif b < 0:
                        fx = str(p) + "(x" + str(b) + ")"
                else:
                    if b == 0:
                        fx = str(p*a) + "x"
                    elif b > 0:
                        fx = str(p) + "(" + str(a) + "x+" + str(b) + ")"
                    elif b < 0:
                        fx = str(p) + "(" + str(a) + "x" + str(b) + ")"
                if c == 1:
                    if d > 0:
                        gx = "(x+" + str(d) + ")"
                    elif d < 0:
                        gx = "(x" + str(d) + ")"
                else:
                    if d > 0:
                        gx = "(" + str(c) + "x+" + str(d) + ")"
                    elif d < 0:
                        gx = "(" + str(c) + "x" + str(d) + ")"
#
                insubunkai = fx + gx
#
        if A == 0:
            if B == 1:
                if C > 0:
                    tenksi = "x~+~" + str(C)
                elif C < 0:
                    tenksi = "x~" + str(C)
            elif B == -1:
                if C > 0:
                    tenksi = "-x~+~" + str(C)
                elif C < 0:
                    tenksi = "-x~" + str(C)
            else:
                if C > 0:
                    tenksi = str(B) + "x~+~" + str(C)
                elif C < 0:
                    tenksi = str(B) + "x~" + str(C)
        elif A == 1:
            if B == 0:
                if C > 0:
                    tenksi = "x^2~+~" + str(C)
                elif C < 0:
                    tenksi = "x^2~" + str(C)
            elif B == 1:
                if C == 0:
                    tenksi = "x^2~+~x"
                elif C > 0:
                    tenksi = "x^2~+~x~+~" + str(C)
                elif C < 0:
                    tenksi = "x^2~+~x~" + str(C)
            elif B == -1:
                if C == 0:
                    tenksi = "x^2~-x"
                elif C > 0:
                    tenksi = "x^2~-x~+~" + str(C)
                elif C < 0:
                    tenksi = "x^2~-x~" + str(C)
            elif B > 0:
                if C == 0:
                    tenksi = "x^2~+~" + str(B) + "x"
                elif C > 0:
                    tenksi = "x^2~+~" + str(B) + "x~+~" + str(C)
                elif C < 0:
                    tenksi = "x^2~+~" + str(B) + "x~" + str(C)
            elif B < 0:
                if C == 0:
                    tenksi = "x^2~" + str(B) + "x"
                elif C > 0:
                    tenksi = "x^2~" + str(B) + "x~+~" + str(C)
                elif C < 0:
                    tenksi = "x^2~" + str(B) + "x~" + str(C)
        elif A == -1:
            if B == 0:
                if C > 0:
                    tenksi = "-x^2~+~" + str(C)
                elif C < 0:
                    tenksi = "-x^2~" + str(C)
            elif B == 1:
                if C == 0:
                    tenksi = "-x^2~+~x"
                elif C > 0:
                    tenksi = "-x^2~+~x~+~" + str(C)
                elif C < 0:
                    tenksi = "-x^2~+~x~" + str(C)
            elif B == -1:
                if C == 0:
                    tenksi = "-x^2~-x"
                elif C > 0:
                    tenksi = "-x^2~-x~+~" + str(C)
                elif C < 0:
                    tenksi = "-x^2~-x~" + str(C)
            elif B > 0:
                if C == 0:
                    tenksi = "-x^2~+~" + str(B) + "x"
                elif C > 0:
                    tenksi = "-x^2~+~" + str(B) + "x~+~" + str(C)
                elif C < 0:
                    tenksi = "-x^2~+~" + str(B) + "x~" + str(C)
            elif B < 0:
                if C == 0:
                    tenksi = "-x^2~" + str(B) + "x"
                elif C > 0:
                    tenksi = "-x^2~" + str(B) + "x~+~" + str(C)
                elif C < 0:
                    tenksi = "-x^2~" + str(B) + "x~" + str(C)
        else:
            if B == 0:
                if C > 0:
                    tenksi = str(A) + "x^2~+~" + str(C)
                elif C < 0:
                    tenksi = str(A) + "x^2~" + str(C)
            elif B == 1:
                if C == 0:
                    tenksi = str(A) + "x^2~+~x"
                elif C > 0:
                    tenksi = str(A) + "x^2~+~x~+~" + str(C)
                elif C < 0:
                    tenksi = str(A) + "x^2~+~x~" + str(C)
            elif B == -1:
                if C == 0:
                    tenksi = str(A) + "x^2~-x"
                elif C > 0:
                    tenksi = str(A) + "x^2~-x~+~" + str(C)
                elif C < 0:
                    tenksi = str(A) + "x^2~-x~" + str(C)
            elif B > 0:
                if C == 0:
                    tenksi = str(A) + "x^2~+~" + str(B) + "x"
                elif C > 0:
                    tenksi = str(A) + "x^2~+~" + str(B) + "x~+~" + str(C)
                elif C < 0:
                    tenksi = str(A) + "x^2~+~" + str(B) + "x~" + str(C)
            elif B < 0:
                if C == 0:
                    tenksi = str(A) + "x^2~" + str(B) + "x"
                elif C > 0:
                    tenksi = str(A) + "x^2~" + str(B) + "x~+~" + str(C)
                elif C < 0:
                    tenksi = str(A) + "x^2~" + str(B) + "x~" + str(C)
#            print(a)
#            print(b)
#            print(c)
#            print(d)
        print("("+str(i)+")")
        print("$"+insubunkai+"$\n")
#            print(A)
#            print(B)
#            print(C)
        print("$"+tenksi+"$\n\n")
#
        with open("ensyu.tex","a") as f:
            print("("+str(i)+")~~$"+insubunkai+"$\n", file = f)
        with open("ans.tex","a") as g:
            print("("+str(i)+")~~$"+insubunkai+"$\n", file = g)
            print("~~~~~~~~~$="+tenksi+"$\n", file = g) 
    i = i + 1
with open("ensyu.tex","a") as f:
    print(r"\end{document}", file = f)
with open("ans.tex","a") as g:
    print(r"\end{document}", file = g)
