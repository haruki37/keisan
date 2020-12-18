"""
    test.py
"""
import sympy as sy

from latexfile import LatexFile


def main():
    tex = LatexFile('calc_result', title='Calculation result', point=9)
    tex.add_eq('1 + 1 = ' + sy.latex(1 + 1))
    tex.add_eqs([
        '1 + 2 = ' + sy.latex(1 + 2),
        '1 + 3 = ' + sy.latex(1 + 3)
    ])
    tex.compile()


if __name__ == '__main__':
    main()
