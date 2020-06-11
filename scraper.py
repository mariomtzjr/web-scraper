import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Configuramos webdriver

driver = webdriver.Chrome()

productos = []  # Lista para almacenar nombres de productos
precios = []  # Lista pra almacenar precios
ratings = []  # Lista para almacenar rating del producto

driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

# Obtenemos el contenido de la página a través del driver
content = driver.page_source
soup = BeautifulSoup(content)

productos = [a.find('div', attrs={'class':'_3wU53n'}).get_text() for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'})]
precios = [a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'}).get_text() for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'})]
ratings = [a.find('div', attrs={'class':'hGSR34'}).get_text() for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'})]

# Creamos archivo para almacenar los datos obtenidos
df = pd.DataFrame({'Product Name':productos,'Price':precios,'Rating':ratings})
df.to_csv('productos.csv', index=False, encoding='utf-8')
