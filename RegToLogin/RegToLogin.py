import getpass
import json
import os

reg_dict = {}


class LoginAndReg:
    def __init__(self):
        self.name = input("Enter your name : ")
        self.email_id = input("Enter the email id : ")
        print("The password you will enter will remain invisible !!")
        self.password = getpass.getpass()
        if os.path.exists("RegistrationDetails.txt"):
            reg_file = open("RegistrationDetails.txt", "r")
            reg_details = reg_file.read()
            global reg_dict
            reg_dict = json.loads(reg_details)

    def register(self):
        reg_dict[self.email_id] = self.password, self.name
        reg_details = json.dumps(reg_dict)
        print(reg_dict)
        if os.path.exists("RegistrationDetails.txt"):
            reg_file = open("RegistrationDetails.txt", "w")
            reg_file.write(reg_details)
        else:
            reg_file = open("RegistrationDetails.txt", "x")
            reg_file.write(reg_details)

    @classmethod
    def login(cls):
        if os.path.exists("RegistrationDetails.txt"):
            reg_file = open("RegistrationDetails.txt", "r")
            reg_details = reg_file.read()
            global reg_dict
            reg_dict = json.loads(reg_details)
        log_email = input("Enter your email :")
        log_pass = getpass.getpass()
        try:
            if log_pass == reg_dict[log_email][0]:
                print(reg_dict[log_email][1] +
                      " You have logged in successfully !!!")
            else:
                print("Login failed !")
        except:
            print("Login failed !")


if __name__ == '__main__':
    try:
        while True:
            input_reg = input(
                "Enter 'r' to register or 'l' to login or 'q' to quit: ")
            if input_reg.lower() == 'r':
                user = LoginAndReg()
                user.register()
            elif input_reg.lower() == 'q':
                exit()
            elif input_reg.lower() == 'l':
                LoginAndReg.login()
            else:
                print("Invalid input !")
    except Exception as e:
        print("problem during login or registration !!!")
