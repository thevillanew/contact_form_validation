from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# initializing webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
url = "http://automationpractice.com/index.php?controller=contact"
driver.get(url)
image_path = "D:\\gbh project\\test_data\\thor.jpg"


def set_email(email):
    email_field = driver.find_element("id", "email")
    email_field.click()
    email_field.clear()
    email_field.send_keys(email)


def set_order_field(order_id):
    order_field = driver.find_element("id", "id_order")
    order_field.click()
    order_field.clear()
    order_field.send_keys(order_id)


def upload_file(file_path):
    file = driver.find_element("xpath", "//input[@id='fileUpload']")
    file.send_keys(file_path)


def set_message(message):
    message_field = driver.find_element("id", "message")
    message_field.click()
    message_field.clear()
    message_field.send_keys(message)


def submit_form():
    submit_button = driver.find_element("xpath", "//button[@id='submitMessage']/span")
    submit_button.click()


def get_warning_message():
    warning_message = driver.find_element("xpath", "//div[@class='alert alert-danger']/ol/li")
    return warning_message.text



