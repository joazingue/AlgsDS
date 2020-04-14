"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input:
    x = 1,
    y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

x = list("{0:b}".format(1).zfill(5))
y = list("{0:b}".format(4).zfill(5))

print(x)
print(y)

bits_x = [0]*8
bits_y = [0]*8
