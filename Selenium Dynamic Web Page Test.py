# Based on Pluralsight course "Scraping Dynamic Web Pages with Python and Selenium"
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

fireFoxOptions = Options()
fireFoxOptions.add_argument("--kiosk")

b = webdriver.Firefox(options=fireFoxOptions)
b.get("https://www.premierleague.com/players")

element = WebDriverWait(b, 10).until(
    EC.element_to_be_clickable((By.ID, "search-input"))
    )

search_ele = b.find_element_by_id("search-input")
search_ele.send_keys("Wayne Rooney")
search_ele.send_keys(Keys.RETURN)

# clicking on wayne rooney
b.implicitly_wait(2)
click_wayne = b.find_element_by_xpath("//img[@data-player='p13017']").click()

# stats button element
time.sleep(2)
wayne_stats = b.find_element_by_xpath("//a[@href='stats']").click()

page_source_stats = b.page_source
soup = BeautifulSoup(page_source_stats, features="html.parser")
stat_finder = soup.find_all("span", class_="allStatContainer")

print(10*"-" + "Wayne Rooney Stats" + 10*"-" + "\n")
for stat in stat_finder:
    print(stat["data-stat"] + " - " + stat.string.rstrip())

b.quit()
