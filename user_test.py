
import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Von","ilkfjdow")
        
    def test_init(self):
        self.assertEqual(self.new_user.username,"Von")
        self.assertEqual(self.new_user.userpassword,"ilkfjdow")
    
if __name__ == '__main__':
    unittest.main()   