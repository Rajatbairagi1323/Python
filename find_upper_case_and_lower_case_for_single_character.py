# Program to find upper case, lower case, symbol for single character value with the help of ASCII table ? 

value=input("Enter: ")   # value is a variable 
if type(int(value))==int :       # == compare
    print("It is number")
elif type(value)==str:
    if ord(value)>=65 and ord(value)<=90:     #The ord() function returns the number representing the unicode code of a specified character.
        print("you enter upper case letter")
    elif ord(value)>=97 and ord(value)<=122:
        print("you enter lower case")
    elif ord(value)>=1 and ord(value)<=64:
        print("It is a symbol")
    elif ord(value)>=91 and ord(value)<=96:
        print("It is a symbol")
    elif ord(value)>=123 and ord(value)<=126:
        print("It is a symbol")
    else :
        x = int(value)
        if(x == value):
            print("It is a number")
