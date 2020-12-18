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
(a, b, c, d) = sy.symbols("a b c d")
i = sy.symbols("i")
pra1 = (a*x + b*i)*(c*x +d*i)
ans1 = sy.expand(pra1)
pra2 = i**2
ans2 = sy.expand(pra2)
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
    print(r"tip1: $"+sy.latex(pra1)+"$\n", file = f)
    print(r"~~~~~~~~~$="+sy.latex(ans1.subs(i, sy.I))+"$", file = f)
    print("\n", file = f)
    print(r"tip2: $"+sy.latex(pra2)+"$", file = f)
    print(r"~~~~~~~~~$="+sy.latex(ans2.subs(i, sy.I))+"$", file = f)
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
    print(r"tip1: $"+sy.latex(pra1)+"$\n", file = g)
    print(r"~~~~~~~~~$="+sy.latex(ans1.subs(i, sy.I))+"$", file = g)
    print("\n", file = g)
    print(r"tip2: $"+sy.latex(pra2)+"$", file = g)
    print(r"~~~~~~~~~$="+sy.latex(ans2.subs(i, sy.I))+"$", file = g)
    print("\n", file = g)
# 問題の作成
j = 1
while j <= n:
    a = random.randrange(nas,nal)
    b = random.randrange(nbs,nbl)
    c = random.randrange(ncs,ncl)
    d = random.randrange(nds,ndl) 
    q = 1
    if a == 0 or b == 0 or c == 0 or d == 0:
        continue
    else:
        k = 2
        while k <= min(abs(a),abs(b)):
            moda = a % k  
            modb = b % k  
            if moda == 0 and modb == 0:
                a = a // k
                b = b // k
                k -= 1
                q = q * k
            k += 1    
        if a < 0:
            a = -1 * a
            b = -1 * b
            q = -1 * q
        k = 2
        while k <= min(abs(c),abs(d)):
            modc = c % k  
            modd = d % k  
            if modc == 0 and modd == 0:
                c = c // k
                d = d // k
                k -= 1
                q = q * k
            k += 1    
        if c < 0:
            c = -1 * c
            d = -1 * d
            q = -1 * q
    ins = q*(a*x + b*i)*(c*x + d*i)
    ten = sy.expand(ins)
    tty = (a*x + b*i)*(c*x + d*i)
    ttt = sy.expand(tty)
    if q == 1:
        with open("ensyu.tex","a") as f:
            print("("+str(j)+")~~$"+sy.latex(ins.subs(i, sy.I))+"$\n", file = f)
        with open("ans.tex","a") as g:
            print("("+str(j)+")~~$"+sy.latex(ins.subs(i, sy.I))+"$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(ten.subs(i, sy.I))+"$\n", file = g) 
    elif q == -1:
        with open("ensyu.tex","a") as f:
            print("("+str(j)+")~~$-"+sy.latex(tty.subs(i, sy.I))+"$\n", file = f)
        with open("ans.tex","a") as g:
            print("("+str(j)+")~~$-"+sy.latex(tty.subs(i, sy.I))+"$\n", file = g)
            print("~~~~~~~~~$=-("+sy.latex(ttt.subs(i, sy.I))+")$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(ten.subs(i, sy.I))+"$\n", file = g) 
    else:
        with open("ensyu.tex","a") as f:
            print("("+str(j)+")~~$"+sy.latex(q)+sy.latex(tty.subs(i, sy.I))+"$\n", file = f)
        with open("ans.tex","a") as g:
            print("("+str(j)+")~~$"+sy.latex(q)+sy.latex(tty.subs(i, sy.I))+"$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(q)+"("+sy.latex(ttt.subs(i, sy.I))+")$\n", file = g)
            print("~~~~~~~~~$="+sy.latex(ten.subs(i, sy.I))+"$\n", file = g) 
    j += 1
with open("ensyu.tex","a") as f:
    print(r"\end{document}", file = f)
with open("ans.tex","a") as g:
    print(r"\end{document}", file = g)
