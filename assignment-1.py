name = "Risqua"
age = 33
height = 5.4
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2: User Input and Math
user_name = input("\nWhat is your name? ")
birth_year = int(input("What year were you born? "))

current_year = 2026
age = current_year - birth_year

print(f"Hi, {user_name}! You are {age} years old.")

# Section 3: Type Conversion and f-strings
first_number = float(input("\nEnter the first number: "))
second_number = float(input("Enter the second number: "))

product = first_number * second_number


print(f"The result of {first_number} × {second_number} = {product}")

# Section 4: Formatted Receipt
item_name = "Notebook"
price = 4.75
quantity = 3
total = price * quantity

print("\n===========================")
print("          RECEIPT")
print("===========================")
print(f"Item:      {item_name}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")

# Section 5: Mini-Project — Profile Card
profile_name = input("\nWhat is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("What is one fun fact about you? ")
profile_birth_year = int(input("What year were you born? "))

profile_age = current_year - profile_birth_year

print("\n================================")
print(f"PROFILE: {profile_name}")
print("================================")
print(f"Hometown:  {hometown}")
print(f"Hobby:     {hobby}")
print(f"Fun fact:  {fun_fact}")
print(f"Age:       {profile_age}")
print("================================")
