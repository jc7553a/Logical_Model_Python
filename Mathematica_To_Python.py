import re

poly = 'x+y+2*x*y+x**2*y+x*y**2+x**2*y**2'
def maxPoly (polynomial, xVar, yVar):
    num_states = 3
    polynomial.replace('x', xVar)
    polynomial.replace('y', yVar)
    print(polynomial)

if __name__ == '__main__':
    global poly
    maxPoly(poly, 'x2', 'x8')
            
