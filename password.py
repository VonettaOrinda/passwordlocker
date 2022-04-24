import string
import random



def generate_Password (stringLength=8) :
        
        """Generate a random password string of letters and digits and special characters"""
        
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
 
    
    
    
    
    
    