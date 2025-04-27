try:
    age = int(input("Enter your age: "))
    if age<0:
        print("age can not be negative !")
    else: 
        if age %2==0:
            print("your age is even")
        else:
            print("your age is odd")
except ValueError:
    print("Age is not valid please enter a correct age!")