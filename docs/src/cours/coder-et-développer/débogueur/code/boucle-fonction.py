def test_égalité(i, x):
    print("fonction test_égalité avec comme paramètre :", i, x)
    if x == i:
        print("égalité !")


x = 4
for i in range(10):
    print(i)
    test_égalité(i, x)

print("c'est fini.")
