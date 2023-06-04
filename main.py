from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from warnings import filterwarnings
import time
from bs4 import BeautifulSoup

time.sleep(5)

filterwarnings("ignore")

driver = webdriver.Chrome()
driver.set_window_size(1250, 740)
driver.get(
    "https://www.trendyol.com/jakarli/unisex-zumrut-yesili-bisiklet-yaka-pamuk-oversize-boyfriend-t-shirt-p-284940903")

time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# İlgili <div> etiketini bul
div_tag = soup.find("div", {"style": "position: relative;"})

# <div> etiketi altındaki <img> etiketini bul
img_tag = div_tag.find("img")

# Resim bağlantısını (URL) al
img_url = img_tag["src"]

# Çıktıyı yazdır
print(img_url)

wait = WebDriverWait(driver, 5)

div_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-slide']"))
)
print(div_elements)
for div_element in div_elements:
    action = ActionChains(driver)
    action.move_to_element(div_element).click().perform()
    wait = WebDriverWait(driver, 5)
    img_element = div_element.find_element(By.TAG_NAME, "img")
    img_src = img_element.get_attribute("src")
    print("Görsel Linki:", img_src)

driver.quit()