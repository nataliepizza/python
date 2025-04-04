# what are variables 
# there are different types of variables 
# strings are text
name="john" #qutation marks
name2="lucy"
# integers are whole numbers
num1 = "10" #no quotation marks
num2 = 20 
print(int(num1)+ num2) #when you have a + sign beetween two variables its called #concatenation
# floats are decimal numbers
#type casting 
# booleans are true or false
# lists are collections of values
# dictionaries are collections of key-value pairs
#f strinfs allow us to insert variables into strings
# using f before the string
print(name+ "and" +name2 + "have" + num1 + str(num2) + "apples")
print(f"{name} and {name2} have {num1} apples")
dollars= 10.99
print(f"{name} has {dollars} dollars")\
#print(name+ "and" +name2 + "have" + num1 + str(num2) + "apples")
#floats are decimal numbers
its_student = True
print(f"{name} is a student: {its_student}")

dog= "charlie"
name3="Nat"
food="brownie"
drink="matcha"
name4="Yari"
print(f"{name3} and {name4} take {dog} on a walk to get {food} and {drink}")