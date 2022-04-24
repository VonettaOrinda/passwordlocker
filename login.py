



def register():
    print("REGISTER")
    print("-"*30)
    username = input("enter username:  ")
    userpassword = input("enter password:  ")
    confirm_pass=input("confirm password:   ")
    
    #  validation
    if userpassword == confirm_pass:
        user = User(username,userpassword)
        user.save_user
        print(f"Welcome {username}!you are now registered")
        print("Lets Login")
        
    else:
       repeat= input("Something has gone wrong. Try again. y/n")
       if repeat == "y":
           print(register())
       else:
           print(exit())

 #    login   
def Login():
     print("LOGIN")
     print("-"*30)
     username = input("Enter username: ")
     userpassword = input("enter login password:  ")
     
     user = User(username,userpassword)
     if user is None:
         print("please enter a valid name and password")
     else:
         user.login
         print(f"Welcome {username}!you are logged in")
         print("\n")
         print("-"*30)
         print('What would you like to do?')
         while True:
            print("Use this short codes : ")
            print("cc-create a new password")
            print("dc-display passwords")
            print("fc-find a specific credential")
            print("dd-delete credential")
            print("ex -exit" )
            print("-"*50)
            user_input = input("answer: ")
            if user_input == "cc":
                            choose= input("would you like a custom password or generated password?: c = custom and g = generated password: c/g?")
                            if  choose == "c":
                                    
                                    print("*"*60)
                                    print("Account name i.e Facebook")
                                    accountName= input()
                                    
                            
                                    print("User Name")
                                    user_name= input()
                            
                                                        
                                    print("password")
                                    user_password= input()

                                    run.save_credentials(run.create_credentials(accountName,user_name,user_password))
                                    print("\n")
                                    print(f"New {accountName} credentials created and saved:")
                                    print(f"Name:{user_name}")
                                    print(f"password:{user_password}")
                                    print("\n")
                            else:
                                print("*"*60)
                                print("Account name i.e Facebook")
                                accountName= input()
                                    
                            
                                print("User Name")
                                user_name= input()                  
                            
                                user_password=generate_password()
                                print("*"*60)
                                run.save_credentials(run.create_credentials(accountName,user_name,user_password))
                                print("\n")
                                print(f"New {accountName} credentials created and saved:")
                                print(f"Name:{user_name}")
                                print(f"Password:{user_password}")
                                print("\n")
                                print("*"*60)
            elif user_input == "dc":
                if run.display_credentials():
                    print("Here is a list of your saved passwords")
                    print("\n")
                    
                    for credential in run.display_credentials():
                        print(f"{credential.username} {credential.account_name} ......{credential.password_}")
                    print('\n')
                else:
                    print('\n')
                    print("Sorry! You do not have any saved passwords")
                    print('\n')
                    
            elif user_input == "dd":
                print("Enter the account you want to delete:" )
                deleteAccount = input()
                print(f"{deleteAccount} account successfuly deleted")
                print('\n')
                print("*"*60)
                
            elif user_input == "ex":
                            print("Bye for now.......")
                            break
            else:
                            print("I really didn't get that. Please use the short codes") 