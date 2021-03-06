

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from woocommerce import API

chrome_options = Options()
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1920,1080")
chrome_options.headless = True

def main(main_url):

    wcapi = API(
        url="https://az-mebel.ru/",
        consumer_key="ck_292e3970d43f0934000f671a2dad593a9c320e43",
        consumer_secret="cs_c8c878c0530c656729d90a94345c892485b80f07",
        timeout=1000000
    )

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
                # 'price':  card.find_element_by_class_name('price').text,
                'title':  card.find_element_by_class_name('name').text,
                'url': card.find_element_by_class_name('img').get_attribute('href')
            })
            
        

        for card in urls:
            print('????????????????', card['url'])
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
                    if attr_name == '????????????' or attr_name == '????????????' or attr_name == '??????????????':
                        attr_value = attr_value + ' ????'
                    if attr_name == '??????':
                        attr_value = attr_value.replace(',','.') + ' ????'

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

            variants = []

            if driver.find_elements_by_class_name('catalog'):
                items = driver.find_element_by_class_name('catalog').find_elements_by_css_selector('.item')
                for prod in items:
                    item_name = prod.find_element_by_class_name('name').text
                    wc_products = wcapi.get('products', params={
                        "search": item_name
                    }).json()
                    print(len(wc_products))
                    
                    if len(wc_products) != 0:
                        variants.append(wc_products[0]['id'])



            data_info = {
                "title": card['title'],
                "url": images,
                "attrs": attributes,
                "description": description,
                "variants": variants,
                "page": i
            }

            print(data_info)
            data.append(data_info)

    return data

        