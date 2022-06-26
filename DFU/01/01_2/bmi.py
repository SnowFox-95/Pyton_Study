age = int(input())
height = float(input())
weight = float(input())

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")
elif age>=45:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)

    if bmi < 22:
        description = "недостаточной массой тела."
    elif bmi < 27:
        description = "нормальной массой тела."
    elif bmi < 32:
        description = "избыточной массой тела."
    else:
        description = "ожирением."

    print("bmi=", bmi, "Вы относитесь к группе людей с", description)
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)

    if bmi < 18.5:
        description = "недостаточной массой тела."
    elif bmi < 25:
        description = "нормальной массой тела."
    elif bmi < 30:
        description = "избыточной массой тела."
    else:
        description = "ожирением."

    print("bmi=", bmi, "Вы относитесь к группе людей с", description)