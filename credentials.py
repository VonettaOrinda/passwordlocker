class credential:
    """
    class that generates new instances of credentials.
    """
    credential_list=[] #Empty credential list
    
    def__init__(self,account_details,username,password):
        
        self.account_details= account_details
        self.username= username
        self.password= password
        
    credential_list=[]
    
    def save_credentials(self):
      """
      Function to save users account credentials
      """
      
      credential.credentials_list.append(self)
      