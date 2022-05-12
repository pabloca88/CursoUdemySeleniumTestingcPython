# IMPORT LIBS
import time

from selenium import webdriver
import time

# INIZIALIZO EL DRIVER
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("//Users/pablocalvano/Documents/Cursos Automation Udemy/CURSO AUTOMATION PYTHON "
                          "MERVIN/CursoUdemySeleniumTestingcPython/workspace/environment/Scripts/chromedriver")

# VOY HOST DE LA APLICACION
driver.get("http://www.python.org")

# SE VERIFICA AL TITULO DE LA APLICACION
assert "Python" in driver.title

time.sleep(10)

# ALMACENO EN UNA VARIABLE EL OBJETO CON EL QUE VOY A INTERACTUAR
elem = driver.find_element_by_id("id-search-field")

elem.clear()

elem.send_keys("pycon")

elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

driver.close()
