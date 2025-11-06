#### Xavier Nazario
#### Student ID 2512208
## Pseudocode
## Step 1 Set odd multiples of 19 that are
##  more than 60 and less then 200, those are
##  95, 133, and 171.
## Step 2 Prompt user for multiples in int
##  format.
##      If input is good, display good input
##      and other factor else display bad input.

## Code for program3_2.py

def main():

# Set multiples of 19 that are >60 and <200
    x = 95
    y = 133
    z = 171

# Prompt user for multiples
    odd_mult = int(input('Enter an odd multiple that is > 60 and < 200 '))
    if odd_mult == x or odd_mult == y or odd_mult == z:
        print('Good input, factors are 95, 133, 171')
    else:
        print('Bad input')

main()
