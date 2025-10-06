# Problem -01 ( Divide the Asset )
area = 800
# write your code here
if area > 0 and area <= 10**9:
    res1 = area / 2
    print(res1)


# Problem -02 ( Cycle or Laptop )
money = 10000
# write your code here
if money > 0 and money <= 10**9:
    if money >= 25000:
        print("Laptop")
    elif money >= 10000 and money < 25000:
        print("Cycle")
    else:
        print("Chocolate")


# Problem -03 ( Medicine Planner )
lastDay = 11
# write your code here
for i in range(lastDay):
    if i % 3 == 0:
        print(i, " - medicine")
    else:
        print(i, " - rest")


# Problem 04 - (Delete / Store)
fileName = "pdfData.jpg"
# write your code here
splitName = fileName.split(".")
if (
    splitName[0][0] == "#"
    or splitName[len(splitName) - 1] == "pdf"
    or splitName[len(splitName) - 1] == "docx"
):
    print("Store")
else:
    print("Delete")
