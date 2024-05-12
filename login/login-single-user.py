import datetime
import time

sole_user = 'Steven'
sole_pass = 4242
curr = time.time()
curr_time_interp = time.ctime(curr)

def main():
    login = input('Please enter your first name:\n')
    #registered user
    if(login == 'Steven'):
        password()
    else:
        print("You are not a registered user")
def password():
    user_int_one = int(input("Please enter your password.\n"))
    if(user_int_one == ""):
        print("what are you doing with your life...")
    if(user_int_one == sole_pass):
        print("Welcome " + sole_user + "!\nThank you for logging in. Current date and time:\n" + curr_time_interp)
    if(user_int_one != sole_pass):
        print('Wrong password Mr. ' + sole_user + "\nPlease try again.")
        password()


if __name__ == "__main__":
    main()