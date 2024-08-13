n = 45
i = 0
while (True):
    a = int(input("Guess the number.\n"))
    i = i + 1
    if (i == 5):
        print ("GAME OVER.")
        break
    elif a == n:
        print ("Congrats you have guessed the number in ", i, "tries.\n")
        break
    elif a < n:
        print ("Just a little bit more. You have ",5-i, "tries left.\n")
    elif a > n:
        print ("Just a little bit lower. You have ",5-i, "tries left.\n") 
    
    else:
        print ("You have not entered a valid number. Please try again.\n")               
