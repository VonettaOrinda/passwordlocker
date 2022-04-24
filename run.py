#!usr/bin/env python3
from credentials import Credential
import login

#create credential

def create_credentials(user_name,accountDetails,user_password):
        new_credential = Credential(user_name,accountDetails,user_password)
        return new_credential

# save credential
def save_credentials(credential):
        credential.save_credential()
        
# delete credential
def del_credential(credential):
        credential.delete_credential()
        
def find_credential(account_details):
        return Credential.find_by_account(account_details)

def check_existing_credentials(account_name):
        return Credential.credential_exist(account_name)

def  display_credentials():
        return Credential.display_credential()

# main function
def main():
        print("Hi,welcome to our password generator app,")
        ans=input("would you like to generate a password? y for YES or n for NO:  ")
        if ans == "y":
                status = input("Already registered?  y/n?")
                if status == "n":
                        login.register()
                        login.Login()
                else:
                        login.Login()
                       
                 
if __name__ == '__main__':

     main()   