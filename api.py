from time import sleep
from attr import attributes
import requests
from woocommerce import API

wcapi = API(
  url="https://az-mebel.ru/",
  consumer_key="ck_292e3970d43f0934000f671a2dad593a9c320e43",
  consumer_secret="cs_c8c878c0530c656729d90a94345c892485b80f07",
  timeout=50
)

r = requests.post(url='https://www.triya.ru/rest/catalog', data = {
    "remoteAddress":"185.58.153.141",
    "token": None,
    "code":"divany",
    "page":1,
    "order":"default",
    "params":{},
    "promo":True
    })

    # ck_292e3970d43f0934000f671a2dad593a9c320e43
    # cs_c8c878c0530c656729d90a94345c892485b80f07


wc_attributes = wcapi.get('products/attributes') 

# print(wc_attributes.json())


for item in r.json()['items']:

  
    link = item['link'].split('/')

    post_data = {
      "catalog": link[2],
      "code": link[3],
      "remoteAddress":"185.58.153.141",
      "token": None,
      "id": item['id']
    }


    r_nest = requests.post(url='https://www.triya.ru/rest/catalog/product', data = post_data )


    product = r_nest.json()


    product_data = {
      "name": product['product']['name'],
      "type": "simple",
      "short_description": "",
      "description": "",
      "categories": [
        {
          "id": 104
        }
      ],
      "images": [],
      "regular_price": str(product['product']['price']['price']),
      "attributes": [
        
      ]
    }

    
    # # print(item )
    # # print(item['name'])
    # # print(item['price'])
    # # print(item['pictures'])
    # # print(item['groupedProps'])
    # # print(item['localProps'])

    for img in product['refs']['refs']:

      for img_link in img['pictures']:

        product_data["images"].append({
            "src": "https://www.triya.ru/upload/" + img_link,
            "alt": img_link
        })
    
    colors = []

    # for attr in product['refs']['options']['options']:

    #   colors.append(attr['label']['text'])

    # product_data["attributes"].append({
    #     "id": 1,
    #     "visible": True,
    #     "variation": False,
    #     "options": [
    #       '|'.join(str(x) for x in colors)
    #     ]
    #   })
    # print(product_data)
    
    response = wcapi.post('products', product_data).json()
    print(response)
    