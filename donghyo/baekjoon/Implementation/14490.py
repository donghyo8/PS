from fractions import Fraction

N, M = map(int, input().split(":"))
f = Fraction(M, N)
print(str(f.denominator) + ":" + str(f.numerator))