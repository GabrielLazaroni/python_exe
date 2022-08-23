from random import randint

num = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
for i in num:
    print(f"{i}")
print(f"o maior valor é {max(num)}")
print(f"o menor valor é {min(num)}")
