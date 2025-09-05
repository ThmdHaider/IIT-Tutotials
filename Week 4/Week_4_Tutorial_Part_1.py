a = 1
b = 1.5

cond1 = (3 * a == 2 * b)
cond2 = (a < b) or (b < a)
cond3 = not (a < b) or not (a < (b - a))
cond4 = ((a == b) or not (b < a)) and ((a < b) or (b == a + 1))

print("1. 3 * a == 2 * b →", cond1)
print("2. (a < b) or (b < a) →", cond2)
print("3. not (a < b) or not (a < (b - a)) →", cond3)
print("4. ((a == b) or not (b < a)) and ((a < b) or (b == a + 1)) →", cond4)

