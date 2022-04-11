
c = [x * x for x in range(0, 10) if x * x % 2 == 0]
print(c)

from math import sqrt
p = [(o, a, h) for o in range(1, 14) for a in range(1, o) if (h := sqrt(o*o+a*a)) % 1 == 0]
print(p)