from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# WebDriver ayarlarını yapın
chrome_options = Options()
chrome_options.add_argument("--headless")  # Arka planda çalıştırmak için bu seçeneği ekleyebilirsiniz
chrome_driver_path = "path/to/chromedriver"  # Kromedriver'ın yolunu kendiniz belirtin
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
driver.set_window_size(1250, 740)

# Web sayfasını açın
driver.get("https://www.trendyol.com/jakarli/unisex-zumrut-yesili-bisiklet-yaka-pamuk-oversize-boyfriend-t-shirt-p-284940903")

# Sayfanın yüklenmesini bekleyin
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pr-new-br")))

# Sayfa kaynağını alın
html = driver.page_source

# BeautifulSoup nesnesi oluşturun
soup = BeautifulSoup(html, "html.parser")

# Veriyi çekin
urun_isim = soup.find("h1", class_="pr-new-br", attrs={"data-drroot": "h1"})
urun_isim_kodsuz = urun_isim.find("span")
veri = urun_isim_kodsuz.get_text(strip=True)
print(veri)

# WebDriver'ı kapatın
driver.quit()
