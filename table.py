A = input("Enter: ")

if type(int(A))==int :
    print("it is number")
elif type(A)==str:
    if ord(A)>=65 and ord(A)<=90:
        print("you enter upper case letter")
    elif ord(A)>=97 and ord(A)<=122:
        print("you enter lower case")
    elif ord(A)>=1 and ord(A)<=64:
        print("It is a symbol")
    elif ord(A)>=91 and ord(A)<=96:
        print("It is a symbol")
    elif ord(A)>=123 and ord(A)<=126:
        print("It is a symbol")
    else :
        x = int(A)
        if(x == A):
            print("It is a number")
    


    


# if type(b)==str:
#     print("ysef")