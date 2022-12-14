"""
5 * 3 = 5 + 5 + 5
      = 5 + (5 * 2)
      = 5 + 5 + (5 * 1)
      = 5 + 5 + 5
      = 15
"""
def producto(n1, n2):
    if n2 == 1:
        return n1
    else:
        return n1 + producto(n1, n2 - 1)

print(producto(5, 3))