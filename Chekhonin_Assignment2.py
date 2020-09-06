#!/usr/bin/env python3
"""Make calculations with numbers
Usage:
   python3 calculator.py <option>
"""

def action(option,a,b):
    """Executes function according to choosen option.
      Args:
          action: The option number.
      Returns:
          Output from choosen function.
    """
    answer = "The answer is : "
    
    if option == 1:
        print(answer+str(add(a, b)))
    elif option == 2:
        print(answer+str(subtract(a, b)))
    elif option == 3:
        print(answer+str(multiply(a, b)))
    elif option == 4:
        print(answer+str(divide(a, b)))
    elif option == 5:
        print(answer+str(power(a, b)))
    elif option == 6:
        print(answer+str(modulo(a, b)))
        
        
def subtract(a,b):
    """Fetch subtraction of entered numbers.
      Args:
          a,b: Entered numbers from user.
      Returns:
          Result of subtraction of two numbers.
    """
    return a-b


def multiply(a,b):
    """Fetch multiplication of entered numbers.
      Args:
          a,b: Entered numbers from user.
      Returns:
          Result of multiplication of two numbers.
    """
    return a*b


def divide(a,b):
    """Fetch division of entered numbers.
      Args:
          a,b: Entered numbers from user.
      Returns:
          Result of division of two numbers.
    """
    return a/b


def power(a,b):
    """Fetch power of entered numbers.
      Args:
          a,b: Entered numbers from user.
      Returns:
          Result of power of two numbers.
    """
    return a^b


def add(a,b):
    """Fetch sum of entered numbers.
      Args:
          a,b: Entered numbers from user.
      Returns:
          Sum of two numbers.
    """
    return a+b


def modulo(a,b):
    """Fetch modulo of entered numbers.
      Args:
          a,b: Entered numbers from user.
      Returns:
          Modulo of two numbers.
    """
    return a%b
    
def main():
    """Promt user to input two numbers and show options to manipulate."""
    
    a = input("Please enter the First Number:\n")
    b = input("Please enter the Second Number:\n")
    a = int(a)
    b= int(b)
    print("Options:")
    print("""
    1.	Add
    2.	Subtract
    3.	Multiply
    4.	Divide
    5.	Power
    6.	Modulo      
          """)
          
    isValidInput=False
    while isValidInput==False:
        option = input("Please select the calculation option:\n")
        option = int(option)
        if option>=1 and option <=6 and type(option)==int:
            isValidInput = True
        else:
            print("Wrong option!")
    
    action(option, a, b)
    
if __name__=='__main__':
    main()
