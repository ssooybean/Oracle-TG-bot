# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import urllib.request


from PDFCreators.natalPDF import create_PDF

driver = webdriver.Chrome()

driver.get("https://astro-online.ru/natal.html")
driver.implicitly_wait(0.5)
day = driver.find_element(by=By.NAME, value="dayz")
day_select = Select(day)
day_select.select_by_value("02")

name = driver.find_element(by=By.NAME, value="u_namez")
name.send_keys("Мария")

month = driver.find_element(by=By.NAME, value="monthz")
month_select = Select(month)
month_select.select_by_value("06")

year = driver.find_element(by=By.NAME, value="yearz")
year_select = Select(year)
year_select.select_by_value("2008")

hour = driver.find_element(by=By.NAME, value="hourz")
hour_select = Select(hour)
hour_select.select_by_value("15")

minut = driver.find_element(by=By.NAME, value="minutz")
minut_select = Select(minut)
minut_select.select_by_value("00")

city = driver.find_element(by=By.NAME, value="city")
city_select = Select(city)
city_select.select_by_value("10")

submit_button = driver.find_element(by=By.NAME, value="zerocool")
submit_button.click()

driver.implicitly_wait(0.5)

# Натальная карта
natalmap = driver.find_element(by=By.ID, value="current_img")

# Таблица под натальной картой
table = driver.find_element(by=By.CLASS_NAME, value="desk_natal_table")
table.screenshot("C:\\Users\\user\\umk\\table.png")

# Текст Планеты в знаках
planets = driver.find_element(by=By.ID, value="pln_in_sign")

create_PDF(planets.text, natalmap, table)
# Сохраняем полученную натальную карту на диск
src = natalmap.get_attribute("src")
urllib.request.urlretrieve(src, "C:\\Users\\user\\umk\\map.png")
