import random

def draw(fail):
    if fail==0:
        print("     _________")
        print("     |    |")
        print("     |    0")
        print("     |   /|\ ")
        print("     |    |")
        print("     |   / \ ")
        print("--------------")
        print()
    elif fail==1:
        print("     _________")
        print("     |    |")
        print("     |    0")
        print("     |   /|\ ")
        print("     |    |")
        print("     |       ")
        print("--------------")
        print()
    elif fail==2:
        print("     _________")
        print("     |    |")
        print("     |    0")
        print("     |    |  ")
        print("     |    |")
        print("     |       ")
        print("--------------")
        print()
    elif fail==3:
        print("     _________")
        print("     |    |")
        print("     |    0")
        print("     |       ")
        print("     |     ")
        print("     |       ")
        print("--------------")     
        print()
    elif fail==4:
        print("     _________")
        print("     |    |")
        print("     |     ")
        print("     |       ")
        print("     |     ")
        print("     |       ")
        print("--------------")     
        print()
    elif fail==5:
        print("     _________")
        print("     |     ")
        print("     |     ")
        print("     |       ")
        print("     |     ")
        print("     |       ")
        print("--------------")
        print()

def hangman():
    print("Let's play HANGMAN!!! Topic: SPORTS")
    print()
    print("May the odds be ever in your favour!!")
    print()
    print("Select difficulty level")
    print("1. Beginner: Noob")
    print("2. Intermediate (default): I know English")
    print("3. Advanced: Dictionary crammer")
    print()
    difstr=input("Enter your choice: ")
    if difstr.isnumeric():
        dif=int(difstr)
    else: 
        print("You seem to be a NOOB :) !!");
        dif=1;
    print()
    #select word list according to difficulty level
    if dif ==1: 
        word_list=["badminton", "cricket", "tennis", "hockey", "yoga", "karate", "volleyball", "basketball", "baseball", "running", "judo", "golf", "football"]
    elif dif==2:
        word_list=["archery", "badminton", "cricket", "bowling", "boxing", "tennis", "hockey", "yoga", "fitness", "gymnastics", "karate", "volleyball", "basketball", "baseball", "rugby", "cycling", "running", "fishing", "judo", "climbing", "pool", "shooting", "golf", "football"]
    elif dif==3:
        word_list=["archery", "badminton", "cricket", "bowling", "boxing", "curling", "tennis", "skateboarding", "surfing", "hockey", "yoga", "fencing", "fitness", "gymnastics", "karate", "volleyball", "weightlifting", "basketball", "baseball", "rugby", "wrestling", "cycling", "running", "fishing", "judo", "climbing", "billiards", "pool", "shooting", "golf", "football"]
    else:
        word_list=["archery", "badminton", "cricket", "bowling", "boxing", "tennis", "hockey", "yoga", "fitness", "gymnastics", "karate", "volleyball", "basketball", "baseball", "rugby", "cycling", "running", "fishing", "judo", "climbing", "pool", "shooting", "golf", "football"]
    
    word=random.choice(word_list)
    i=len(word)
    fail=5
    if dif ==1:
        maxTrials= i+ fail + 1 #Max No of times one may try
        print('Selecting noob, you have ',maxTrials,' trials, including ',fail,' wrong attempts')
    elif dif==2:
        maxTrials= i+ fail
        print('Selecting intermediate, you have ',maxTrials,' trials, including ',fail,' wrong attempts')
    elif dif==3:
        maxTrials= i
        print('Selecting dictionary crammer, you have ',maxTrials,' trials, including ',fail,' wrong attempts')
    else:
        maxTrials= i+ fail
        print('Selecting intermediate, you have ',maxTrials,' trials, including ',fail,' wrong attempts')
    ch='' # guess string
    
    draw(fail)
    print('The word is:     ', end =" ")
    for x in range(i): 
        print('_', end =" ")#for printing in same line  
    print(),print()
    
    for j in range(maxTrials):#i is the number of trials , 5 errors allowed
        print("Your guesses till now are: \"",ch,"\"")
        while True:
            ch1 = input('Enter a character: ') 
            if len(ch1)>1:
                print("Error: Please enter a single character, try again !!")
            elif ch1.lower() in ch:
                print("You have already guessed this earlier, NOT COUNTING IT :) !!")
            elif ch1.isalpha() == False:
                print("Error: Please enter an alphabet only, try again !!")
            else:
                break
                
        ch2=ch1.lower()
        if ch2 not in word:
            fail-=1
        draw(fail)
        if fail==0:
            break
        ch=ch+ch2
        noDashes=0
        print('The word is:     ', end =" ")
        for c in word:
            if c in ch:
                print(c, end =" ")
            else:
                print('_', end =" ")
                noDashes+=1
        print(),print()
        print('Remaining trials = ',maxTrials-j-1,', Remaining wrong attempts = ',fail)
        if noDashes==0:
            break
    print()
    if noDashes==0:
        print("Congratulations, You Won!!")
    else:
            print("Sorry. Better luck next time!!")
            print("The word was: ",word)
            
hangman()