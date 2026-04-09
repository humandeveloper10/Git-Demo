import BasePage

class TestReferencePage(BasePage.BasePage):
    def __init__(self):
            super().__init__()


    def Test_invalidemailformat(self):
        email = self.driver.find_element_by_id("email-input").clear()
        password = self.driver.find_element_by_id("password-input").clear()
        email = self.driver.find_element_by_id("email-input").send_keys("logindcodility")
        password = self.driver.find_element_by_id("password-input").send_keys("password")
        button = self.driver.find_element_by_id("login-button").click()
        message = self.driver.find_element_by_id("messages")
        assert "Enter a valid email" in message.text
                
    def Test_validlogin(self):
        email = self.driver.find_element_by_id("email-input").send_keys("login@codility.com")
        password = self.driver.find_element_by_id("password-input").send_keys("password")
        button = self.driver.find_element_by_id("login-button").click()
        message = self.driver.find_element_by_id("container")
        assert "Welcome to Codility" in message.text  
    
    def Test_invalidlogin(self):
        email = self.driver.find_element_by_id("email-input").send_keys("unknown@codility.com")
        password = self.driver.find_element_by_id("password-input").send_keys("password")
        button = self.driver.find_element_by_id("login-button").click()
        message = self.driver.find_element_by_id("messages")
        assert "You shall not pass! Arr!" in  message.text

    def Test_emptylogin(self):
        email = self.driver.find_element_by_id("email-input").send_keys("")
        password = self.driver.find_element_by_id("password-input").send_keys("password")
        button = self.driver.find_element_by_id("login-button").click()
        message = self.driver.find_element_by_id("messages")
        assert "Email is required" in message.text

if __name__ == "__main__":
    test = TestReferencePage()

    test.Test_invalidemailformat()
    test.Test_validlogin()
    test.Test_invalidlogin()
    test.Test_emptylogin()

    print("All tests executed")


print("hello world from user X")
print("Hello from user Y")
#user x can continue from here