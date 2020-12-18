#!/usr/bin/env python3
#
import numpy as np
import math
import sympy as sy
import random
# 問題数
n = 100
# 乱数の範囲
#nal = 7
#nas = 1
#nbl = 13
#nbs = 0
ncl = 3
ncs = -3
#ndl = 10
#nds = -10
#変数の定義
(x, y) = sy.symbols("x y")
(a, b, c, d) = sy.symbols("a b c d")
i = sy.symbols("i")
pi = math.pi
#pra1 = (a*x + b*i)*(c*x +d*i)
#ans1 = sy.expand(pra1)
#pra2 = i**2
#ans2 = sy.expand(pra2)
# 問題のlatex
with open("ensyu.tex","w") as f:
    print(r"\documentclass[a4j,twocolumn,10pt,fleqn,dvipdfmx]{jarticle}", file = f)
    print(r"\usepackage{graphicx}", file = f)
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
#    print(r"\begin{figure}", file = f)
#    print(r"\includegraphics[width = 70mm]{img.jpg}", file = f)
#    print(r"\includegraphics[width = 70mm]{img2.jpg}", file = f)
#    print(r"\end{figure}", file = f)
    print(r"tip1: $"+sy.latex(180)+"^\circ$\n", file = f)
    print(r"~~~~~~~~~$=\pi$", file = f)
    print("\n", file = f)
    print(r"tip1: $"+sy.latex(360)+"^\circ$\n", file = f)
    print(r"~~~~~~~~~$=2\pi$", file = f)
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
#    print(r"tip1: $"+sy.latex(pra1)+"$\n", file = g)
#    print(r"~~~~~~~~~$="+sy.latex(ans1.subs(i, sy.I))+"$", file = g)
#    print("\n", file = g)
#    print(r"tip2: $"+sy.latex(pra2)+"$", file = g)
#    print(r"~~~~~~~~~$="+sy.latex(ans2.subs(i, sy.I))+"$", file = g)
#    print("\n", file = g)
# 問題の作成
def main(x):
    # ラジアン → 度
    rad = x
    deg = np.rad2deg(x)
    # 画面出力
#    print(sy.latex(rad))
#    print(deg) 
#    print(round(deg, 0))
    with open("ensyu.tex","a") as f:
        print(r"("+str(j)+")~~$"+sy.latex(round(deg))+"^\circ$\n", file = f)
    with open("ans.tex","a") as g:
        print(r"("+str(j)+")~~$"+sy.latex(round(deg))+"^\circ$\n", file = g)
        if b+2*a*c == 0:
            print(r"~~~~~~~~~$=""0$\n", file = g) 
        elif b+2*a*c == a:
            print(r"~~~~~~~~~$=""\pi$\n", file = g) 
        elif b+2*a*c == -a:
            print(r"~~~~~~~~~$=""-\pi$\n", file = g) 
        elif a == 1:
            print(r"~~~~~~~~~$="+str(b+2*c)+"\pi$\n", file = g) 
        else:
            print(r"~~~~~~~~~$=\frac{"+str(b+2*a*c)+"}{"+str(a)+"}\pi$\n", file = g) 
j = 1
while j<= n:
    a = random.choice([4, 6])
    b = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12])
    c = random.randrange(ncs,ncl)
#    c = 0
    k = 2
    while k <= min(abs(a),abs(b)):
        moda = a % k  
        modb = b % k  
        if moda == 0 and modb == 0:
            a = a // k
            b = b // k
            k -= 1
        k += 1    
    if abs(b/a*pi) > 2*pi:
        continue 
    theta = b/a*pi + 2*pi*c
    main(theta)
    j += 1
with open("ensyu.tex","a") as f:
    print(r"\end{document}", file = f)
with open("ans.tex","a") as g:
    print(r"\end{document}", file = g)
