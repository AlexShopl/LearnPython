import random

N=random.randint(1,100)   
userGuess=-1

print("Привет, давай поиграем в угадай число. Я загадываю число от 1 до 100.")

while userGuess!=N:      
    userGuess=int(input("Угадай число от 1 до 100: "))      
    if userGuess > N:        
        print("Число должно быть меньше!")
    elif userGuess < N:         
        print("Число должно быть больше!")      
    else:         
        print("Вы угадали, это число = " + str(N))  
        print("Конец игры")         

#Конец игры
