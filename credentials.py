class credential:
    """
    class that generates new instances of credentials.
    """
    credentials_list=[] #Empty credential list
    
    def __init__(self,account_details,username,password):
        
        self.account_details= account_details
        self.username= username
        self.password= password
        
    credentials_list=[]
    
    def save_credentials(self):
      """
      Function to save users account credentials
      """
       # self.new_credential.save_credential()
      credential.credentials_list.append(self)
      
    def del_credentials(self):
        """
        Function to delete a users account credentials
        """
        
        credential.credential_list.remove(self)
        
        
    @classmethod
    def find_by_account(cls,account_details):
        
        for credential in cls.credentials_list: 
            if credential.account_details==account_details:
                return credential
            
    @classmethod
    def account_exists(cls,account_details):
        for credential in cls.credentials_list:
            if credential.account_details== account_details:
                return True
        return False
    
    # display Credential
    @classmethod
    def display_credential(cls):
        return cls.credentials_list
        
        
    