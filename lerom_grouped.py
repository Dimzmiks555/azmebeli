from selenium import webdriver



def main(main_url, category_name):

    

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get(main_url)

    result = driver.find_element_by_css_selector(".composition_block").find_elements_by_css_selector('.item')
    
    urls = []

    for item in result:
        # link.click()

        item_data = {
            'link':item.find_element_by_css_selector('a').get_attribute('href'),
        }

        attrs = []

        attr_array = item.find_element_by_css_selector('.property').text.split(', ')

        for attr_str in attr_array:

            num = ""
            attr_name = ""

            for attr_letter in attr_str:
                if attr_letter == '(':
                    break

                if attr_letter == 'Ш':
                    attr_name = 'Ширина'
                elif attr_letter == 'В':
                    attr_name = 'Высота'
                elif attr_letter == 'Г':
                    attr_name = 'Глубина'

                if attr_letter.isdigit():
                    num = num + attr_letter
            attrs.append({
                'name': attr_name,
                'value': num + ' мм'
            })

        item_data['attrs'] = attrs


        urls.append(item_data)
        
    
    data = []

    for url in urls:
        driver.get(url['link'])
        print('Страница', url['link'])
        description = driver.find_element_by_css_selector('.tab_content').find_elements_by_css_selector('.tab_pane')[1].text
        title = category_name + ' ' + driver.find_element_by_tag_name('h1').text
        price = driver.find_element_by_class_name('price').text
        images_arr = []
        
        view_block = driver.find_element_by_id('view_block')

        imgs = view_block.find_elements_by_tag_name('img')

        for img_link in imgs:
            images_arr.append(img_link.get_attribute('src'))


        modules = driver.find_element_by_css_selector('.tab_content').find_element_by_css_selector('.module_block').find_elements_by_css_selector('.item')

        sub_products = []

        for module in modules:
            module_name = module.find_element_by_css_selector('.property').text
            module_price = module.find_element_by_css_selector('.price').text
            print(module_price)
            module_img = module.find_element_by_css_selector('.photo').find_element_by_css_selector('img').get_attribute('src')
            module_attrs = []

            module_attrs_str = module.find_element_by_css_selector('.property2').text
            module_attrs_str = module_attrs_str.replace('x',',')
            module_attrs_str = module_attrs_str.replace('х',',')
            module_attrs_str = module_attrs_str.replace('*',',')
            module_attrs_str_array = module_attrs_str.split(',')
            print(module_attrs_str_array)

            module_attrs.append({
                'name': 'Высота',
                'value': module_attrs_str_array[0] + ' мм'
            })
            module_attrs.append({
                'name': 'Ширина',
                'value': module_attrs_str_array[1] + ' мм'
            })
            if len(module_attrs_str_array) == 3:
                
                module_attrs.append({
                    'name': 'Глубина',
                    'value': module_attrs_str_array[2] + ' мм'
                })

            sub_products.append({
                'title': module_name,
                'price': module_price,
                'img': module_img,
                'attrs': module_attrs
            })







        data.append({
            "price": price,
            "attrs": url['attrs'],
            "title": title,
            "images": images_arr,
            'description': description,
            'sub_products': sub_products
        })

    
    print(data)
    return data

    

