#!usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from lxml import etree
from lxml.cssselect import CSSSelector
import StringIO
import time

driver = webdriver.Chrome()
driver.get('https://public-cpgh.epropertyplus.com/landmgmtpub/app/base/propertySearch?searchInfo=%7B%22criteria%22%3A%7B%22criterias%22%3A[]%7D%7D#')

time.sleep(1)

driver.find_element_by_css_selector('div.modal-footer > button').click()

time.sleep(1)

raw_txt = driver.find_element_by_css_selector('#propertyListTable')

txt = raw_txt.get_attribute('innerHTML')

parser = etree.HTMLParser()

tree = etree.parse(StringIO.StringIO(txt), parser)

messy_text = tree.xpath('//*/text()')

with open('messy_text.txt', 'a+') as f:
    print >> f, messy_text
