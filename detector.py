text = input("Enter your text: ")

upper = 0
lower = 0
space = 0
number = 0
plus = 0
minus = 0
multiply = 0
division = 0
special = 0

in_number = False

for x in text:

    if x.isupper():
        upper += 1
        in_number = False

    elif x.islower():
        lower += 1
        in_number = False

    elif x == ' ':
        space += 1
        in_number = False

    elif x == '+':
        plus += 1
        in_number = False

    elif x == '-':
        minus += 1
        in_number = False

    elif x == '*':
        multiply += 1
        in_number = False

    elif x == '/':
        division += 1
        in_number = False

    elif x.isdigit() or x == '.':
        if not in_number:
            number += 1
            in_number = True

    else:
        special += 1
        in_number = False

word = 0

for x in text.split():
    if x.isalpha():
        word += 1

print("=============================================================")
print("============== You use in your text =========================")
print("Word ========================", word)
print("Upper Case letter ===========", upper)
print("Lower Case letter ===========", lower)
print("Space =======================", space)
print("Number (floating + intiger) =", number)
print("Plus sign ===================", plus)
print("Minus sign ==================", minus)
print("Multiply sign ===============", multiply)
print("Division sign ===============", division)
print("Special Character ===========", special)
print("===============================================================")
print("===============================================================")