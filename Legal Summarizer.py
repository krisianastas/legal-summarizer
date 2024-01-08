import lxml
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from time import sleep

names = []
full_text = ""
numri = input("Vendos numrin e ligjit: ")
data = input("Vendos daten e ligjit: ")
datat = []
datat = data.split(".")
url = "http://qbz.gov.al/eli/ligj/" + datat[2] + "/" + datat[1] + "/" + datat[0] + "/" + numri

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get(url)
sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')
element = soup.find_all("div", {"class": "textLayer"})

for ele in element:
    full_text += ele.text + " "

driver.quit()

api_key = "YOUR API KEY"
url_api = 'https://portal.ayfie.com/api/summarize'
myobj = {
  "language": "auto",
  "text": full_text,
  "min_length": 5,
  "max_length": 100
}

x = requests.post(url_api, json = myobj, headers={"X-API-KEY":api_key})
x.raise_for_status()
response = json.loads(x.text)
final = response["result"]["summary_in_provided_language"]
print(final)