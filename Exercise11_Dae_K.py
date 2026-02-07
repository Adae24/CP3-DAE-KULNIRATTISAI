#Input
heightPyr = int(input("Height:"))

#Output
for x in range(heightPyr):
    text = " "
    for y in range(heightPyr-x-1):
        print(text, end="")
    for y in range(x + 1):
        print("*", end=" ")
    print(text)



