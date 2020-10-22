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
#Для данного теста потребуется предварительно выйти из системы
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
#Для данного теста потребуется предварительно выйти из системы
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



#TC-4
#Для данного теста потребуется предварительно выйти из системы
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

#5. Добавьте тест, что содержимое старой цены = "₹600.00"

#6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert # используйте assert

#7. Добавьте явное ожидание и нажмите на обложку книги
#• Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)

#8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)





#TC-5
#Для данного теста потребуется предварительно выйти из системы
driver.get("http://practice.automationtesting.in/my-account/customer-logout/")
'''
проверка цены в корзине
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop"
3. Добавьте в корзину книгу "HTML5 WebApp Development"
4. Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
• Используйте для проверки assert
5. Перейдите в корзину
6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
7. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
'''



#TC-6
'''
работа в корзине
Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop"
 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
• Перед добавлением первой книги, проскролльте вниз на 300 пикселей
• После добавления 1-й книги добавьте sleep
4. Перейдите в корзину
5. Удалите первую книгу
• Перед удалением добавьте sleep
6. Нажмите на Undo (отмена удаления)
7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
• Предварительно очистите поле с помощью локатор_поля.clear()
8. Нажмите на кнопку "UPDATE BASKET"
9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
10. Нажмите на кнопку "APPLY COUPON"
• Перед нажатимем добавьте sleep
11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
'''



#TC-7
'''
покупка товара
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
3. Добавьте в корзину книгу "HTML5 WebApp Development"
4. Перейдите в корзину
5. Нажмите "PROCEED TO CHECKOUT"
• Перед нажатием, добавьте явное ожидание
6. Заполните все обязательные поля
• Перед заполнением first name, добавьте явное ожидание
• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
7. Выберите способ оплаты "Check Payments"
• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
8. Нажмите PLACE ORDER
9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
'''


#ending the tests
sleep(3)
driver.quit()