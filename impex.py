

from selenium import webdriver

url ='https://mebel-impex.ru/catalog/1001203373'

def main():


    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get(url)

    pagination = driver.find_element_by_id('pagination')

    ul_pagination = pagination.find_element_by_tag_name('ul')

    li_s_pagination = ul_pagination.find_elements_by_tag_name('li')

    print(len(li_s_pagination))

    
    data = []
    
    for i in range(1, len(li_s_pagination) - 1):
        

        driver.get(url + "?&page" + '=' + str(i))

        cards = driver.find_elements_by_class_name('card')

        

        urls = []

        for card in cards:
            # link.click()


            urls.append({
                'price':  card.find_element_by_class_name('uk-text-left').find_element_by_tag_name('span').text,
                'title':  card.find_element_by_class_name('uk-text-center').find_element_by_tag_name('a').text,
                'url': card.find_element_by_tag_name('a').get_attribute('href')
            })
            
        

        for card in urls:
            print('Страница', card['url'])
            driver.get(card['url'])

            
            
            description = driver.find_element_by_id('overview').find_element_by_tag_name('p').text


            images = []
            attributes = []

            for image in driver.find_element_by_id('Thumbnav_images').find_elements_by_css_selector('img'):

                if image.get_attribute('src') != None:
                    images.append(image.get_attribute('src'))


            for attrib in driver.find_element_by_id('characteristics').find_elements_by_css_selector('li'):

                attrib_arr = attrib.get_attribute("innerText").split(': ')
                if len(attrib_arr) == 2:
                    attr_name = attrib_arr[0]
                    attr_value = attrib_arr[1]

                    attr_name = attr_name.replace(' товара', '')

                    if attr_name == 'Ширина' or attr_name == 'Высота' or attr_name == 'Глубина':
                        attr_value = str(int(float(attr_value.replace(',','.')) * 10)) + ' мм'
                    if attr_name == 'Вес':
                        attr_value = attr_value.replace(',','.') + ' кг'

                    attributes.append({"name": attr_name, "value": attr_value})


            data.append({
                "price": card['price'],
                "title": card['title'],
                "url": images,
                "attrs": attributes,
                "description": description,
                "page": i
            })
    return data

        