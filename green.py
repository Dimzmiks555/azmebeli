from attr import attr
from selenium import webdriver

def main(main_url, pages):


    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get(main_url)

    pagination = driver.find_element_by_class_name('wrapp-pagination')

    ul_pagination = pagination.find_element_by_tag_name('ul')

    li_s_pagination = ul_pagination.find_elements_by_tag_name('li')

    print(len(li_s_pagination))

    
    data = []
    
    for i in range(1, pages):
        

        driver.get(main_url + "?PAGEN_1" + '=' + str(i))

        imgs = driver.find_elements_by_class_name('img-item')

        

        urls = []

        for img in imgs:
            # link.click()
            urls.append(img.find_element_by_tag_name('a').get_attribute('href'))
            
        

        for url in urls:
            print('Страница', url)
            driver.get(url)

            title = driver.find_element_by_class_name('title-card').text
            price = driver.find_element_by_class_name('price').text

            
            description = driver.find_element_by_id('about-product').find_element_by_tag_name('p').text




            img_urls = []
            attributes = []

            slider = driver.find_element_by_class_name('slick-list').find_elements_by_tag_name('img')

            characters_block = driver.find_element_by_class_name('wrapp-characteristics-tabs-card').find_elements_by_class_name('item-characteristic-tabs')

            for charact in characters_block:

                if charact.find_elements_by_css_selector('.value-characteristic'):
                    char_name = charact.find_element_by_css_selector('.name-characteristic').get_attribute("innerText")
                    char_value = charact.find_element_by_css_selector('.value-characteristic').get_attribute("innerText")
                    attributes.append({"name": char_name, "value": char_value})
            

            for img in slider:
                img_urls.append(img.get_attribute('src'))
            
            # view_block = driver.find_element_by_id('view_block')
            # img = view_block.find_element_by_tag_name('img')
            # img_url = img.get_attribute('src')
            # print(img, img_url)
            print(attributes)

            resultat = {
                "price": price,
                "title": title,
                "url": img_urls,
                "attrs": attributes,
                "description": description,
                "page": i
            }
    
            data.append(resultat)

        
    return data