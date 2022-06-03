from woocommerce import API

def uploadKvartalGroupedWC(data, category_id):

        
        wcapi = API(
        url="https://az-mebel.ru/",
        consumer_key="ck_292e3970d43f0934000f671a2dad593a9c320e43",
        consumer_secret="cs_c8c878c0530c656729d90a94345c892485b80f07",
        timeout=1000000
        )




        wc_attributes = wcapi.get('products/attributes').json()


        for item in data:

            wc_products = wcapi.get('products', params={
                "category" : category_id,
                "search": item['title']
            }).json()
            print(wc_products)
            
            filtered_product = next((prod for prod in wc_products if prod["name"] == item['title']), False)

            product_data = {
                "name": item['title'],
                "type": "grouped",
                'grouped_products': item['variants'],
                "short_description": "",
                "description": item['description'],
                "categories": [{"id": category_id}],
                "images": [],
                # "regular_price": item['price'],
                "attributes": [{
                    "id": 2,
                    "visible": True,
                    "variation": False,
                    "options": ['KVARTAL']
                }]
            }

            for img in item['url']:

                product_data['images'].append({
                "src": img,
                "alt": 'KVARTAL'
            })
            

            # for attr in item['attrs']:

            #     attr_data = {
            #         "visible": True,
            #         "variation": False,
            #     }

            #     filtered = next((item for item in wc_attributes if item["name"] == attr['name']), False)
            #     print(filtered)
            #     if filtered:
            #         attr_data['id'] = filtered['id']
            #         attr_data['options'] = [attr['value']]
            #     else:
            #         attr_data['name'] = attr['name']
            #         attr_data['options'] = [attr['value']]
                    

            #     product_data['attributes'].append(attr_data)
            print(product_data)

            if filtered_product:
                # del product_data['images']
                # del product_data['attributes']
                # del product_data['description']
                response = wcapi.put('products/' + str(filtered_product["id"]), product_data)
                print(response.json())
            else: 
                response = wcapi.post('products', product_data)
                print(response.json())