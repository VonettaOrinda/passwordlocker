import unittest
from credentials import Credential



class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Instagram", "Von", "@von")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name, "Instagram")
        self.assertEqual(self.new_credential.username, "Von")
        self.assertEqual(self.new_credential.password, "@von")
    
    # credential save
    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)
        
        # multiple credentials
        
    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("test","accountname","username","userp")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list))
        
    def tearDown(self):
        Credential.credentials_list = []
        
        
    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("test","accountname","username","userp")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
        
            
        
    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("test","accountname","username","userp")
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)
        
        # find credential
        
    def test_find_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("test","accountname","username","userp")
        test_credential.save_credential()
        
        found_credential = Credential.find_by_account("accountname")
        
        self.assertEqual(find_by_account.account_name,test_credential.accountname)
        
          
    def test_credential_exist(self):
        self.new_credential.save_credential()
        test_credential = Credential("test","userservice","userp")
        test_credential.save_credential()
        
        credential_exist = Credential.credential_exist("userp")
        self.assertTrue(credential_exist)
        
    def test_display_credentials(self):
        self.assertEqual(Credential.display_credential(),Credential.credentials_list)


if __name__ == '__main__':
    unittest.main()
