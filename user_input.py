"""
f_name = input("Enter yout name: ")
age = input("Enter your age: ")

print(f" Your name is  {f_name} and your age is {age}")


# anything from input is considered  a string
#write a program that takes 2 numbers form user and display the sum of both numbers
num1 = int(input(" Enter your first number: "))
num2  = int(input(" Enter your second number: "))

sum = num1 + num2

print(sum)

# write a code to help your client with money transfer
#it should ask for user total amount to send in USD
#Then it should tell how the receiver will get in ksh
#sending fees should be 0.02 
#exchange rate should be 129
"""

sending_fees = 0.02
exchange_rate = 129
user_amount = int(input("Please enter the amount you send: "))
fee_amount = sending_fees * user_amount
amount_plus_fees = user_amount + fee_amount
receiving_amount = exchange_rate * user_amount

print(f"The total amount plus fees is $ {amount_plus_fees:,} and you family will receive ksh {receiving_amount}")

user_answer = input("Do you want to continue? (yes/no): ")
if user_answer == "yes":
    print("Proceed with payment")
else:
    print("Thank you for using our service")

   