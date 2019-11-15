import random2
generatedNum = round(random2.random() * 100)
userNum = int(input("Я загадал число от 0 до 100, попробуйте его угадать: "))
while True:
    if userNum == generatedNum:
        print("Молодец ты угадал число!")
        quit = input("Желаете выйти? (y/n): ")
        if quit == "y":
            break
        else:
            generatedNum = round(random2.random() * 100)
            userNum = int(input("Я загадал число от 0 до 100, попробуйте его угадать: "))
            continue
    elif userNum > generatedNum:
       userNum = int(input("Число слишком большое, попробуйте заново!: "))
       continue
    elif userNum < generatedNum:
       userNum = int(input("Число слишком маленькое, попробуйте заново!: "))
       continue