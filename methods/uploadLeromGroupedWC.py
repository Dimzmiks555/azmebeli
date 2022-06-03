from woocommerce import API

def uploadLeromGroupedWC(data, category_id, sub_product_id):

        
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
                'grouped_products': [],
                "short_description": "",
                "description": item['description'],
                "categories": [{"id": category_id}],
                "images": [],
                "regular_price": item['price'],
                "attributes": [{
                    "id": 2,
                    "visible": True,
                    "variation": False,
                    "options": ['LEROM']
                }]
            }

            for img in item['images']:
                product_data['images'].append({
                "src": img,
                "alt": 'GREEN3'
            })
            

            for attr in item['attrs']:

                attr_data = {
                    "visible": True,
                    "variation": False,
                }

                filtered = next((item for item in wc_attributes if item["name"] == attr['name']), False)
                print(filtered)
                if filtered:
                    attr_data['id'] = filtered['id']
                    attr_data['options'] = [attr['value']]
                else:
                    attr_data['name'] = attr['name']
                    attr_data['options'] = [attr['value']]
                    

                product_data['attributes'].append(attr_data)
            print(product_data)

            for sub_product in item['sub_products']:

                sub_product_data = {
                    "name": sub_product['title'],
                    "type": "simple",
                    "short_description": "",
                    "description": '',
                    "categories": [{"id": sub_product_id}],
                    "images": [{"src": sub_product['img'],"alt": 'LEROM'}],
                    "regular_price": sub_product['price'],
                    "attributes": [{
                        "id": 2,
                        "visible": True,
                        "variation": False,
                        "options": ['LEROM']
                    }]
                }

                for sub_attr in sub_product['attrs']:

                    sub_attr_data = {
                        "visible": True,
                        "variation": False,
                    }

                    sub_filtered = next((item for item in wc_attributes if item["name"] == sub_attr['name']), False)
                    print(sub_filtered)
                    if sub_filtered:
                        sub_attr_data['id'] = sub_filtered['id']
                        sub_attr_data['options'] = [sub_attr['value']]
                    else:
                        sub_attr_data['name'] = sub_attr['name']
                        sub_attr_data['options'] = [sub_attr['value']]
                        

                    sub_product_data['attributes'].append(sub_attr_data)


                wc_sub_products = wcapi.get('products', params={
                    "search": sub_product['title']
                }).json()
                print(wc_sub_products)
                print(sub_product_data)
                
                filtered_sub_product = next((prod for prod in wc_sub_products if prod["name"] == sub_product['title']), False)

                if filtered_sub_product:
                    print('update_sub_product')
                    response = wcapi.put('products/' + str(filtered_sub_product["id"]), sub_product_data)
                    product_data['grouped_products'].append( filtered_sub_product["id"])
                    print(response)
                else: 
                    print('new_sub_product')
                    response = wcapi.post('products', sub_product_data)
                    print(response.json())
                    product_data['grouped_products'].append( response.json()["id"])



            if filtered_product:
                response = wcapi.put('products/' + str(filtered_product["id"]), product_data)
                print(response)
            else: 
                # del product_data['images']
                # del product_data['attributes']
                # del product_data['description']
                response = wcapi.post('products', product_data)
                print(response)