from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import config

opts = Options()
opts.headless = True
driver = webdriver.Firefox(options=opts)

driver.get("https://" + config.ipdnswhatever + "/network/certificates")


search_usernamefield = driver.find_element_by_name('username')
search_usernamefield.send_keys(config.username)
serach_passwordfield = driver.find_element_by_name('password')
serach_passwordfield.send_keys(config.password)
search_loginbutton = driver.find_element_by_id('_login')
search_loginbutton.click()

search_addcertbutton = driver.find_element_by_class_name('button-secondary')
search_addcertbutton.click()

driver.find_element_by_xpath("//select[@name='add_import_option']/option[text()='Import Certificate']").click()

search_browseuploadbutton = driver.find_element_by_name('cert_file')
search_browseuploadbutton.send_keys(config.p12filelocation)

search_passphrasefield = driver.find_element_by_id('cert_pass')
search_passphrasefield.send_keys(config.p12passphrase)

search_nextbutton = driver.find_element_by_class_name('submit')
search_nextbutton.click()

search_submitbutton = driver.find_element_by_class_name('submit')
search_submitbutton.click()

search_commitbutton = driver.find_element_by_class_name('button-changes')
search_commitbutton.click()

search_commitchangesbutton = driver.find_element_by_id('commit_btn')
search_commitchangesbutton.click()

driver.close()