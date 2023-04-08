# Bag Problem

here are my results:
```
filtered = 0.600306
inside = 0.5010007655856731
outside = 0.498999234414327
```

## Mathematical Proof
'''
P(A|B) = P(B|A)P(A)/P(B)
A = is in pocket 4, B = is not in 1-3
P(B|A) = 100% (given it is in pocket 4, it cannot be in pockets 1-3)
P(A) = 20% (equal chance among all 4 pockets)
P(B) = 40% (20% chance it is in pocket 4, 20% chance it is not in any pocket)
P(A|B) = 1 * 0.2 / 0.4
P(A|B) = 50%
