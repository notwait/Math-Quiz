from random import randrange
import math
score = 0
while True:
    rounds = input("How many rounds you want to play? ")
    try:
       rounds = int(rounds)
       if rounds <= 0:
            int('NopeUDon\'ti')
       breaker = True
    except:
       print("This isn't a number or it is 0 or lower")
       breaker = False
    if breaker:
        break
difficulty = ""
while not ((difficulty.lower() == "automatic") or (difficulty.lower() == "easy") or (difficulty.lower() == "normal") or (difficulty.lower() == "hard")):
    difficulty = input("Choose Difficulty [Automatic, Easy, Normal, Hard] ")
for x in range(rounds):
    if score < 0:
        print('Sadly, you lost :( Restart the file so you can play one more time!')
        break
    if difficulty.lower() == "easy" or difficulty.lower() == "automatic":
        FirstNum = randrange(1, 10)
        SecondNum = randrange(1, 10)
        if randrange(1,2) == 1:
            Operator = "+"
        else:
            Operator = "-"
        if not difficulty.lower() == "automatic":
            ans = input("How much is " + str(FirstNum) + Operator + str(SecondNum) + "?")
        else:
            print(str(FirstNum) + Operator + str(SecondNum))
        if not difficulty.lower() == "automatic":
              if Operator == "+":
                if int(ans) == FirstNum + SecondNum:
                    print('Correct!', FirstNum, Operator, SecondNum, "=", ans, "+200 Score")
                    score += 200
                else:
                    print('Wrong! -100 Score')
                    score -= 100
              else:
                if int(ans) == FirstNum - SecondNum:
                    print('Correct!', FirstNum, Operator, SecondNum, "=", ans, "+200 Score")
                    score += 200
        else:
            if Operator == "+":
                print(FirstNum + SecondNum)
            else:
                print(FirstNum - SecondNum)
    if difficulty.lower() == "normal":
        FirstNum = randrange(1, 100)
        SecondNum = randrange(1, 100)
        X = randrange(1,4)
        if X == 1:
            Operator = "+"
        elif X == 2:
            Operator = "-"
        elif X == 3:
            Operator = "×" #Este sinal foi posto aqui com o mapa de caracteres
        elif X == 4:
            Operator= "÷" #Este aqui também
        ans = input('How much is floor(' + str(FirstNum) + Operator + str(SecondNum) + ')?')
        try:
            int(ans)
        except ValueError:
            X = 5
        if ((X == 1) and (FirstNum + SecondNum == int(ans)) or (X == 2) and (FirstNum - SecondNum == int(ans))) or ((X == 3) and (FirstNum * SecondNum == int(ans)) or (X == 4) and (int(FirstNum / SecondNum) == int(ans))):
            print('Correct! floor(', FirstNum, Operator, SecondNum, ") =", ans, "Score +200")
            score += 200
        else:
            print("Wrong! -100 Score")
            score -= 100
    if difficulty.lower() == 'hard':
        spacing = ' '
        FirstNum = randrange(1, 100)
        SecondNum = randrange(1, 100)
        if (X := randrange(3, 6)) == 3:
            Operator = "×"
        elif X == 4:
            Operator= "÷" 
        elif X == 5:
            Operator = "!"
            spacing = ''
            SecondNum = ''
            FirstNum = (FirstNum % 10) + 1
        ans = input('How much is floor(' + str(FirstNum) + Operator + str(SecondNum) + ')?')
        try:
            int(ans)
        except ValueError:
            X = -1
        if ((X == 1) and (FirstNum + SecondNum == int(ans)) or (X == 2) and (FirstNum - SecondNum == int(ans))) or ((X == 3) and (FirstNum * SecondNum == int(ans)) or (X == 4) and (int(FirstNum / SecondNum) == int(ans)) or ((X==5) and (math.factorial(FirstNum) == int(ans)))):
            print('Correct! floor(', str(FirstNum) + spacing + str(Operator) + spacing + str(SecondNum) + ") =", ans, "Score +200")
            score += 200
        else:
            print("Wrong! -100 Score")
            score -= 100
        
