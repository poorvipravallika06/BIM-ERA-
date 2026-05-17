 #DAY - 1 TASKS 
'''1. Check whether employee age is above 21 and salary is above 30000
age = int(input("enter your age:"))
salary = int(input("enter your salary:"))
if age > 21 and salary > 30000:
    print("you are eligible for the job")
else:
    print("you are not eligible for the job")
    
#2. Check whether student passed in two subjects
subject1 = int(input("enter your marks in subject 1:"))
subject2 = int(input("enter your marks in subject 2:"))
if subject1 >=35 and subject2 >= 35:
    print("you have passed in both the subjects")
else:
    print("you have failed in one or both the subjects")
    
#3.Check whether entered value is between two ranges
value = int(input("enter a value:"))
if value >= 10 and value <= 20:
    print("the value is between 10 and 20")

#4.Check whether username and password are correct
username ="admin"
password=1234
username_1= input("enter your username:")
password_1= int(input("enter your password:"))
if(username_1 == username and password_1 == password):
    print("login successful")
else:
    print("login failed")

#5.Check whether temperature is within safe range
temperature = int(input("enter the temperature:"))
if temperature >=0 and temperature <= 100:
    print("the temperature is within safe range")
else:
    print("the temperature is not within safe range")

#6.Check whether both entered numbers are even
number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))
if number1 % 2 == 0 and number2 % 2 == 0:
    print("both numbers are even")
else:
    print("at least one number is not even")

#7.Check whether both entered numbers are positive
number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))
if number1 > 0 and number2 > 0:
    print("both numbers are positive")
else:
    print("at least one number is not positive")
    
#8.Check whether person is eligible for driving
age = int(input("enter your age:"))
licence_availbility = input("do you have a driving licence? (yes/no):")
if age >= 18 and licence_availbility.lower() == "yes":
    print("you are eligible for driving")
else:
    print("you are not eligible for driving")

#9.Check whether project progress meets deadline condition
progress = int(input("enter project progress percentage:"))
if progress >= 80:
    print("project is on track to meet the deadline")   
else:   
    print("project is behind schedule and may not meet the deadline")
    
#10.Check whether attendance and marks satisfy eligibility
attendance = int(input("enter your attendance percentage:"))
marks = int(input("enter your marks percentage:"))
if(attendance >=75 and marks >=35):
    print("you are eligible for the examination")
else:
    print("you are not eligible for the examination")

#11.Check whether entered role is Admin or Manager
admin = int(input("enter your role ( Admin or Manager):"))
if admin ==  10 or admin == 20:
    print (" you are an Admin")
else:
    print("you are a manager")

#12.Check whether student scored distinction in any one subject
subject1 = int(input("enter your marks in subject 1:"))
subject2 = int(input("enter your marks in subject 2:"))
if subject1>= 75 or subject2>=75:
    print("distinction in at least one subject")
else:
    print("no distinction in any subject ")

#13.Check whether entered day is weekend
day = input("enter a day of the week:")
if day.lower()=="saturday " or day.lower()=="sunday":
    print("its a weekend")
else:
    print("its a weekday")
    
#14.Check whether selected category matches two possible values
category = input("enter a category (A or B):")
if category.upper() == "A" or category.upper() == "B":
    print("valid category") 
else:
    print("invalid category")
    
#15. Check whether salary or experience satisfies requirement
salary = int(input("enter your salary:"))
experience = int(input("enter your years of experience:"))
if salary>100000 or experience >= 2:
    print("you meet the requirements")
else:
    print("you do not meet the requirements")

#16. Check whether temperature is extremely low or high
temperature = int(input("enter the temperature:"))
if temperature < 0 or temperature > 100:
    print("the temperature is extremely low or high")
else:
    print("the temperature is within normal range")
    
#17.Check whether entered username matches predefined values
username = input("enter your username:")
if username.lower() =="admin" or username.lower() == "user":
    print("valid username") 
else:
    print("invalid username")   
    
#18.Check whether selected option belongs to given choices
option = input("enter an option (X, Y, Z):")
if option.upper() == "X" or option.upper() == "Y" or option.upper() == "Z":
    print("valid option")
else:
    print("invalid option") 
    
#19. Check whether entered city matches allowed cities
city = input("enter a city:")
if city.lower() == "vizag " or city.lower()== "hyd":
    print("allowed city")
else:
    print("not an allowed city")

#20.Check whether entered number matches predefined values
number = int(input("enter a number:"))
if number == 10 or number == 20 or number == 30:
    print("number matches predefined values") 
else:
    print("number does not match predefined values")
    
#21.Check whether user is not admin
username = input("enter your username:")
if username.lower() != "admin":
    print(" you are not an admin")
else:
    print("you are an admin")
    
#22.Check whether entered number is not positive
number = int(input("enter a number:"))
if(number <= 0):
    print("the number is not positive")
else:
    print("number is positive")
    
#23.Check whether entered value is not empty
value = input("enter a value:")
if value.strip() != "":
    print("the value is not empty ")
else:
    print("the value is empty")

#24.Check whether file is not available
file_name = input("enter the file name:")
if file_name.strip() != "":
    print("the file is available")
else:
    print("the file is not available")

#25.Check whether employee is not active
employee_status = input("enter employee status (active/inactive):")
if employee_status.lower() != "active":
    print("the employee is not active")
else:
    print("the employee is active")
    
#26.Check whether project status is not completed
project_status = input("enter project status (completed/in progress):")
if project_status.lower() != "completed":
    print("the project is not completed")
else:
    print("the project is completed")
    
#27.Check whether password is not correct
password = input("enter your password:")
if password != "1234":
        print(" password is not correct")
else:
    print("password is correct")
    
#28.Check whether temperature is not safe
temperature = int(input("enter the temperature:"))
if temperature != 0 and temperature != 100:
    print("the temperature is  safe")
else:
    print("the temperature is not safe")
    
#29. Check whether selected option is not allowed
option = input("enter an option :")
if option.upper() != "A" and option.upper() != "B" and option.upper() != "C":
    print("the option is not allowed")
else:
    print("the option is allowed")
    
#30. Check whether marks are not passing marks'''
marks = int(input("enter your marks:"))
if marks != 35:
    print("the marks are not passing marks")
else:
    print("the marks are passing marks")

