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
from selenium.webdriver.support.select import Select



'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'''
#user credentials
email = 'johndoe9029@company.net'
password = 'qpqpqpqpqp56'
'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'''



#TC-1 #отображение страницы товара

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Залогиньтесь
driver.find_element_by_css_selector("#menu-item-50>a").click()
driver.find_element_by_id("username").send_keys(f"{email}")
driver.find_element_by_id("password").send_keys(f"{password}")
driver.find_element_by_css_selector("form.login>p>input[name='login']").click()

#3. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector("#menu-item-40>a").click()

#4. Откройте книгу "HTML 5 Forms"
driver.find_element_by_css_selector("#content>ul.products>li.post-181>a.woocommerce-LoopProduct-link").click()

#5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
book_header = driver.find_element_by_css_selector("div#product-181>div.summary>h1.product_title")
assert book_header.text == "HTML5 Forms"



#TC-2 #количество товаров в категории

'''Для теста потребуется предварительно выйти из системы'''
driver.get("http://practice.automationtesting.in/my-account/customer-logout/")

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Залогиньтесь
driver.find_element_by_css_selector("#menu-item-50>a").click()
driver.find_element_by_id("username").send_keys(f"{email}")
driver.find_element_by_id("password").send_keys(f"{password}")
driver.find_element_by_css_selector("form.login>p>input[name='login']").click()

#3. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector("#menu-item-40>a").click()

#4. Откройте категорию "HTML"
driver.find_element_by_css_selector("#woocommerce_product_categories-2>ul.product-categories>li.cat-item-19>a").click()

#5. Добавьте тест, что отображается три товара
book_elements = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
assert len(book_elements) == 3



#TC-3 #сортировка товаров

'''Для теста потребуется предварительно выйти из системы'''
driver.get("http://practice.automationtesting.in/my-account/customer-logout/")

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Залогиньтесь
driver.find_element_by_css_selector("#menu-item-50>a").click()
driver.find_element_by_id("username").send_keys(f"{email}")
driver.find_element_by_id("password").send_keys(f"{password}")
driver.find_element_by_css_selector("form.login>p>input[name='login']").click()

#3. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector("#menu-item-40>a").click()

#4. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему #• Используйте проверку по value
sorting_dropdown = driver.find_element_by_css_selector("#content>form.woocommerce-ordering>select")
if sorting_dropdown.get_attribute("value") == 'price-desc':
    print(f"[Проверка пройдена] Выбрана сортировка по уменьшению цены")
else:
    print("[ОШИБКА] Выбранный вариант сортировки не соответствует требуемому")

#5. Отсортируйте товары от большего к меньшему • в селекторах используйте класс Select
Select(sorting_dropdown).select_by_visible_text("Sort by price: high to low")

#6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
sorting_dropdown = driver.find_element_by_css_selector("#content>form.woocommerce-ordering>select")

#7. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему #• Используйте проверку по value
assert sorting_dropdown.get_attribute("value") == "price-desc"



#TC-4 отображение, скидка товара

'''Для теста потребуется предварительно выйти из системы'''
driver.get("http://practice.automationtesting.in/my-account/customer-logout/")

#1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

#2. Залогиньтесь
driver.find_element_by_css_selector("#menu-item-50>a").click()
driver.find_element_by_id("username").send_keys(f"{email}")
driver.find_element_by_id("password").send_keys(f"{password}")
driver.find_element_by_css_selector("form.login>p>input[name='login']").click()

#3. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector("#menu-item-40>a").click()

#4. Откройте книгу "Android Quick Start Guide"
driver.find_element_by_css_selector("li.post-169>a>h3").click()

#5. Добавьте тест, что содержимое старой цены = "₹600.00"
old_price = driver.find_element_by_css_selector("p.price>del>.woocommerce-Price-amount")
assert old_price.text == "₹600.00"

#6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert # используйте assert
new_price = driver.find_element_by_css_selector("p.price>ins>.woocommerce-Price-amount")
assert new_price.text == "₹450.00"

#7. Добавьте явное ожидание и нажмите на обложку книги
#• Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
driver.find_element_by_css_selector("div.images [alt='Android Quick Start Guide']").click()
wait.until(EC.visibility_of_element_located((By.ID, "fullResImage")))

#8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.pp_close")))
driver.find_element_by_css_selector("a.pp_close").click()



#TC-5 проверка цены в корзине

#1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")

#2. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector("#menu-item-40>a").click()

#3. Добавьте в корзину книгу "HTML5 WebApp Development"
driver.find_element_by_css_selector("a[data-product_id='182']").click()

#4. Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00" • Используйте для проверки assert
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a.wpmenucart-contents>span.cartcontents"), "1 Item"))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a.wpmenucart-contents>span.amount"), "₹180.00"))
assert driver.find_element_by_css_selector("a.wpmenucart-contents>span.cartcontents").text == "1 Item"
assert driver.find_element_by_css_selector("a.wpmenucart-contents>span.amount").text == "₹180.00"

#5. Перейдите в корзину
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()

#6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td.product-price>span.woocommerce-Price-amount.amount"), "₹180.00"))

#7. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
'''Совпадает с предыдущим'''



#TC-6 работа в корзине
#Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()

#1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")

#2. Нажмите на вкладку "Shop"
driver.find_element_by_css_selector("#menu-item-40>a").click()

#3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
#driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[data-product_id='182']").click()
#sleep(1)
#wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a.wpmenucart-contents>span.cartcontents"), "1 Item"))
driver.find_element_by_css_selector("[data-product_id='180']").click()

#4. Перейдите в корзину
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()

#5. Удалите первую книгу
driver.find_element_by_css_selector(".remove[data-product_id='182']").click()

#6. Нажмите на Undo (отмена удаления)
driver.find_element_by_css_selector(".woocommerce-message>a").click()

#7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
#• Предварительно очистите поле с помощью локатор_поля.clear()
driver.find_element_by_css_selector(".input-text.qty.text").clear()
driver.find_element_by_css_selector(".input-text.qty.text").send_keys("3")

#8. Нажмите на кнопку "UPDATE BASKET"
driver.find_element_by_css_selector("input[name='update_cart']").click()

#9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
assert driver.find_element_by_css_selector(".input-text.qty.text").get_attribute("value") == '3'

#10. Нажмите на кнопку "APPLY COUPON" #• Перед нажатимем добавьте sleep
#wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='apply_coupon']")))
sleep(2)
driver.find_element_by_css_selector("input[name='apply_coupon']").click()

#11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
assert driver.find_element_by_css_selector("ul.woocommerce-error>li").text == "Please enter a coupon code."



#TC-7 #покупка товара

#1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")

#2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
driver.find_element_by_css_selector("#menu-item-40>a").click()
driver.execute_script("window.scrollBy(0, 300);")

#3. Добавьте в корзину книгу "HTML5 WebApp Development"
driver.find_element_by_css_selector("[data-product_id='182']").click()

#4. Перейдите в корзину
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a.wpmenucart-contents>span.cartcontents"), "1 Item"))
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()

#5. Нажмите "PROCEED TO CHECKOUT" #• Перед нажатием, добавьте явное ожидание
driver.find_element_by_css_selector(".checkout-button.button").click()

#6. Заполните все обязательные поля #• Перед заполнением first name, добавьте явное ожидание
#• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
#• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
driver.find_element_by_id("billing_first_name").send_keys("John")
driver.find_element_by_id("billing_last_name").send_keys("Doe")
driver.find_element_by_id("billing_email").send_keys(f"{email}")
driver.find_element_by_id("billing_phone").send_keys(f"+358449363456")
driver.find_element_by_id("s2id_billing_country").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Finland")
driver.find_element_by_css_selector("#select2-results-1>li>div").click()
driver.find_element_by_id("billing_address_1").send_keys("Karankokatu 4")
driver.find_element_by_id("billing_city").send_keys("Lappeenranta")
driver.find_element_by_id("billing_postcode").send_keys("53850")

#7. Выберите способ оплаты "Check Payments" #• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
sleep(2)
driver.find_element_by_id("payment_method_cheque").click()

#8. Нажмите PLACE ORDER
driver.find_element_by_id("place_order").click()

#9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

#10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>:nth-child(3)>td"), "Check Payments"))



#ending the tests
sleep(2)
driver.quit()