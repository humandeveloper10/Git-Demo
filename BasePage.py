from selenium import webdriver
class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/selenium_login_page/9a3e1f6c3c/index.html")