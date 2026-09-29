# Simple Python Program for Beginner Tech Students
# This program teaches basic Python concepts

# 1. VARIABLES AND DATA TYPES
print("=== LESSON 1: VARIABLES AND DATA TYPES ===")
name = "Alice"
age = 15
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# 2. BASIC ARITHMETIC
print("\n=== LESSON 2: BASIC ARITHMETIC ===")
num1 = 10
num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")

# 3. CONDITIONAL STATEMENTS (IF/ELSE)
print("\n=== LESSON 3: CONDITIONAL STATEMENTS ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# 4. LOOPS (FOR LOOP)
print("\n=== LESSON 4: LOOPS ===")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# 5. LISTS
print("\n=== LESSON 5: LISTS ===")
fruits = ["Apple", "Banana", "Orange", "Mango"]
print(f"My favorite fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Number of fruits: {len(fruits)}")

# 6. FUNCTIONS
print("\n=== LESSON 6: FUNCTIONS ===")
def greet(name):
    """A simple function that greets someone"""
    return f"Hello, {name}! Welcome to coding!"

message = greet("Student")
print(message)

# 7. SIMPLE CALCULATOR FUNCTION
def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

result = add_numbers(7, 3)
print(f"7 + 3 = {result}")

print("\n=== CONGRATULATIONS! You've learned the basics of Python! ===")
