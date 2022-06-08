

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

    
    data = []
    
        
        

    # driver.get(main_url + "page" + '/' + str(i))

    catalog = driver.find_element_by_class_name('catalog-content__row ')

    cards = catalog.find_element_by_css_selector('.catalog-content__col')

    print(len(cards))

    urls = []

    for card in cards:
        # link.click()
        if not 'no_photo.png' in card.find_element_by_tag_name('img').get_attribute('src'):
            urls.append({
                'url': card.find_element_by_tag_name('a').get_attribute('href')
            })

        
    

    for card in urls:
        print('Страница', card['url'])
        driver.get(card['url'])
        
        sub_urls = []

        catalog = driver.find_element_by_class_name('catalog-content__row ')

        cards = catalog.find_element_by_css_selector('.catalog-content__col')

        for card in cards:
            if not 'no_photo.png' in card.find_element_by_tag_name('img').get_attribute('src'):
                sub_urls.append({
                    'url': card.find_element_by_tag_name('a').get_attribute('href')
                })
        for product in sub_urls:
            print('Страница', product['url'])
            driver.get(product['url'])

            product_info = driver.find_element_by_css_selector('.product-info')

            title = product_info.find_element_by_css_selector('h1').text
            price = product_info.find_element_by_css_selector('.product-info__cost-price').text

            description = ''

            attributes = []
            if driver.find_elements_by_css_selector('.product-item-detail-properties'): 
                tabs_data = driver.find_element_by_css_selector('.product-item-detail-properties').find_element_by_css_selector('.tabs_data')

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

            for image_block in driver.find_element_by_class_name('product-content__gallery').find_elements_by_css_selector('.product-item-detail-slider-image'):
                img = image_block.find_element_by_css_selector('img').get_attribute('src')
                images.append(img)

            data_info = {
                "price": price,
                "title": title,
                "url": images,
                "attrs": attributes,
                "description": description,
            }

            print(data_info)
            data.append(data_info)

    return data

        