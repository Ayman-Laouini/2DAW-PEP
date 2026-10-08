
print("Primera")
for i in range(0, 11, 2):
    print(i)

print("\nSegunda")
for i in range(0, 11):
    if i % 2 != 0:
        continue 
    print(i)

print("\nTercera")
i = 0
while i <= 10:
    print(i)
    i = i + 2

print("\nCuarta")
i = 0
while i <= 10:
    if i % 2 != 0:
        i = i + 1
        continue
    print(i)
    i = i + 1
