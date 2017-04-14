import re
import os
import time
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, ElementNotVisibleException,
                                        StaleElementReferenceException, NoSuchWindowException)
from bs4 import BeautifulSoup
PATH = os.getcwd()
browser = webdriver.PhantomJS('%s/phantomjs' % PATH)
#Chrome('/home/la9ran9e/chromedriver')
#PhantomJS('%s/phantomjs' % PATH)
BLOCK_class = 'searchResults__list'
next_page_class = 'pagination__arrow _right'
next_page_xpath = '/html/body/div[1]/div/div[1]/div[2]\
/div[2]/div[3]/div/div[3]/div/div[3]/div[2]/div/div/div/\
div/div[2]/div/div[4]/div[2]/div[2]'
RESULTS_xpath = '/html/body/div[1]/div/div[1]\
/div[2]/div[2]/div[3]/div/div[3]/div/div[3]/div[2]/div/div/div/div/div[1]/h2'
RESULTS_class = 'searchResults__headerName'
URL ='https://2gis.ru/moscow/search/\
%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%\
D0%B5%20%D1%81%D0%B8%D0%B3%D0%B0%D1%80%D0%B5%D1%82%D1%8B%20%2F%20%D0%BA%D0%B0\
%D0%BB%D1%8C%D1%8F%D0%BD%D1%8B/tab/firms?queryState=zoom%2F11'
'''https://2gis.ru/moscow/search/adidas\
%20%D0%B4%D0%B8%D1%81%D0%BA%D0%BE%D0%BD%D1%82/tab/firms?queryState=zoom%2F11'''
'''https://2gis.ru/moscow/search/\
%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%\
D0%B5%20%D1%81%D0%B8%D0%B3%D0%B0%D1%80%D0%B5%D1%82%D1%8B%20%2F%20%D0%BA%D0%B0\
%D0%BB%D1%8C%D1%8F%D0%BD%D1%8B/tab/firms?queryState=zoom%2F11'''
id_ = re.compile(r'id="[a-z0-9\-]*"')
link = re.compile(r'\?http[\:\/\.a-zA-Z0-9\-\_\+]*$')
nums = re.compile(r'^[0-9]+')
browser.get(URL)
time.sleep(3)
RESULTS_elem = browser.find_element_by_class_name(RESULTS_class)
RESULTS_ = RESULTS_elem.text
RESULTS = nums.search(RESULTS_)
RESULTS = RESULTS.group(0)
print(RESULTS)
list_dir = os.listdir(PATH)
if 'log' in list_dir:
    log_file = open('%s/log' % PATH)
    log_line = log_file.read()
    log = log_line.split(';')
else:
    log = []
if '2gis_base' in list_dir:
    w = open('%s/2gis_base' % PATH, 'a')
else:
    w = open('%s/2gis_base' % PATH, 'w')
    w.write(';'.join(['name', 'address', 'site', 'vk.com',
             'twitter.com', 'facebook.com', 'instagram.com',
                      'youtube.com', 'plus.google.com', 'telegram', 'ok.ru',
                      'tel', 'skype'])\
            +'\n')
         

def obj_call(id_name):
    obj = None
    while not obj:
        try:
            obj = browser.find_element_by_id(id_name)
        except NoSuchElementException:
            print('repeat find obj')
            time.sleep(2)
    click_handler(obj)
            
def click_handler(obj):
    Clicked = False
    while not Clicked:
        try:
            obj.click()
            time.sleep(3)
            Clicked = True
        except (ElementNotVisibleException, StaleElementReferenceException):
            print('repeat click')
            time.sleep(5)
            
def search_contacts(class_name = 'contact'):
    contacts_BLOCK = None
    timeout = 0
    while not contacts_BLOCK and timeout < 5:
        timeout += 1
        try:
            contacts_BLOCK = browser.find_element_by_class_name(class_name)
        except NoSuchElementException:
            try:
                contacts_BLOCK = browser.find_element_by_class_name('mediaContacts__block')
            except NoSuchElementException:
                time.sleep(3)        
    if contacts_BLOCK:
        contacts_BLOCK_html = contacts_BLOCK.get_attribute('innerHTML')
        soup = BeautifulSoup(contacts_BLOCK_html, 'html.parser')
        elems = soup.find_all('a')
        for elem in elems:
            href = elem.get('href')
            if 'http://link.2gis.ru' in href:
                l = link.search(href)
                if l:
                    if '//m.' not in href:
                        href = l.group(0)[1:]
                        contacts_dict['site'] = href
                        write_list[2] = href
            elif 'vk.com' in href:
                contacts_dict['vk.com'] = href
                write_list[3] = href
            elif 'twitter.com' in href:
                contacts_dict['twitter.com'] = href
                write_list[4] = href
            elif 'facebook.com' in href:
                contacts_dict['facebook.com'] = href
                write_list[5] = href
            elif 'instagram.com' in href:
                contacts_dict['instagram.com'] = href
                write_list[6] = href
            elif 'youtube.com' in href:
                contacts_dict['youtube.com'] = href
                write_list[7] = href
            elif 'plus.google.com' in href:
                contacts_dict['plus.google.com'] = href
                write_list[8] = href
            elif 'telegram' in href:
                contacts_dict['telegram'] = href
                write_list[9] = href
            elif 'ok.ru' in href:
                contacts_dict['ok.ru'] = href
                write_list[10] = href
            elif 'tel:' in href:
                href = href[4:]
                contacts_dict['tel'] = href
                write_list[11] = href
            elif 'skype:' in href:
                href = href[6:]
                contacts_dict['tel'] = href
                write_list[12] = href
            print('>>> %s' % href)
    #print(write_list)
    w.write(';'.join(write_list) + '\n')

def searcher(BLOCK_class):
    global elem, contacts_dict, write_list, iteration, log
    contacts_dict = {}
    BLOCK = None
    while not BLOCK:
        try:
            BLOCK = browser.find_element_by_class_name(BLOCK_class)
        except NoSuchElementException:
            print('repeat find BLOCK')
            time.sleep(3)
    BLOCK_html = BLOCK.get_attribute('innerHTML')
    soup = BeautifulSoup(BLOCK_html, 'html.parser')
    elems = soup.find_all('article')
    for elem in elems:
        write_list = ['NaN']*13
        iteration += 1
        print('<%s>' % iteration)
        name = find_text("miniCard__headerTitleLink")
        address = find_text('miniCard__address')
        if name+address not in log:
            print(name)
            contacts_dict['name'] = name
            write_list[0] = name
            print(address)
            contacts_dict['address'] = address
            write_list[1] = address
            elem = str(elem)
            m = id_.search(elem)
            id_name = m.group(0)[4:-1]
            print(id_name)
            obj_call(id_name)
            search_contacts()
            log.append(name+address)
    
    
def find_text(class_name):
    text_elem = elem.find_all(class_ = class_name)
    text = text_elem[0].string
    text = text.replace('\xa0', ' ')
    return text
    
def next_pages_searcher(m = 'Pages not found'):
    try:
        next_page = browser.find_element_by_xpath(next_page_xpath)
        time.sleep(2)
    except NoSuchElementException:
        print('# %s' % m)
        next_page = None
    return next_page

iteration = 0        
try:
    next_page = next_pages_searcher()
    if next_page:
        while iteration < int(RESULTS):
            searcher(BLOCK_class)
            next_page = next_pages_searcher()
            if next_page:
                click_handler(next_page)
                
    else:
        searcher(BLOCK_class)
except KeyboardInterrupt:
    w.close()
    log_file = open('%s/log' % PATH, 'w')
    log_file.write(';'.join(log))
    log_file.close()
    browser.close()
browser.close()
w.close()
