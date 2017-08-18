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
    print("You are too young to vote.")

# if statement with elif and else clauses
invoice_total = 450
discount_percent = 0
if invoice_total >= 500:
    discount_percent = .2
elif invoice_total >= 250:
    discount_percent = .1
elif invoice_total > 0:
    discount_percent = 0
else:
    print("Invoice total must be greater than zero.")

# if statement used for grading
score = int(input("Enter test score: "))
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
score = int(input("Enter test score: "))
total_score = 0
if score >= 0 and score <= 100:
    total_score += score
else:
    print("Test score must be between 0 and 100.")

# if statement that validates the customer type
is_valid = True
customer_type = input("Enter customer type (r/w): ")
if customer_type.lower() == "r" or customer_type.lower() == "w":
    pass
else:
    print("Customer type must be 'r' or 'w'.")
    is_valid = False


