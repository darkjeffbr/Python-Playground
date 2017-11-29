def separator(width=40):
    print("".center(width, '#'))    
try:
    print("Inside try")
except Exception as e:
    print(e)
else:
    print("No exception raised")

separator()

try:
    print("An Exception will be raised")
    raise ValueError("A custom exception is being raised")
except Exception as e:
    print(e)
else:
    print("No exception raised")

separator()

try:
    print("This is a try... and next comes the finally block")
except:
    print('It will not be executed')
finally:
    print('... Finally we are here')

separator()

class Error(Exception):
    """Base class for other exceptions"""
    pass

class InputTooSmallError(Error):
    """Raised when the entered alphabet is smaller than the actual one"""
    pass

class InputTooLargeError(Error):
    """Raised when the entered alphabet is larger than the actual one"""
    pass

# our main program
# user guesses an alphabet until he/she gets it right

# you need to guess this alphabet
alphabet = 'm'

while True:
    try:
        apb = input("Enter an alphabet: ")
        if apb < alphabet:
            raise InputTooSmallError
        elif apb > alphabet:
            raise InputTooLargeError
        break
    except InputTooSmallError:
        print('The entered alphabet is too small, try again!')
        print('')
    except InputTooLargeError:
        print('The entered alphabet is too large, try again!')
        print('')

print('Congratulations! You guessed it correctly')