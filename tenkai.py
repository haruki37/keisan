#!/usr/bin/env python3

import random

n = 40 

nap = 3 
nam = 1 
nbp = 10 
nbm = -10
ncp = 3
ncm = 1 
ndp = 10
ndm = -10

with open("kadai/ensyu-tenkai.tex","w") as f:
    print(r"\documentclass[a4j,10pt,fleqn]{jarticle}", file = f)
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
#
#    print(r"\title{ensyu}", file = f)
#    print(r"\author{Haruki Mifuji}", file = f)
#    print(r"\date{\today}", file = f)
#
    print(r"\begin{document}", file = f)
#    print(r"\maketitle", file = f)
#
#    print(r"\section{ensyu}", file = f)
#
    print("tip: $(ax + b)(cx + d) = acx^2 + (ad + bc)x + bd$\n", file = f)
#
with open("kadai/ans-tenkai.tex","w") as g:
    print(r"\documentclass[a4j,10pt,fleqn]{jarticle}", file = g)
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
#
#    print(r"\title{ensyu}", file = g)
#    print(r"\author{Haruki Mifuji}", file = g)
#    print(r"\date{\today}", file = g)
#
    print(r"\begin{document}", file = g)
#    print(r"\maketitle", file = g)
#
#    print(r"\section{ensyu}", file = g)
#
    print("tip: $(ax + b)(cx + d) = acx^2 + (ad + bc)x + bd$\n", file = g)

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

        with open("kadai/ensyu-tenkai.tex","a") as f:
            print("("+str(i)+")~~$"+ensyu+"$\n", file = f)
        with open("kadai/ans-tenkai.tex","a") as g:
            print("("+str(i)+")~~$"+ensyu+"$", file = g)
            print("$$"+ans+"$$\n", file = g) 

    i = i + 1

with open("kadai/ensyu-tenkai.tex","a") as f:
    print(r"\end{document}", file = f)
with open("kadai/ans-tenkai.tex","a") as g:
    print(r"\end{document}", file = g)
