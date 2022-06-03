from selenium import webdriver

def main(category, page_key):

    sonberry_url = 'https://sonberry.ru/'

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get(sonberry_url + category + "/")

    pagination = driver.find_element_by_class_name('bx-pagination-container')

    ul_pagination = pagination.find_element_by_tag_name('ul')

    li_s_pagination = ul_pagination.find_elements_by_tag_name('li')

    print(len(li_s_pagination))
    
    for i in range(1, len(li_s_pagination) - 1):
        
        print(i, sonberry_url + category + "/?PAGEN_" + str(page_key) + '=' + str(i))

        driver.get(sonberry_url + category + "/?PAGEN_" + str(page_key) + '=' + str(i))

        links = driver.find_elements_by_class_name('product-item-image-wrapper')

        print(links, links.__len__)

        urls = []

        for link in links:
            # link.click()
            urls.append(link.get_attribute('href'))
            
        
        data = []

        for url in urls:
            print('Страница', url)
            driver.get(url)

            title = driver.find_element_by_class_name('product-card-heading').text
            price = driver.find_element_by_class_name('product-item-detail-price-current').text

            if (category == 'tekstil'):
                description = ''
            else:
                description = driver.find_element_by_class_name('product-item-detail-content').find_element_by_tag_name('div').text

            img_url = ''
            
            # view_block = driver.find_element_by_id('view_block')
            print({
                "price": price,
                "title": title,
                "url": img_url,
                "description": description,
                "page": i
            })
            # img = view_block.find_element_by_tag_name('img')
            # img_url = img.get_attribute('src')
            # print(img, img_url)


            data.append({
                "price": price,
                "title": title,
                "url": img_url,
                "page": i
            })

        
        print(data)
