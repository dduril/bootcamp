# Chapter 3 Code Examples

# lower() method used to compare strings
string1 = "John"
string2 = "john"
string1 == string2                  # False
string1.lower() == string2.lower()  # True
print(string1)
print(string2)

# if statement
age = 20
if age >= 18:
    print("You are eligible to vote.")

# if statement with an else clause
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# if statement with elif and else clauses
invoice_total = 950
discount_percent = 0
if invoice_total >= 1000:
    discount_percent = .2
elif invoice_total >= 500:
    discount_percent = .1
elif invoice_total > 0:
    discount_percent = 0
else:
    print("Invoice total must be greater than zero.")

# if statement used for grading
score = int(input("Enter a test score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# if statement that validates a range of a score
score = int(input("Enter a test score: "))
total_score = 0
if score >= 0 and score <= 100:
    total_score += score
else:
    print("Test scores must be between 0 and 100.")

# if statement that validates the customer type
is_valid = True
customer_type = input("Enter a customer type (m/t): ")
if customer_type.lower() == "m" or customer_type.lower() == "t":
    pass
else:
    print("Customer type must be 'm' or 't'.")
    is_valid = False

# while loop example
choice = "y"
while choice.lower() == "y":
    print("Hello!")
    choice = input("Say hello again (y/n): ")
print("Bye!")

# another while loop example
counter = 0
while counter < 10:
    print(counter, end=" ")
    counter += 1
print("\nWhile loop ended.")

# range() function
range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4, 5
range(2, 10, 2)     # 2, 4, 6, 8
range(5, 0 -1)      # 5, 4, 3, 2, 1

# for loop
for i in range(10):
    print(i, end=" ")
print("For loop ended.")
