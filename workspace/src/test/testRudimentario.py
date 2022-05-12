from selenium.webdriver.common.keys import Keys
from selenium import webdriver


driver = webdriver.Chrome("/Users/pablocalvano/Documents/Cursos Automation Udemy/CURSO AUTOMATION PYTHON "
                          "MERVIN/CursoUdemySeleniumTestingcPython/workspace/Scripts/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()