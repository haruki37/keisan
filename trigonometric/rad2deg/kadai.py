#!/usr/bin/env python3
#
import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sy
import random
import re
#
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["text.usetex"] = True
#
# 問題数
n = 10
#
# 乱数の範囲
#nal = 7
#nas = 1
#nbl = 13
#nbs = 0
ncl = 3
ncs = -3
#ndl = 10
#nds = -10
#
#変数の定義
(x, y) = sy.symbols("x y")
(a, b, c, d) = sy.symbols("a b c d")
i = sy.symbols("i")
pi = math.pi
#
#ヒント
h = n + 4
pra = plt.figure(figsize=(8,n+2))
ans = plt.figure(figsize=(8,n+2))
pra.text(0.1, 1-1/(n+3), "Convert the following angles from radians to degrees.", fontsize=20)
ans.text(0.1, 1-1/(n+3), "Convert the following angles from radians to degrees.", fontsize=20)
pra.text(0.1, 1-2/(h), "tip~1:", fontsize=20)
pra.text(0.2, 1-2/(h), r"$\displaystyle \pi~[rad]$", fontsize=20)
pra.text(0.5, 1-2/(h), r"$\displaystyle = 180~[^\circ~]$", fontsize=20)
pra.text(0.1, 1-3/(h), "tip~2:", fontsize=20)
pra.text(0.2, 1-3/(h), r"$\displaystyle 2\pi~[rad]$", fontsize=20)
pra.text(0.5, 1-3/(h), r"$\displaystyle = 2\times 180~[^\circ~] = 360~[^\circ~]$", fontsize=20)
ans.text(0.1, 1-2/(h), "tip~1:", fontsize=20)
ans.text(0.2, 1-2/(h), r"$\displaystyle \pi~[rad]$", fontsize=20)
ans.text(0.5, 1-2/(h), r"$\displaystyle = 180~[^\circ~]$", fontsize=20)
ans.text(0.1, 1-3/(h), "tip~2:", fontsize=20)
ans.text(0.2, 1-3/(h), r"$\displaystyle 2\pi~[rad]$", fontsize=20)
ans.text(0.5, 1-3/(h), r"$\displaystyle = 2\times 180~[^\circ~] = 360~[^\circ~]$", fontsize=20)
#
# 問題の作成
def main(x):
    rad = x
    deg = np.rad2deg(x)
    pra.text(0.1, 1-(j+3)/(h), "("+str(j)+")", fontsize=20)
    ans.text(0.1, 1-(j+3)/(h), "("+str(j)+")", fontsize=20)
    if b+2*a*c == 0:
        pra.text(0.2, 1-(j+3)/(h), r"$\displaystyle 0~[rad]$", fontsize=20)
        ans.text(0.2, 1-(j+3)/(h), r"$\displaystyle 0~[rad]$", fontsize=20)
    elif b+2*a*c == a:
        pra.text(0.2, 1-(j+3)/(h), r"$\displaystyle \pi~[rad]$", fontsize=20)
        ans.text(0.2, 1-(j+3)/(h), r"$\displaystyle \pi~[rad]$", fontsize=20)
    elif b+2*a*c == -a:
        pra.text(0.2, 1-(j+3)/(h), r"$\displaystyle -\pi~[rad]$", fontsize=20)
        ans.text(0.2, 1-(j+3)/(h), r"$\displaystyle -\pi~[rad]$", fontsize=20)
    elif a == 1:
        pra.text(0.2, 1-(j+3)/(h), r"$\displaystyle "+str(b+2*c)+"\pi~[rad]$", fontsize=20)
        ans.text(0.2, 1-(j+3)/(h), r"$\displaystyle "+str(b+2*c)+"\pi~[rad]$", fontsize=20)
    else:
        pra.text(0.2, 1-(j+3)/(h), r"$\displaystyle \frac{"+str(b+2*a*c)+"}{"+str(a)+"}\pi~[rad]$", fontsize=20)
        ans.text(0.2, 1-(j+3)/(h), r"$\displaystyle \frac{"+str(b+2*a*c)+"}{"+str(a)+"}\pi~[rad]$", fontsize=20)
    ans.text(0.5, 1-(j+3)/(h), r"$\displaystyle ="+sy.latex(round(deg))+"~[^\circ~]$", fontsize=20)
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
#
pra.savefig("pra.pdf")
ans.savefig("ans.pdf")
