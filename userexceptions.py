class Error(Exception):
    """Base class for the other exceptions"""
    pass

class ValueTooSamllError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input is too large"""
    pass

number=10

while True:
    try:
        i_num=int(input("Enter a number: "))
        if i_num<number:
            raise ValueTooSamllError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueTooSamllError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! you guessed correctly.")







