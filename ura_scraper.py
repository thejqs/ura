#!usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from lxml import etree
from lxml.cssselect import CSSSelector
import StringIO
import time


def open_url(url):
    '''
    navigates to our starting point
    '''
    driver = webdriver.Chrome()
    driver.get(url)

    return driver


def ditch_popup(driver):
    '''
    clicks out of an annoying modal that shouldn't be there in the first place
    '''
    time.sleep(1)
    driver.find_element_by_css_selector('div.modal-footer > button').click()


def get_text(driver):
    '''
    pulls out the raw text that contains what we're interested in
    '''
    time.sleep(1)
    raw_txt = driver.find_element_by_css_selector('#propertyListTable')
    return raw_txt.get_attribute('innerHTML')


def parse_text(text):
    '''
    turns the raw text into a DOM tree
    '''
    parser = etree.HTMLParser()
    return etree.parse(StringIO.StringIO(text), parser)


def get_target_text(tree):
    '''
    collects messy but useful strings from the DOM tree
    '''
    return tree.xpath('//*/text()')


def write_target_text_to_file(target_text):
    '''
    stashes our text in a file where a collaborator can clean it
    '''
    with open('messy_text.txt', 'a+') as f:
        print >> f, target_text


def do_the_damn_thang(url):
    '''
    runs the functions to slurp up the data thingies
    '''
    driver = open_url(url)
    ditch_popup(driver)
    text = get_text(driver)
    tree = parse_text(text)
    target_text = get_target_text(tree)
    write_target_text_to_file(target_text)
    driver.close()


if __name__ == '__main__':
    url = 'https://public-cpgh.epropertyplus.com/landmgmtpub/app/base/propertySearch?searchInfo=%7B%22criteria%22%3A%7B%22criterias%22%3A[]%7D%7D#'
    do_the_damn_thang(url)
