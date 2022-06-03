from selenium import webdriver
from time import sleep


def main():


    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    
    driver.maximize_window()
    driver.get('https://www.e-1.ru/catalog/shkafy_kupe')

    
    for i in range(1, 10):
        

        driver.get('https://www.e-1.ru/catalog/shkafy_kupe' + "/?PAGEN_1" + '=' + str(i))

        driver.execute_script("window.scrollTo(0, +document.body.scrollHeight / 8)")

        sleep(1)
        
        driver.execute_script("window.scrollTo(0, (+document.body.scrollHeight / 8) * 2)")
        
        sleep(1)

        driver.execute_script("window.scrollTo(0, (+document.body.scrollHeight / 8) * 3)")
        
        sleep(1)
        
        driver.execute_script("window.scrollTo(0, (+document.body.scrollHeight / 8) * 4)")

        sleep(1)
        
        driver.execute_script("window.scrollTo(0, (+document.body.scrollHeight / 8) * 5)")
        
        sleep(1)

        driver.execute_script("window.scrollTo(0, (+document.body.scrollHeight / 8) * 6)")
        
        sleep(1)
        
        driver.execute_script("window.scrollTo(0, (+document.body.scrollHeight / 8) * 7)")


        sleep(60)

        imgs = driver.find_elements_by_class_name('item_block')


        items = []

        for img in imgs:
            # link.click()

            loc_data = {
                'url': img.find_element_by_class_name('image_wrapper_block').find_element_by_tag_name('a').get_attribute('href'),
                'title': img.find_element_by_class_name('item-title').text,
                'img': img.find_element_by_class_name('image_wrapper_block').find_element_by_tag_name('img').get_attribute('src'),
            }

            print(loc_data)

            items.append(loc_data)
            
        
        # data = []

        # for item in items:
        #     print('Страница',item['url'])
        #     driver.get(item['url'])

        #     title = driver.find_element_by_class_name('title-card').text
        #     price = driver.find_element_by_class_name('price').text

            
        #     description = driver.find_element_by_id('about-product').find_element_by_tag_name('p').text




        #     img_urls = []

        #     slider = driver.find_element_by_class_name('slick-list').find_elements_by_tag_name('img')

        #     for img in slider:
        #         img_urls.append(img.get_attribute('src'))
            
        #     # view_block = driver.find_element_by_id('view_block')
        #     print({
        #         "price": price,
        #         "title": title,
        #         "url": img_urls,
        #         "description": description,
        #         "page": i
        #     })
        #     # img = view_block.find_element_by_tag_name('img')
        #     # img_url = img.get_attribute('src')
        #     # print(img, img_url)


        #     data.append({
        #         "price": price,
        #         "title": title,
        #         "url": img_urls,
        #         "description": description,
        #         "page": i
        #     })

        
        # print(data)