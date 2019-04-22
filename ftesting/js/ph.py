from selenium import webdriver
 
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.PhantomJS()
# driver.get('https://python.org')
 
# html = driver.page_source
# print(html)

driver.get('https://imgur.com/')
 
images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))
 
driver.close()