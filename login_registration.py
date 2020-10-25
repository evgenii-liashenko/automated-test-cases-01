#Setting up webdriver and libraries
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
from selenium.webdriver.support.ui import WebDriverWait
driver.implicitly_wait(5)
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
from random import randint



#TC-9 #регистрация аккаунта   !!!  FLAKY TEST  !!!

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Нажмите на вкладку "My Account Menu"
driver.find_element_by_css_selector("li#menu-item-50>a").click()

#3. В разделе "Register", введите email для регистрации
email=f'johndoe{randint(0,10000)}@company.net'
driver.find_element_by_id("reg_email").send_keys(email)
sleep(2)

#4. В разделе "Register", введите пароль для регистрации
password = f'qpqpqpqpqp{randint(0,100)}'
driver.find_element_by_id("reg_password").send_keys(password)

#5. Нажмите на кнопку "Register"
#wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-password-strength"), "Strong"))
reg_btn_selector = ".woocomerce-FormRow.form-row>input.woocommerce-Button.button[name='register']"
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"{reg_btn_selector}")))
driver.find_element_by_css_selector(f"{reg_btn_selector}").click()



#TC-10 #логин в систему
'''Для теста логина потребуется предварительно выйти из системы'''
driver.get("http://practice.automationtesting.in/my-account/customer-logout/")

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Нажмите на вкладку "My Account Menu"
driver.find_element_by_css_selector("li#menu-item-50>a").click()

#3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
driver.find_element_by_id("username").send_keys(f"{email}")

#4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
driver.find_element_by_id("password").send_keys(f"{password}")

#5. Нажмите на кнопку "Login"
driver.find_element_by_css_selector("form.login>p>input[name='login']").click()

#6. Добавьте проверку, что на странице есть элемент "Logout"
#logout_link = driver.find_element_by_css_selector("#page-36 .woocommerce-MyAccount-navigation-link--customer-logout>a")
logout_link = driver.find_element_by_link_text("Logout")
assert logout_link.get_attribute("href") == "http://practice.automationtesting.in/my-account/customer-logout/"



print(f"{email} {password}")

#ending the tests
sleep(3)
driver.quit()