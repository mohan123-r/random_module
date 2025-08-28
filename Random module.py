# Rock,Scissor,Paper Game
'''import random
print("---WELCOME TO Rock,Scissor,Paper Game---")
print("TYPE STOP TO STOP THE GAME")
while True:
    user=input("Enter the user choice:").lower()
    a=['rock','paper','scissor']
    system=random.choice(a)
    print(f'System has selected {system}, hence result is...')
    if user=='stop':
        print("Game End...")
        break
    elif user==system:
        print("Result Is Tie...")
    elif (user=='rock' and system=='paper') or (user=='paper' and system=='scissor') or (user=='scissor' and system=='rock'):
        print("System Won The Game...")
    elif (user=='paper' and system=='rock') or (user=='scissor' and system=='paper') or (user=='rock' and system=='scissor'):
         print("User Won The Game...")
    else:
        print("Invalid Choice...")'''

#Dice Game
'''import random
print("---WELCOME TO THE DICE GAME---")
print("Enter '0' to stop the game")
user_score=0
system_score=0
while True:
    user=int(input("Enter any number from 1 to 6:"))
    if user==6:
        i=0
        while i<2:
            print("You Entered 6")
            user_score+=user
            user=int(input("Enter again any Number from 1 to 6:"))
            if user!=6:
                user_score+=user
                break
            i=i+1
        else:
            break
    elif 1<=user<=5:
        user_score+=user
    system=random.randint(1,6)
    print("system entered number:",system)
    if system==6:
        i=0
        while i<2:
            print("System Entered 6")
            system_score+=system
            system=random.randint(1,6)
            print("System Enter again any Number from 1 to 6:",system)
            if system!=6:
                system_score+=system
                break
            i=i+1
        else:
            break
    elif 1<=system<=5:
        system_score+=system
print(user_score)
print(system_score)'''

#method 2
'''import random
print("---WELCOME TO THE DICE GAME---")
print("---LET'S PLAY THE GAME---")
print("Enter 0 to stop the game")
user_score=0
system_score=0
while True:
    user=int(input("Enter any number from 1-6:"))
    if user==6:
        print("user entered 6")
        user_score+=user
        user=int(input("Enter again any number from 1-6:"))
        if user==6:
            print("user entered 6 again")
            user_score+=user
            user=int(input("Enter again any number from 1-6:"))
            if user==6:
                break
            else:
                user_score+=user
        else:
            user_score+=user
    elif 1<=user<=5:
        user_score+=user
    system=random.randint(1,6)
    print("System Entered number from 1-6:",system)
    if system==6:
        print("system entered 6")
        system_score+=system
        system=random.randint(1,6)
        print("System again Entered number from 1-6:",system)
        if system==6:
            print("system entered 6 again")
            system_score+=system
            system=random.randint(1,6)
            print("System again Entered number from 1-6:",system)
            if system==6:
                break
            else:
                system_score+=system
        else:
            system_score+=system
    elif 1<=system<=5:
        system_score+=system
print(user_score)
print(system_score)
if user_score > system_score:
    print("USER WON THE GAME")
else:
    print("SYSTEM WON THE GAME")'''

#Find Crush's Favorite Food
'''import random
food=['Biryani','Mutton','Kheer','Chicken','poori','Roti','Masala Dosa']
fav_food=random.choice(food)
print(f'Jaanu Favorite Food is "{fav_food}"')'''

#predict future of your bestfriend
'''import random
future=['Dcoctor','Teacher','Software Engineer','Thief','CM','Police']
option=random.choice(future)
print(f'My Friend Will Become A {option}')'''

#LOVE CALCULATOR
'''import random
user=input("Enter your name:")
crush=input("Enter your crush name:")
percent=random.uniform(20,100)
if percent>90:
    print(" Ohhhhho, very Lucky Person")
elif 70<=percent<=90:
    print("One Sided, Good person, do not fall in bad habits....")
elif 50<=percent<70:
    print("Abhi sochle yaar, koi dusri dhundle...")
elif 35<=percent<50:
    print("Love is waste of time...")
else:
    print("No one likes you ,focus on carrier")'''

#Mobile Lock Screen
'''import time
while True:
    sol=0
    attempts=3
    while attempts>0:
        print(f'Attempts left {attempts}')
        user=input("Enter the password:")
        if user=='py@123':
            print("Mobile Lock Opened")
            sol=1
            break
        print("Tyr Again..")
        attempts=attempts-1
    else:
        print("Locked for 5 Seconds")
        time.sleep(5)
    if sol==1:
        break'''

#rock-paper-scissor user will enter the game only if he looses the first attempt
#if tie continue or exit
#if user wins game will come to an end
'''import random
print("---WELCOME TO Rock,Scissor,Paper Game---")
print("TYPE STOP TO STOP THE GAME")
while True:
    user=input("Enter the user choice:").lower()
    a=['rock','paper','scissor']
    system=random.choice(a)
    print(f'System has selected {system}, hence result is...')
    if user == "stop":
        print("game end..")
        break
    elif user==system:
        print("Result Is Tie...")
        print("you want to continue or exit the game...")
        ch=input("enetr your choice to continue or stop the game:")
        if ch=="continue":
            continue
        elif ch=="stop":
            print("Game End...")
            break
        else:
            print("invalid choice")
            break
    elif (user=='rock' and system=='paper') or (user=='paper' and system=='scissor') or (user=='scissor' and system=='rock'):
        print("System Won The Game...")
        continue
    elif (user=='paper' and system=='rock') or (user=='scissor' and system=='paper') or (user=='rock' and system=='scissor'):
         print("User Won The Game...")
         break
    else:
        print("Invalid Choice...")'''

#wap to login ton phonepe by entering the correct otp
'''import random
while True:
    OTP=random.randint(1000,9999)
    print("Generated OTP:",OTP)
    user=int(input("Enter the OTP:"))
    if user == OTP:
        print("Phonepe Is Logged In Successfully...")
        break
    else:
        print("Invalid OTP Please Try Again...")'''

import random
percent=random.randint(1,100)
def Love(): 
    name=input("Enter your name:")
    crush=input("Enter your crush name:")
    if percent>90:
        print("your love percentage is:",percent)
        print(f'{name} and {crush} your made for each other get marrried soon')
    elif 70<=percent<=90:
        print("your love percentage is:",percent)
        print(f'{name} and {crush} your Love is strong continue your love for some more days')
    elif 50<=percent<70:
        print("your love percentage is:",percent)
        print(f'{name} and {crush} Your love is 50 50 You have second chance')
    elif 35<=percent<50:
        print("your love percentage is:",percent)
        print(f'{name} and {crush} love is not good for you best friends is the better option')
    else:
        print("your love percentage is:",percent)
        print(f'{name} and {crush} please dont love any one be single always')
Love()
Love()
Love()
                    











