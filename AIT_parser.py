import requests
from bs4 import BeautifulSoup
import re
import json

URL = 'http://testing-ground.scraping.pro/blocks'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

data = []
for result in soup.find_all('div', class_=re.compile('prod')):
# result = soup.find('div', class_=re.compile('prod'))
    item={}

    item["name"] = result.div.text
    print("name: " + item["name"])

    item["description"] = result.span.text
    item["description"] = item["description"].split(',')[1::]
    print("description: " + ', '.join(map(str, item["description"])))


    item["best_price"] = result.find_all('span')

    a_str = "is_best_price: "
    a_bool = True
    b_bool = False

    if item["best_price"][1].has_attr("class"):
        str_best_price = a_str + str(a_bool)
        print (str_best_price)
    else:
        str_best_price = a_str + str(b_bool)
        print (str_best_price)


    item["price"] = result.find_all('span')
    print("price: " + item["price"][1].text)
    


    for i in result.find_all('span'):
        if soup.find('div', class_='disc'):
            print("hello")
        else:
            print("NONONO")


    # disc = result.find_all('span')
    #
    # discount = result.disc[1].div.text
    # print("discount is here")

    print()

    data.append(item)
    # print(data)

    # with open("textbooks.json", "w") as writeJSON:
    #     json.dump(item, writeJSON, ensure_ascii=False)










# for elem in elems:
#     name = elem.find('div', class_='name')
#     # description = elem.find('div', class_='company')
#     price = elem.find('span', class_='best')
#     if None in (name, price):
#         continue
#     print(name.text.strip())
#     # print(descriptoin.text.strip())
#     print(price.text.strip())
#     print()
