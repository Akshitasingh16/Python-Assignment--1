PROGRAM 1

a=int(input("Enter the first number:))
b=int(input("Enter the second number:))
c= a+b
print("The sum is:",c)

PROGRAM 2
a= int(input("Enter a number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")

PROGRAM 3
  def fact(n): 
  return 1 if n==0 
  else n*fact(n-1)
print(fact(int(input())))

PROGRAM 4
a= input("Enter your name:")
print("Hello ",a)

PROGRAM 5
temp = input("Please enter your information! ") 
try: 
	with open('gfg.txt', 'w') as gfg: 
	  gfg.write(temp) 
except Exception as e: 
   	print("There is a Problem", str(e)) 

 PROGRAM 6
 a= input("Enter the name of the file with .txt extension:")
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()

PROGRAM 7
a= input("Enter your string:")
print(len(a))

PROGRAM 8
str1= input("Enter first word:")
str2= input("Enter second word:")
c = (str1+str2)
print(c)

PROGRAM 9
str1= input("Enter the string:")
if "red" in str1:
    print("Present")
else:
    print("not present")

PROGRAM 10
str1= input("Enter the string:")
c = str1.upper()
print(c)

PROGRAM 11

PROGRAM 12
num = input("Enter Number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)

PROGRAM 13
a= int(input("Enter your birth year:"))
age = 2024-a
print(age)

PROGRAM 14
lines = []
print("Enter your lines of text. Press Enter on an empty line to finish:")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\nYou entered:")
for line in lines:
    print(line)


PROGRAM 15
import csv
with open('Giants.csv', mode ='r')as file:
csvFile = csv.reader(file)
for lines in csvFile:
		print(lines)
PROGRAM 16
string = "Yolo Life"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")

PROGRRAM 17
a= (input("Enter the string:"))
b= a.title()
print(b)

PROGRAM 18
s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")

   
    PROGRAM 19
my_string = "Hello! How are you? I'm doing well, thanks." 

new_string = "" 
for char in my_string: 
    if char not in string.punctuation: 
print(new_string)

PROGRAM 20
list1 = [1, 5, 8, 6, 7]
total = sum(list1)
print("Sum of all elements in given list: ", total)

PROGRAM 21
x= [1,2,4,5,4,6,3,2,1,4]
count=0
for i in x:
    if i== 1:
        count+=1
print(count)

PROGRAM 22
Maximum//
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", max(list1))
Minimum//
list1 = [10, 20, 1, 45, 99]
print("Smallest element is:", min(list1))

PROGRAM 23
Celcuis to fahrenheit//
temp= int(input("Enter the temperature in celcius:"))
temp2= (9/5*temp) + 32
print(temp2)

Fahrenheit to celsius//
temp= int(input("Enter the temperature in fahrenheit:"))
temp2= (temp-32)*5/9
print(temp2)

PROGRAM 24
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, *, /): ")
if operator == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use one of the following: +, *, /.")

    PROGRAM 25
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile: 
	for line in firstfile: 
			secondfile.write(line)


PROGRAM 27
input_string = input("Enter a string: ")
char_list = [char for char in input_string]
print("List of characters:", char_list)