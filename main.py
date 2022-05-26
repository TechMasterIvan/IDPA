from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import time

#Author: Ivan Gotovcevic
#Last Modification: 25.05.2022
#Name: Webscraper Python

starttime = time.time()
#Diese Funktion holt den Preis und den Namen des Produkts von der Webseite
def getBauhausPrice(url):
        request_page = urlopen(url)
        page_html = request_page.read()
        request_page.close()
        #Wan
        html_soup = BeautifulSoup(page_html, 'html.parser')

        price_box = html_soup.find('span', class_="price")
        name_box = html_soup.find('div', class_="col-sm-12 col-lg-7")
        name = name_box.find('h1', class_="")

        filename = 'bauhausprice.csv'
        f = open(filename, 'a')

        today = datetime.today()
        print(name.text.strip() + "(Bauhaus) Price: CHF " + price_box.text.strip())
        #Schreibt in das CSV File rein
        f.write("\n" + str(name.text.strip()) + ', CHF ' + str(price_box.text.strip()) + ', Date: ' + str(today))
        f.close

#Diese Funktion holt den Preis und den Namen des Produkts von der Webseite
def getHornbachPrice(url):
        request_page = urlopen(url)
        page_html = request_page.read()
        request_page.close()

        html_soup = BeautifulSoup(page_html, 'html.parser')

        price_box = html_soup.find('span', class_="ad-ui-Component-price_main-0-2-151 ad-ui-Component-lg-0-2-152")
        name = html_soup.find('h1', class_="ad-ui-Component-headline-0-2-128 ad-ui-Component-label_size_lg-0-2-134 ad-ui-headline-0-2-127")

        filename = 'hornbachprice.csv'
        f = open(filename, 'a')

        today = datetime.today()
        print(name.text.strip() + "(Hornbach) Price: CHF " + price_box.text.strip().split()[0])
        #Schreibt in das CSV File rein
        f.write("\n" + str(name.text.strip()) + ', CHF ' + str(price_box.text.strip().split()[0]) + ', Date: ' + str(today))
        f.close

if __name__ == '__main__':
 #Die While True Schleife wurde verwendet, damit das Programm selbständig immer wieder neustartet und so den aktuellsten Preis abgreift.
 #Momentan ist die Schleife auf 5 Sekunden eingestellt       
 while True:
        today = datetime.today()
        print("Today's date:", today)        
        getBauhausPrice("https://www.bauhaus.ch/de/osb-verlegeplatte-12-mm-14615044")
        getHornbachPrice("https://www.hornbach.ch/shop/OSB3-Verlegeplatte-2050x675x12-mm-E1-ungeschliffen/5195805/artikel.html")
        time.sleep(20.0 - ((time.time() - starttime) % 20.0))
        print("\n")