# Assignment Operators

a = 48

print("Assignment Operators")
print("---------------------")

a += 12
print("+= :", a)

a -= 10
print("-= :", a)

a *= 3
print("*= :", a)

a /= 5
print("/= :", a)

a %=16
print("%= :",a)

print()

# Membership Operators

colors = ["Red", "Blue", "Green"]

print("Membership Operators")
print("---------------------")

print("Blue" in colors)
print("Black" in colors)
print("Black" not in colors)

print()

# Identity Operators

x = [5, 15, 25]
y = x
z = [5, 15, 25]

print("Identity Operators")
print("---------------------")

print(x is y)
print(x is z)
print(x is not z)