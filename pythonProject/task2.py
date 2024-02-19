seat = int(input())

if seat % 6 == 0 or seat % 6 == 5:
    if seat % 6 == 0:
        print("Боковое верхнее")
    else:
        print("Боковое нижнее")
elif seat % 6 == 1 or seat % 6 == 3:
    print("Нижнее в купе")
else:
    print("Верхнее в купе")