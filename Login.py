''' Login Page'''
"==============================="


import database

''' A function to create and account'''
def CreateAcct():
    print("Please enter your login details")
    print("Email:")
    Email = input()
    print("Password")
    Password = input()
    return Email,Password
    

#print('@' in Email)
''' File to save login info'''
def LoginInfo(Email, Password):
    p1 = database.person(Email, Password)
    p1.cridentiald()
''' Open file that contains login info'''   
def OpenLoginInfo():
    f = open("cridentials.txt",'r')
    thes = f.read()
    return thes

'''Verify if login info are in infoFile'''
def verifieLoginInfo(you,Email, Password):
    if Email and Password in you:
        return True
    else:
        return False
    
        

'''Login page'''
def Login():
    print("Email")
    Email= input()
    print("Password")
    Password = input()
    you = OpenLoginInfo()
    then = verifieLoginInfo(you,Email,Password)
    if then == True:
        print("Welcome to your account")
    else:
        print("Invalid Email or Password")
        print("Enter Q to create another account or enter E to exit")
        Q = input()
        if Q == "C":
            createVerify()
        if Q== "E":
            quit()
        
''' Verify the account just created'''      
def createVerify():
    #Login Page
    Email,Password = CreateAcct()
    print(Email, Password)
    you = OpenLoginInfo()
    then=verifieLoginInfo(you,Email, Password)
   # print(then)
    if then == True:
        print("Already have an account")
    else:
        LoginInfo(Email, Password)
        print("Done!, to login Enter L")
        e = input()
        if e == "L":
            Login()
        
     
def mainLogin():
    print("Enter C to create an account if not click N to Login")
    print("Enter Q to quit")
    c = input()

    if c == 'C':
        createVerify()
       # print("Go create an account")
    elif c == 'N':
        Login()
        print("Enter Q to quit")
        Q = input()
        if Q == "Q":
            quit()

    elif c == "Q":
        quit()
            
mainLogin()