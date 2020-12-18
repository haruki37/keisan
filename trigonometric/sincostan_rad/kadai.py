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
pra = plt.figure(figsize=(8,n))
ans = plt.figure(figsize=(8,n))
pra.text(0.1, 1-1/(n+3), "tip1:", fontsize=20)
pra.text(0.1, 1-2/(n+3), "tip2:", fontsize=20)
pra.text(0.2, 1-1/(n+3), r"$\displaystyle \pi$", fontsize=20)
pra.text(0.2, 1-2/(n+3), r"$\displaystyle 2\pi$", fontsize=20)
pra.text(0.5, 1-1/(n+3), r"$\displaystyle = 180^\circ$", fontsize=20)
pra.text(0.5, 1-2/(n+3), r"$\displaystyle = 2\times 180^\circ = 360^\circ$", fontsize=20)
#
# 問題の作成
def theta(x):
    rad = x
    deg = np.rad2deg(x)
    pra.text(0.1, 1-(j+2)/(n+3), "("+str(j)+")", fontsize=20)
    ans.text(0.1, 1-(j+2)/(n+3), "("+str(j)+")", fontsize=20)
    if b+2*a*c == 0:
        pra.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle 0$", fontsize=20)
        ans.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle 0$", fontsize=20)
    elif b+2*a*c == a:
        pra.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle \pi$", fontsize=20)
        ans.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle \pi$", fontsize=20)
    elif b+2*a*c == -a:
        pra.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle -\pi$", fontsize=20)
        ans.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle -\pi$", fontsize=20)
    elif a == 1:
        pra.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle "+str(b+2*c)+"\pi$", fontsize=20)
        ans.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle "+str(b+2*c)+"\pi$", fontsize=20)
    else:
        pra.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle \frac{"+str(b+2*a*c)+"}{"+str(a)+"}\pi$", fontsize=20)
        ans.text(0.2, 1-(j+2)/(n+3), r"$\displaystyle \frac{"+str(b+2*a*c)+"}{"+str(a)+"}\pi$", fontsize=20)
    ans.text(0.5, 1-(j+2)/(n+3), r"$\displaystyle ="+sy.latex(round(deg))+"^\circ$", fontsize=20)
def main(x):
    sin_theta = np.sin(x)
    print("sin(" + str(b+2*a*c) + "/" +str(a) + ")=")
    print(round(sin_theta, 3))
    cos_theta = np.cos(x)
    print("cos(" + str(b+2*a*c) + "/" +str(a) + ")=")
    print(round(cos_theta, 3))
    tan_theta = np.tan(x)
    print("tan(" + str(b+2*a*c) + "/" +str(a) + ")=")
    print(round(tan_theta, 3))

j = 1
while j<= n:
    a = random.choice([4, 6])
    b = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12])
#    c = random.randrange(ncs,ncl)
    c = 0
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
    theta_rad = b/a*pi + 2*pi*c
#    theta(theta_rad)
    main(theta_rad)
    j += 1
#
pra.savefig("pra.pdf")
ans.savefig("ans.pdf")
