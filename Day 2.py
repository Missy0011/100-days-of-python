print(len("57474"))
print("hello"[3]) #subscriptinng
print("123"+"456")#variable operation
print(123+345)#mathematical operation without ""
print(3.14159+5.67)#floating point number
#boolean > Ture and false
num_char=len(input("What's your name?"))
new_num_char=str(num_char)
print("Your name has "+new_num_char+" no. of letters")
c=float(123)
print(type(c))
#adding two numbers from 1 two digits number
q=input("enter a two digit number")
num1=q[0]
num2=q[1]
print(num1)
print(num2)
sum=int(num1)+int(num2)
sum1=str(sum)
print("the sum is"+sum1)
#printing summation of two digits numbers
a=input("Enter 1st two digit number?")
b=input("Enter 2nd two digit number?")
result=int(a) + int(b)
resultt=str(result)
print("The sum is "+resultt)
print(3*3)
print(2**3)  # power **
# ** > *,/ > + > -
print(3*3+3/3-3)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
height1=float(height)
weight1=float(weight)
bmi=(weight1/height1**2)
bmi1=str(bmi)
print(bmi1)
print(round(8/3, 2))
print(8//3)  # gives a round figure
result = 4/2
result /= 2
print(result)
score = 0
score += 1  # increases the value by 1
height = 1.8
iswinning = True
print("your score is " + str(score))
# or
print(f"your score is {score} and your height is {height} and your winninng is {iswinning}")
##################     Tip Calculator    #####################
print("welcome to Tip Calculator")
bill=int(input("How much is your bill?"))
tip=int(input("How much do you wanna pay? 10, 15, 20 rs. ?"))
ppl=int(input("how many people are gonna split this bill?"))
new_bill=bill+(bill*(tip/100))
per_ppl=new_bill/ppl
print(f"Your total bill including tip is {new_bill} and each person will pay {per_ppl} rs")