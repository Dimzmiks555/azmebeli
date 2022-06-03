from selenium import webdriver
from selenium.webdriver.common.by import By
from sympy import product
import green
from time import sleep
from attr import attributes
import requests
from woocommerce import API
from methods.uploadKvartalGroupedWC import uploadKvartalGroupedWC
from methods.uploadKvartalWC import uploadKvartalWC
from methods.uploadLeromGroupedWC import uploadLeromGroupedWC
from methods.uploadLeromWC import uploadLeromWC
import sonberry
import lerom
import impex
import eone
import kvartal
import lerom_grouped
import kvartal_grouped
from methods.uploadImpexWC import uploadImpexWC




if __name__ == "__main__":
    # lerom.main()
    # sonberry.main('matrasy', 22)
    # sonberry.main('krovati', 17)
    # sonberry.main('podushki', 1)
    # sonberry.main('tekstil', 1)
    # sonberry.main('mebel-dlya-spalni', 1)

    


    kreslo_url = 'https://green3.ru/catalog/kreslo'
    kachalki_url = 'https://green3.ru/catalog/kresla_kachalki/'
    pufy_url = 'https://green3.ru/catalog/pufy/'


    
    # data_kachalki = green.main(kachalki_url, 7)
    # data_kreslo = green.main(kreslo_url, 11)
    # data_pufy = green.main(pufy_url, 4)


    # uploadGreenWC(data_kachalki, 94)
    # uploadGreenWC(data_kreslo, 101)
    # uploadGreenWC(data_pufy, 95)
    
    
    
    # data_impex = impex.main()

    # print(data_impex)

    kvartal_skaff_raspash_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/shkafy/raspashnye/'
    kvartal_skaff_kupe_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/shkafy/shkafy-kupe/'
    kvartal_mygkaya_mebel_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/myagkaya-mebel/'
    kvartal_matrasy_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/matrasy/'
    kvartal_krovati_iz_massiva_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/krovati/krovati-iz-massiva/'
    kvartal_krovati_iz_ldsp_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/krovati/krovati-iz-ldsp-i-mdf/'
    kvartal_data_krovati_interiernie_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/krovati/krovati-interernye/'
    kvartal_data_krovati_detskie_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/krovati/detskie-krovati/'
    kvartal_data_prikrovatnye_tumby_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/krovati/prikrovatnye-tumby/'
    kvartal_data_kuhni_gotovie_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/kuhni/kollektsiya-gotovyh-reshenij/'
    kvartal_data_obedennie_zony_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/kuhni/obedennye-zony/'
    kvartal_data_obedennie_stoli_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/kuhni/obedennye-stoly/'
    kvartal_data_stulya_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/kuhni/stulya-taburety/'
    kvartal_data_komody_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/malye-formy/komody/'
    kvartal_data_stoly_zhurnalnye_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/malye-formy/stoly-zhurnalnye/'
    kvartal_data_stoly_komp_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/malye-formy/stoly-kompyuternye-i-party/'
    kvartal_data_stoly_makiazh_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/malye-formy/stoly-makiyazhnye/'
    kvartal_data_polki_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/malye-formy/stellazhi-i-polki/'
    kvartal_data_office_chairs_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/malye-formy/ofisnye-kresla-i-stulya/'
    kvartal_data_gostinue_gotovie_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/gostinye/gotovye-resheniya/'
    kvartal_data_prihozh_ready_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/prihozhie/gotovye-resheniya-prihozhie/'
    kvartal_data_prihozh_obuv_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/prihozhie/obuvnitsy/'


    
    kvartal_spalni_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/spalnye-garnitury/'
    kvartal_detskie_group_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/detskie/'
    kvartal_gostinue_group_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/gostinye/modulnye-resheniya/'
    kvartal_prihozh_group_url = 'https://xn----7sbafbvb7ameh8b0a2m.xn--p1ai/product-category/prihozhie/modulnye-resheniya-prihozhie/'
    

    # data_kvartal_shaff_raspash = kvartal.main(kvartal_skaff_raspash_url)
    # data_mygkaya_mebel = kvartal.main(kvartal_mygkaya_mebel_url)
    # data_matrasy = kvartal.main(kvartal_matrasy_url)
    # data_krovati_iz_massiva = kvartal.main(kvartal_krovati_iz_massiva_url)
    # data_krovati_iz_ldsp = kvartal.main(kvartal_krovati_iz_ldsp_url)
    # data_krovati_interiernie = kvartal.main(kvartal_data_krovati_interiernie_url)
    # data_krovati_detskie = kvartal.main(kvartal_data_krovati_detskie_url)
    # data_prikrovatnye_tumby = kvartal.main(kvartal_data_prikrovatnye_tumby_url)
    # data_skaff_kupe = kvartal.main(kvartal_skaff_kupe_url)
    # data_kuhni_gotovie = kvartal.main(kvartal_data_kuhni_gotovie_url)
    # data_obedennie_zony = kvartal.main(kvartal_data_obedennie_zony_url)
    # data_obedennie_stoli = kvartal.main(kvartal_data_obedennie_stoli_url)
    # data_stulya = kvartal.main(kvartal_data_stulya_url)
    # data_komody = kvartal.main(kvartal_data_komody_url)
    # data_stoly_zhurnalnye = kvartal.main(kvartal_data_stoly_zhurnalnye_url)
    # data_stoly_komp = kvartal.main(kvartal_data_stoly_komp_url)
    # data_stoly_makiazh = kvartal.main(kvartal_data_stoly_makiazh_url)
    # data_polki = kvartal.main(kvartal_data_polki_url)
    # data_office_chairs = kvartal.main(kvartal_data_office_chairs_url)
    # data_gostinue_gotovie = kvartal.main(kvartal_data_gostinue_gotovie_url)
    # data_prihozh_ready = kvartal.main(kvartal_data_prihozh_ready_url)
    # data_prihozh_obuv = kvartal.main(kvartal_data_prihozh_obuv_url)

    
    # data_kv_spalni = kvartal_grouped.main(kvartal_spalni_url)
    # data_kv_detskie = kvartal_grouped.main(kvartal_detskie_group_url)
    # data_kv_gostinue_group = kvartal_grouped.main(kvartal_gostinue_group_url)
    # data_kv_prihozh_group = kvartal_grouped.main(kvartal_prihozh_group_url)




    # uploadKvartalWC(data_kvartal_shaff_raspash, 98)
    # uploadKvartalWC(data_mygkaya_mebel, 104)
    # uploadKvartalWC(data_matrasy, 71)
    # uploadKvartalWC(data_krovati_iz_massiva, 93)
    # uploadKvartalWC(data_krovati_iz_ldsp, 93)
    # uploadKvartalWC(data_krovati_interiernie, 93)
    # uploadKvartalWC(data_krovati_detskie, 93)
    # uploadKvartalWC(data_prikrovatnye_tumby, 105)
    # uploadKvartalWC(data_skaff_kupe, 96)
    # uploadKvartalWC(data_kuhni_gotovie, 100)
    # uploadKvartalWC(data_obedennie_zony, 100)
    # uploadKvartalWC(data_obedennie_stoli, 106)
    # uploadKvartalWC(data_stulya, 566)
    # uploadKvartalWC(data_komody, 105)
    # uploadKvartalWC(data_stoly_zhurnalnye, 106)
    # uploadKvartalWC(data_stoly_komp, 106)
    # uploadKvartalWC(data_stoly_makiazh, 106)
    # uploadKvartalWC(data_polki, 107)
    # uploadKvartalWC(data_office_chairs, 566)
    # uploadKvartalWC(data_gostinue_gotovie, 97)
    # uploadKvartalWC(data_prihozh_ready, 828)
    # uploadKvartalWC(data_prihozh_obuv, 830)

    # uploadKvartalGroupedWC(data_kv_spalni, 102)
    # uploadKvartalGroupedWC(data_kv_detskie, 103)
    # uploadKvartalGroupedWC(data_kv_gostinue_group, 97)
    # uploadKvartalGroupedWC(data_kv_prihozh_group, 829)



    # data_lerom_krovati = lerom.main()

    # uploadLeromWC(data_lerom_krovati, 93)

    
    # data_lerom_prihozh = lerom_grouped.main('http://www.lerom.ru/catalog/karina-pr/' ,'Прихожая')
    # data_lerom_prihozh_melissa = lerom_grouped.main('http://www.lerom.ru/catalog/melissa-prikh-2021/' ,'Прихожая')
    # data_lerom_detskay_karina = lerom_grouped.main('http://www.lerom.ru/catalog/karina-d/' ,'Детская')
    # data_lerom_detskay_melissa = lerom_grouped.main('http://www.lerom.ru/catalog/melissa-detskaya-2021/' ,'Детская')
    data_lerom_spal_karina = lerom_grouped.main('http://www.lerom.ru/catalog/karina-sp/' ,'Спальня')
    data_lerom_spal_melissa = lerom_grouped.main('http://www.lerom.ru/catalog/melissa-2021/' ,'Спальня')
    data_lerom_gost_melissa = lerom_grouped.main('http://www.lerom.ru/catalog/melissa-gotsinye-2021/' ,'Гостиная')
    data_lerom_gost_karina = lerom_grouped.main('http://www.lerom.ru/catalog/karina-gost/' ,'Гостиная')
    data_lerom_gost_kamelia = lerom_grouped.main('http://www.lerom.ru/catalog/kameliya-gost-2021/' ,'Гостиная')

    # uploadLeromGroupedWC(data_lerom_prihozh, 829, 920)
    # uploadLeromGroupedWC(data_lerom_prihozh_melissa, 829, 920)
    # uploadLeromGroupedWC(data_lerom_detskay_karina, 993, 992)
    # uploadLeromGroupedWC(data_lerom_detskay_melissa, 993, 992)
    uploadLeromGroupedWC(data_lerom_spal_karina, 1002, 1001)
    uploadLeromGroupedWC(data_lerom_spal_melissa, 1002, 1001)
    uploadLeromGroupedWC(data_lerom_gost_melissa, 1005, 1004)
    uploadLeromGroupedWC(data_lerom_gost_karina, 1005, 1004)
    uploadLeromGroupedWC(data_lerom_gost_kamelia, 1005, 1004)


    

    # eone.main()

    # uploadImpexWC(data_impex, 94)

    

