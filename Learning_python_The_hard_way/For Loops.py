x = "Abishek Bacchan"
for i in x:
    print(i, end=",")
print("\n")
print("----------------------------")
for i in x:
    print(i)
print("\n")
print("\n")
for i in x:

    if i == "b" or i == "B":
        print("this is special ")
    else:
        print(i)


list1 = ["red", "blue", "green", "alpha", "orange", "purple"]
colors = ["red", "blue", "green", "alpha", "orange", "purple", [1, 2, 3, 4, 5, 6, 7, 8]]
print("----------------------------")
for i in list1:
    print(i)
print("\n")
print("\n")
print("\n")
print("----------------------------")
for j in colors:
    print(j)
print("----------------------------")
for k in range(20):
    print(k)
print("----------------------------")
for k in range(20):
    print(k + 1)
print("----------------------------")
for k in range(19990, 20000):
    print(k)
print("----------------------------")
for k in range(0, 20, 5):
    print(k)
print("----------------------------")
for i in range(-5, 20):
    if i < 1:
        continue
    elif i > 10:
        break
    else:
        print("5 x ", i, " =", i * 5)
