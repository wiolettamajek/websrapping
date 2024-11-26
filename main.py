from bs4 import BeautifulSoup
from requests import get
#sellenium webdriver / json

URL = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?viewType=listing'

page = get(URL, headers={"User-Agent": "Mozilla/5.0"})
bs = BeautifulSoup(page.content, 'html.parser')

print(bs)


def get_href(html):
    soup = BeautifulSoup(html, 'html.parser')
    a_tag = soup.find('a', class_='css-16vl3c1 e17g0c820')
    href = a_tag['href'] #if    else None
    return href

# Example usage

href = get_href(bs)
print(href)  # Output: /pl/oferta/bezposrednio-2-pokoje-kamienica-stare-bielany-ID4tk3j



#print(page.content)
for offer in bs.find_all('div', class_='css-13gthep eeungyz2'):   #czy powinno być:class_='listing-item'
    flat = offer.find('dl', class_= 'css-12dsp7a e1clni9t1') #'css-1ix8q56 e1clni9t1')
    #print(flat)
    dl = flat
    data = {}
    for dt, dd in zip(dl.find_all('dt'), dl.find_all('dd')):
        key = dt.get_text(strip=True)
        value = dd.get_text(strip=True).replace('\xa0', '')
        data[key] = value

    #print(data)
    #flat2 = flat.get_text().strip()
    #print(offer)

    #break

    #class ="css-16vl3c1 e17g0c820" > … < / a >
    #print("tu powinno sie cos prinotwac : ",offer)
 #