first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
if first==third and first==second:
    print(3)
elif first==third or first==second or second==third:
    print(2)
else:
    print(0)