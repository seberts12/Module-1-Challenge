# coding: utf-8
import csv
from pathlib import Path


loan_costs = [500, 600, 200, 1000, 450]

# First, I will calculate how many loans are in 'loan_costs' by using len() and print() functions

number_of_loans = len(loan_costs)
print(f"The total number of loans is {number_of_loans}.")

# Next, I will calculate the total amount of all loans from loan_costs using sum() and print() functions. 

total_of_loans = sum(loan_costs)
print(f"The total amount of all loans is ${total_of_loans}.")

# Finally, I calcualte the average dividing total_of_loans by number_of_loans

average_loan_price = total_of_loans / number_of_loans
print(f"The average loan price is ${average_loan_price:.2f}.")



loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Finding the future value from the above dictionary 'loan' using the get() function

future_value = loan.get("future_value")
print(f"The future value of the loan is ${future_value:.2f}.")

# Finding the remaining time of the loan from the dictionary, 'loan'

remaining_months = loan.get("remaining_months")
print(f"The loan has {remaining_months} months until maturity.")



# Using the present value equation to find the true value of the loan 
# Period is by months 
# Neccessary return of 20%: Use a discount rate of .20

discount_rate = .20

fair_value = future_value / (1+(discount_rate/12)) ** remaining_months
print(f"A fair price for this loan is ${fair_value:.2f}.")


# Conditional statement used to determine whether to purchase or decline loan
# If fair value is greater than or equal loan price, purchase loan, if not, do not purchase

if fair_value >= loan.get("loan_price"):
    print("This loan is worth at least the cost to buy it.")
else:
    print("This loan is too expensive and not worth the price.")





new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# To calculate the present value of 'new_loan' I am defining a function using parameters of future_value, annual_discount_rate, and remaining_months
# Present value of loan is stored in variable 'present_value_new_loan'
# calcualate_present_value function period: months 

annual_discount_rate = .20

def calculate_present_value(future_value, annual_discount_rate, remaining_months):
    present_value = future_value / (1+(annual_discount_rate/12)) ** remaining_months
    return present_value


present_value_new_loan = calculate_present_value(
    new_loan["future_value"], 
    annual_discount_rate, 
    new_loan["remaining_months"]
    )

print(f"The present value of the new loan is ${present_value_new_loan:.2f}.")



loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# From the above data on 'loans', I am filtering out inexpesnive loans using a for loop and appending them in the list 'inexpesive_loans'
# for every loan in 'loans' if the loan price is less than or equal to $500 add to the 'inexpensive_loans' list

inexpensive_loans = []

for loan in loans:
    loan_price = loan["loan_price"]

    if loan_price <= 500:
        inexpensive_loans.append(loan)



# Creating 'header' variable to be used in the csv file 

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Setting the output file path as a cvs file named 'Inexpensive loans'

output_path = Path("inexpensive_loans.csv")

# The function below opens a csv file and tells python I will be writing into the file using 'w'; newline signals where new lines begin 
with open (output_path, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # csvwriter allows for data to convert into a file
    # writerow function converts python lists into csv rows of data 
    # writing header into the csv file 
    csvwriter.writerow(header)

    # next I convert the inexpensive loans list into csv file data 
    # Using a for loop, we interate through all the loans in the list and converts it the csv file
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())

# Notifying user the inexpensive loans list is converting to a csv file
print("converting to csv file...")

