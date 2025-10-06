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
