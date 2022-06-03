

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1920,1080")
chrome_options.headless = True

def main(main_url):


    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="chromedriver.exe")
    
    driver.get(main_url)

    
    max_page = 1

    pagination = []

    if driver.find_elements_by_class_name('wp-pagenavi'):
        pagination = driver.find_element_by_class_name('wp-pagenavi')

        if pagination.find_elements_by_css_selector('.last'):
            last_pagination_elem = pagination.find_element_by_css_selector('.last').get_attribute('href')
            last_url_array = last_pagination_elem.split('/')
            max_page = last_url_array[len(last_url_array) - 2]
        else:
            pagination_elems = pagination.find_elements_by_css_selector('.larger')
            end_pagination_elem = pagination_elems[len(pagination_elems) - 1]
            end_url_array = end_pagination_elem.get_attribute('href').split('/')
            max_page = end_url_array[len(end_url_array) - 2]


    
    data = []
    
    for i in range(1, int(max_page)+ 1):
        
        print(i)

        driver.get(main_url + "page" + '/' + str(i))

        cards = driver.find_element_by_id('content').find_element_by_class_name('catalog').find_elements_by_class_name('item')

        print(len(cards))

        urls = []

        for card in cards:
            # link.click()


            urls.append({
                'price':  card.find_element_by_class_name('price').text,
                'title':  card.find_element_by_class_name('name').text,
                'url': card.find_element_by_class_name('img').get_attribute('href')
            })
            
        

        for card in urls:
            print('Страница', card['url'])
            driver.get(card['url'])
            
            description = ''
            attributes = []

            if driver.find_elements_by_css_selector('.tabs_data'): 
                tabs_data = driver.find_element_by_css_selector('.tabs_product').find_element_by_css_selector('.tabs_data')

                tabs_data_divs = tabs_data.find_elements_by_css_selector('div')


                description = tabs_data_divs[len(tabs_data_divs) - 1].text

                for attrib in tabs_data_divs[0].find_elements_by_css_selector('.clr'):
                    
                    attrib_arr = attrib.find_elements_by_css_selector('span')
                    attr_name = attrib_arr[0].get_attribute("innerText")
                    attr_value = attrib_arr[1].get_attribute("innerText")
                    if attr_name == 'Ширина' or attr_name == 'Высота' or attr_name == 'Глубина':
                        attr_value = attr_value + ' мм'
                    if attr_name == 'Вес':
                        attr_value = attr_value.replace(',','.') + ' кг'

                    attributes.append({"name": attr_name, "value": attr_value})



            images = []

            if driver.find_element_by_class_name('two_info_product').find_elements_by_css_selector('.owl-stage'):
                for owl_item in driver.find_element_by_class_name('two_info_product').find_element_by_css_selector('.owl-stage').find_elements_by_css_selector('.owl-item'):

                    if owl_item.get_attribute("class") == 'owl-item':
                        img = owl_item.find_element_by_css_selector('img').get_attribute('src')
                        images.append(img)
            else:
                img = driver.find_element_by_css_selector('.main_img').find_element_by_css_selector('img').get_attribute('src')
                images.append(img)

            images.reverse()

            data_info = {
                "price": card['price'],
                "title": card['title'],
                "url": images,
                "attrs": attributes,
                "description": description,
                "page": i
            }

            print(data_info)
            data.append(data_info)

    return data

        