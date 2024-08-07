numberGrade = int(input())
def grade (a):
    if a <= 100 and a >= 85:
        return "A"
    elif a<=84 and a>=70:
        return "B"
    elif a<=69 and a>=60:
        return "C"
    elif a<=59 and a>=50:
        return "D"
    else:
        return "F"
print(grade(numberGrade))