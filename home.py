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



#TC-8 добавление комментария
#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 100);")

#3. Нажмите на кнопку "READ MORE"
driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-1-0 a[data-product_id]").click()

#4. Нажмите на вкладку "REVIEWS"
driver.find_element_by_css_selector("div#content li.reviews_tab>a").click()

#5. Поставьте 5 звёзд
driver.find_element_by_css_selector("div#respond>form>p.comment-form-rating>p.stars a.star-5").click()

#6. Заполните поле "Review" сообщением: "Nice book!"
driver.find_element_by_id("comment").send_keys("Nice book!")

#7. Заполните поле "Name"
driver.find_element_by_id("author").send_keys("Jane Doe")

#8. Заполните "Email"
driver.find_element_by_id("email").send_keys("janedoe@company.com")

#9. Нажмите на кнопку "SUBMIT"
driver.find_element_by_id("submit").click()



#ending the test
sleep(4)
driver.quit()