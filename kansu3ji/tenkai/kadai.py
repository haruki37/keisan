#!/usr/bin/env python3
#
import sympy as sy
import random
# 問題数
n = 20
# 乱数の範囲
nal = 5
nas = -5
nbl = 10
nbs = -10
ncl = 5
ncs = -5
ndl = 10
nds = -10
#変数の定義
(x, y) = sy.symbols("x y")
(a, b, c) = sy.symbols("a b c")
pra = (a*x + b)**3
ans = sy.expand(pra)
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
    print(r"tip: $"+sy.latex(pra)+"$\n", file = f)
    print(r"~~~~~~~~~$="+sy.latex(ans)+"$", file = f)
    print("\n", file = f)
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
    print(r"tip: $"+sy.latex(pra)+"$\n", file = g)
    print(r"~~~~~~~~~$="+sy.latex(ans)+"$", file = g)
    print("\n", file = g)
# 問題の作成
i = 1
while i <= n:
    a = random.randrange(nas,nal)
    b = random.randrange(nbs,nbl)
    c = random.randrange(ncs,ncl)
#    d = random.randrange(nds,ndl) 
    if a == 0 or b == 0 or c == 0:
        continue
    else:
        j = 2
        while j <= min(abs(a),abs(b)):
            moda = a % j  
            modb = b % j  
            if moda == 0 and modb == 0:
                a = a // j
                b = b // j
                j -= 1
            j += 1    
        if a < 0:
            a = -1 * a
            b = -1 * b
    if c == 1:
        ins = (a*x + b)**3
        ten = sy.expand(ins)
        with open("ensyu.tex","a") as f:
            print("("+str(i)+")~~$"+sy.latex(ins)+"$\n", file = f)
        with open("ans.tex","a") as g:
            print("("+str(i)+")~~$"+sy.latex(ins)+"$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(ten)+"$\n", file = g) 
    elif c == -1:
        ins = -(a*x + b)**3
        tty = (a*x + b)**3
        ten = sy.expand(ins)
        ttt = sy.expand(tty)
        with open("ensyu.tex","a") as f:
            print("("+str(i)+")~~$-"+sy.latex(tty)+"$\n", file = f)
        with open("ans.tex","a") as g:
            print("("+str(i)+")~~$-"+sy.latex(tty)+"$\n", file = g)
            print("~~~~~~~~~$=-("+sy.latex(ttt)+")$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(ten)+"$\n", file = g) 
    else:
        ins = c*(a*x + b)**3
        tty = (a*x + b)**3
        ten = sy.expand(ins)
        ttt = sy.expand(tty)
        with open("ensyu.tex","a") as f:
            print("("+str(i)+")~~$"+sy.latex(c)+sy.latex(tty)+"$\n", file = f)
        with open("ans.tex","a") as g:
            print("("+str(i)+")~~$"+sy.latex(c)+sy.latex(tty)+"$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(c)+"("+sy.latex(ttt)+")$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(ten)+"$\n", file = g) 
    i += 1
with open("ensyu.tex","a") as f:
    print(r"\end{document}", file = f)
with open("ans.tex","a") as g:
    print(r"\end{document}", file = g)
