def check_color(color1, color2):
    if color1 == "красный":
        if color2 == "синий":
            return "фиолетовый"
        elif color2 == "желтый" or color2 == "жёлтый":
            return "оранжевый"
        else:
            return "error"
    elif color1 == "синий" and color2 == "желтый":
        return "зелёный"
    else:
        return "error"


color1 = input("Введите первый цвет: ").strip().lower()
color2 = input("Введите второй цвет: ").strip().lower()
k = ''

if check_color(color1, color2) == 'error':
    k = color1
    color1 = color2
    color2 = k

print(check_color(color1, color2))