#### Xavier Nazario
#### Student ID 2512208
## Pseudocode
## Step 1 Prompt user for two digit integer.
## Step 2 Determine whether good or bad input,
##  if bad, display bad input
##  else prompt for second two digit integer.
## Step 3 Compare both numbers and display.

## Code for program_.py

def main():

# Prompt for 2 digit interger and determine input, the prompt for
#   second integer
    num1 = int(input('Please enter a two digit integer:'))
    if num1 < 10 or num1 > 99:
        print('Bad entry')
    else:
        num1 >= 10 or num1 <= 99
        num2 = int(input('Pleae enter another two digit integer:'))
        if num2 < 10 or num2 > 100: #determine input
            print('Bad entry')
        else:   #compare input
            num3 = num2 - num1
            print(f'The number {num2} is {num3} larger than the ',
                  f'number {num1}.')
    
main()
