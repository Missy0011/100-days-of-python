#if else statements >>>> odd even
#nested if else means if else under if else
height=int(input("Enter your height in cm"))
if height>=120:
    print("You are elligible")
    age=int(input("Enter your age"))
    if age>18:
     print("you have to pay 20 rs.")
    else:
     print("You have to pay 50rs.")
else:
    print("you are not elligible")
################## Leap Year ###################
year=int(input("Enter the year you want to check"))
if year%4==0:
    if year%4==0:
      if year%4==0:
          print("its a leap year")
      else:
          print("its not a leap year")  
    else:
        print("its a leap year")
else:
    print("not a leap year")
 ############### rolar coaster ride ###############
height=int(input("Enter your height"))
if height>120:
    print("You can ride here")
    age=int(input("enter your age"))
    if age <12:
        bill=110
        print("you have to pay 10 rs extra")
    elif age<18:
        bill=120
        print("you have to pay 20 rs. extra")
    else:
        if age>45 and age<55:
            bill=0
            print("you have to pay 0 rs.")
        else:
            bill=150
            print("you have to pay 50 rs.extra")
        
    photo=input("Do you wanna photo?")
    if age>18 and age<45 or age>55 and photo=="y":
        bill=bill+30
        print(f"Your total bill is {bill}")
    else:
        print(f"your bill is {bill}")
else:
    print("Sorry,you cannt ride.")


############# Pizza Order ############
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#🚨 Don't change the code above 👆

#Write your code below this line 👇
if size=="S":
    bill=15
elif size=="M":
    bill=20
else:
    bill=25
if add_pepperoni=="Y":
    if size=="S":
        bill +=2
    else:
        bill +=3
if extra_cheese=="Y":
    bill +=1
    print(f"Your final bill is:{bill}")
else:
    print(f"Your final bill is:{bill}")
    
############ Love Calculator ###########
girl=input("Enter the name of the girl")
boy=input("Enter the name of the boy")
total_name=girl+boy
lower_total_name=total_name.lower()
t=lower_total_name.count("t")
r=lower_total_name.count("r")
u=lower_total_name.count("u")
e=lower_total_name.count("e")
true=t+r+u+e
l=lower_total_name.count("l")
o=lower_total_name.count("o")
v=lower_total_name.count("v")
e=lower_total_name.count("e")
love=l+o+v+e
calculate=str(true)+str(love)
print("Your love percentage is " +calculate+" %")
calculate_int=int(calculate)
if calculate_int>70 and calculate_int<100:
    print("Super match")
elif calculate_int>50 and calculate_int<70:
    print("okok match")
elif calculate_int>30 and calculate_int<50:
    print("Get married soon")
else:
    print("not a perfect match")
print("Welcome to treasure island, if you find the correct route you win")
dir=input("Left or right?")
dir=dir.lower()
if dir=="left":
    do=input("Swim or wait?")
    do=do.lower()
    if do=="wait":
        door=input("Which door? Red,Yellow,Blue")
        door=door.lower()
        if door=="red" or door=="blue":
            print("Game Over")
        elif door=="yellow":
            print("You Win")
    else:
        print("Game Over")
else:
    print("Game Over")