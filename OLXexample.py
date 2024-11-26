from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv

URL = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/q-warszawa/'

#def parse_price(price): #zmiana formatu ceny ale nie działa z linkiem
#    return float(price.replace(' ', '').replace('zł', '').replace(',', ''))

db = sqlite3.connect('flats.db')
cursor = db.cursor()

if len(argv) > 1 and    argv[1] == 'setup':
    cursor.execute('''CREATE TABLE offers (name TEXT, price REAL, location TEXT)''')
    quit()

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('div', class_='css-1apmciz'):    #css-l9drzq'):
    adname = offer.find('a', class_='css-qo0cxu').get_text(strip=True)  #css-1s3qyje -po tym jest opis
    price = offer.find('p', class_='css-13afqrm',attrs={"data-testid": "ad-price"}).get_text(strip=True) #format cey jest z spacjami
    #price = parse_price(offer.find('p', class_='css-13afqrm', attrs={"data-testid": "ad-price"}).get_text(strip=True))
    locationdate = offer.find('p', class_='css-1mwdrlh' ,attrs={"data-testid": "location-date"}).get_text(strip=True)  #.get_text(strip=True)  #
    sizeprice = offer.find('span', class_='css-1cd0guq').get_text(strip=True) #.get_text().strip()  #
    #link = offer.find('a')

    cursor.execute('INSERT INTO offers VALUES (?, ?, ?)', (locationdate, price, sizeprice))
    db.commit()
    
db. close()

    #print(offer)
   # print(adname)
    #print(price, locationdate, sizeprice)
    #print(link['href'])
    #break
    #print(locationdate)
    #print(sizeprice)


#   bs = BeautifulSoup(html, 'html.parser')
#   a_tag = bs.find('a', class_='css-qo0cxu')
#     href = a_tag['href'] if a_tag else None
    #description = a_tag.find('h4').get_text(strip=True) if a_tag else None
#    return href, #description

#href = extract_href(html)
#print(f"href: {href}")





