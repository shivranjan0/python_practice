#Write a script that checks if a given password meets certain criteria (e.g., length, special characters).
password = input("Enter a password:")
def password_check(password):
    if len(password) <8:
        print("password is to short it should be minium 8 charactors")
    elif password.isalpha():
        print("password should contian atleast one number")
    elif password.isnumeric():
        print("password should contain atleast one alphabet")
    else:
        print("password is valid")

password_check(password)
