#!/usr/bin/env python3
#
import random
# 問題数
n = 150
# 乱数の範囲
nal = 5
nas = -5
nbl = 10
nbs = -10
ncl = 5
ncs = -5
ndl = 10
nds = -10
# 問題のlatex
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
    print("tip: $a(x - p)^2 + q$\n"              , file = f)
    print("~~~~~~~~~$= a(x^2 - 2px + p^2) + q$\n", file = f)
    print("~~~~~~~~~$= ax^2 - 2apx + ap^2 + q$\n", file = f)
# 解答のlatex
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
    print("tip: $a(x - p)^2 + q$\n"              , file = g)
    print("~~~~~~~~~$= a(x^2 - 2px + p^2) + q$\n", file = g)
    print("~~~~~~~~~$= ax^2 - 2apx + ap^2 + q$\n", file = g)
# 問題の作成
i = 1
while i <= n:
    a = random.randrange(nas,nal)
    b = random.randrange(nbs,nbl)
    c = random.randrange(ncs,ncl)
#    d = random.randrange(nds,ndl)
    A = a
    B = 2*a*b
    C = a*b**2+c
# 排除する値
    if a == 0 or b == 0 or c ==0:
        i = i - 1
    else:
# 平方完成の結果
        if a == 1:
            if b > 0:
                if c >= 0:
                    heihoukansei = "(x +" + str(b) + ")^2 +" + str(c)
                else:
                    heihoukansei = "(x +" + str(b) + ")^2"   + str(c)
            else:
                if c >= 0:
                    heihoukansei = "(x"   + str(b) + ")^2 +" + str(c)
                else:
                    heihoukansei = "(x"   + str(b) + ")^2"   + str(c)
        elif a == -1:
            if b > 0:
                if c >= 0:
                    heihoukansei = "-(x +" + str(b) + ")^2 +" + str(c)
                else:                                                 
                    heihoukansei = "-(x +" + str(b) + ")^2"   + str(c)
            else:                                                     
                if c >= 0:                                            
                    heihoukansei = "-(x"   + str(b) + ")^2 +" + str(c)
                else:                                                 
                    heihoukansei = "-(x"   + str(b) + ")^2"   + str(c)
        else:
            if b > 0:
                if c >= 0:
                    heihoukansei = str(a) + "(x +" + str(b) + ")^2 +" + str(c)
                else:                                                           
                    heihoukansei = str(a) + "(x +" + str(b) + ")^2"   + str(c)
            else:                                                               
                if c >= 0:                                                      
                    heihoukansei = str(a) + "(x"   + str(b) + ")^2 +" + str(c)
                else:                                                           
                    heihoukansei = str(a) + "(x"   + str(b) + ")^2"   + str(c)
# 展開の結果
        if A == 1:
            if B > 0:
                if C == 0:
                    tenkai = "x^2 +" + str(B) + "x"
                elif C > 0:
                    tenkai = "x^2 +" + str(B) + "x +" + str(C)
                else:
                    tenkai = "x^2 +" + str(B) + "x"   + str(C)
            else:
                if C == 0:
                    tenkai = "x^2"   + str(B) + "x"
                elif C > 0:
                    tenkai = "x^2"   + str(B) + "x +" + str(C)
                else:
                    tenkai = "x^2"   + str(B) + "x"   + str(C)
        elif A == -1:
            if B > 0:
                if C == 0:
                    tenkai = "-x^2 +" + str(B) + "x"
                elif C > 0:
                    tenkai = "-x^2 +" + str(B) + "x +" + str(C)
                else:
                    tenkai = "-x^2 +" + str(B) + "x"   + str(C)
            else:
                if C == 0:
                    tenkai = "-x^2"   + str(B) + "x"
                elif C > 0:
                    tenkai = "-x^2"   + str(B) + "x +" + str(C)
                else:
                    tenkai = "-x^2"   + str(B) + "x"   + str(C)
        else:
            if B > 0:
                if C == 0:
                    tenkai = str(A) + "x^2 +" + str(B) + "x"
                elif C > 0:
                    tenkai = str(A) + "x^2 +" + str(B) + "x +" + str(C)
                else:
                    tenkai = str(A) + "x^2 +" + str(B) + "x"   + str(C)
            else:
                if C == 0:
                    tenkai = str(A) + "x^2"   + str(B) + "x"
                elif C > 0:
                    tenkai = str(A) + "x^2"   + str(B) + "x +" + str(C)
                else:
                    tenkai = str(A) + "x^2"   + str(B) + "x"   + str(C)
#        print(a)
#        print(b)
#        print(c)
#        print(d)
#        print("("+str(i)+")")
#        print("$"+heihoukansei+"$\n")
#        print(A)
#        print(B)
#        print(C)
#        print("$"+tenkai+"$\n\n")
# 問題の出力
# 途中式なし
        if a == 1:
            with open("ensyu.tex","a") as f:
                print("("+str(i)+")~~$"+heihoukansei+"$\n", file = f)
            with open("ans.tex","a") as g:
                print("("+str(i)+")~~$"+heihoukansei+"$\n", file = g)
                print("~~~~~~~~~$="+tenkai+"$\n", file = g) 
# 途中式あり
        else:        
            if a == -1:
                if b > 0:
                    if c >= 0:
                        totyu = "-(x^2 +" + str(2*b) + "x +" + str(b**2) +  ") +" + str(c)
                    else:
                        totyu = "-(x^2 +" + str(2*b) + "x +" + str(b**2) +  ")"   + str(c)
                else:
                    if c >= 0:
                        totyu = "-(x^2"   + str(2*b) + "x +" + str(b**2) +  ") +" + str(c)
                    else:
                        totyu = "-(x^2"   + str(2*b) + "x +" + str(b**2) +  ")"   + str(c)
            else:
                if b > 0:
                    if c >= 0:
                        totyu = str(a) + "(x^2 +" + str(2*b) + "x +" + str(b**2) +  ") +" + str(c)
                    else:
                        totyu = str(a) + "(x^2 +" + str(2*b) + "x +" + str(b**2) +  ")"   + str(c)
                else:
                    if c >= 0:
                        totyu = str(a) + "(x^2"   + str(2*b) + "x +" + str(b**2) +  ") +" + str(c)
                    else:
                        totyu = str(a) + "(x^2"   + str(2*b) + "x +" + str(b**2) +  ")"   + str(c)
            with open("ensyu.tex","a") as f:
                print("("+str(i)+")~~$"+heihoukansei+"$\n", file = f)
            with open("ans.tex","a") as g:
                print("("+str(i)+")~~$"+heihoukansei+"$\n", file = g)
                print("~~~~~~~~~$="+totyu+"$\n", file = g) 
                print("~~~~~~~~~$="+tenkai+"$\n", file = g) 
    i = i + 1
with open("ensyu.tex","a") as f:
    print(r"\end{document}", file = f)
with open("ans.tex","a") as g:
    print(r"\end{document}", file = g)
