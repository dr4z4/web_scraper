import bs4, requests      # third party module beautiful soup 

# res = requests.get('https://knihy.heureka.cz/jan-vojacek-umeni-byt-zdrav-jan-vojacek/#')  # např. Amazon nejde - nějaké opatření z jejich strany ???
# res.raise_for_status()

# # soup = bs4.BeautifulSoup(res.text)
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# elems = soup.select('#top-offer-price > p > span.js-top-price') # path to CSS selector
# print(elems)
# print(elems[0].text)
# print(elems[0].text.strip()) # protože kolem můžou být bílé znaky \t\n apod.

def getHeurekaPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#top-offer-price > p > span.js-top-price')
    return elems[0].text.strip()

price = getHeurekaPrice('https://knihy.heureka.cz/jan-vojacek-umeni-byt-zdrav-jan-vojacek/#')
print("The price is " + price)

price2 = getHeurekaPrice('https://hry-pro-pc.heureka.cz/minecraft/#')
print("The price is " + price2)

price3 = getHeurekaPrice('https://vysavace.heureka.cz/silvercrest-sas-7_4-li-b3/#')
print("The price is " + price3)

price4 = getHeurekaPrice('https://vina.heureka.cz/moet-chandon-brut-imperial-0_75-l/#')
print("The price is " + price4)