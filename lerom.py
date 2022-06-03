from selenium import webdriver


main_url ="http://www.lerom.ru/"

def main():

    

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get(main_url + "catalog/krovati/")

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
        description = driver.find_element_by_css_selector('.tab_content').text
        title = 'Кровать ' + driver.find_element_by_tag_name('h1').text
        price = driver.find_element_by_class_name('price').text
        images_arr = []
        
        view_block = driver.find_element_by_id('view_block')

        imgs = view_block.find_elements_by_tag_name('img')

        for img_link in imgs:
            images_arr.append(img_link.get_attribute('src'))


        data.append({
            "price": price,
            "attrs": url['attrs'],
            "title": title,
            "images": images_arr,
            'description': description
        })

    
    print(data)
    return data

    

