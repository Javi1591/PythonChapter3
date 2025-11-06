#### Xavier Nazario
#### Student ID 2512208

## Pseudocode for program3_1.py
## Step 1 Set base hours and overtime variables and formula.
## Step 2 Get hourly pay rate and hours worked and
##  assign variables, use float.
## Step 3 Calculate reg pay, any overtime pay and display.
## Step 4 Calculate total pay and asssign variable, then
##  display.


## Code

def main():

# Set base hours and overtime multiplier
    base_hours = 40     # Max weekly hours
    ot_mult = 1.5

# Get hourly pay rate and hours worked
    pay = float(input('Enter the hourly pay rate '))
    hours = float(input('Enter the hours worked last week '))

# Calculate reg and overtime pays and display
    if hours > base_hours:
        ot_hours = hours - base_hours
        overtime_pay = ot_hours * pay * ot_mult
        reg_pay = base_hours * pay
    else:
        reg_pay = hours * pay
        overtime_pay = 0
    print(f'Regular pay: ${reg_pay:,.2f}')
    print(f'Overtime pay: ${overtime_pay:,.2f}')

# Calculate total pay and display
    tot_pay = reg_pay + overtime_pay
    print(f'Total pay: ${tot_pay:,.2f}')

main()
