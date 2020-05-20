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

search_certtoedit = driver.find_element_by_link_text(config.certname)
search_certtoedit.click()

search_certuploadbutton = driver.find_element_by_name('signed_cert')
search_certuploadbutton.send_keys(config.certfilelocation)

search_submitbutton = driver.find_element_by_class_name('submit')
search_submitbutton.click()

search_commitbutton = driver.find_element_by_class_name('button-changes')
search_commitbutton.click()

search_commitchangesbutton = driver.find_element_by_id('commit_btn')
search_commitchangesbutton.click()

driver.close()