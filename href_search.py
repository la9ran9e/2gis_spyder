import re
import os
import time
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException, ElementNotVisibleException,
                                        StaleElementReferenceException, NoSuchWindowException)
from bs4 import BeautifulSoup
PATH = os.getcwd()
BLOCK_class = 'searchResults__list'
next_page_class = 'pagination__arrow _right'
next_page_xpath = '/html/body/div[1]/div/div[1]/div[2]\
/div[2]/div[3]/div/div[3]/div/div[3]/div[2]/div/div/div/\
div/div[2]/div/div[4]/div[2]/div[2]'
RESULTS_xpath = '/html/body/div[1]/div/div[1]\
/div[2]/div[2]/div[3]/div/div[3]/div/div[3]/div[2]/div/div/div/div/div[1]/h2'
RESULTS_class = 'searchResults__headerName'
testUrl_0 = 'https://2gis.ru/moscow/search/\
%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%\
D0%B5%20%D1%81%D0%B8%D0%B3%D0%B0%D1%80%D0%B5%D1%82%D1%8B%20%2F%20%D0%BA%D0%B0\
%D0%BB%D1%8C%D1%8F%D0%BD%D1%8B/tab/firms?queryState=zoom%2F11'
testUrl_1 = 'https://2gis.ru/moscow/search/adidas\
%20%D0%B4%D0%B8%D1%81%D0%BA%D0%BE%D0%BD%D1%82/tab/firms?queryState=zoom%2F11'
URL = testUrl_1
id_ = re.compile(r'id="[a-z0-9\-]*"')
link = re.compile(r'\?http.*$')
nums = re.compile(r'^[0-9]+')

def obj_call(name,
             by = 'id',
             m = 'repeat obj_call',
             Exception_ = NoSuchElementException,
             sleep = 2):
    obj = None
    while not obj:
        try:
            if by == 'id':
                obj = browser.find_element_by_id(name)
            elif by == 'class':
                obj = browser.find_element_by_class_name(name)
            elif by == 'xpath':
                obj = browser.find_element_by_xpath(name)
        except Exception_:
            print(m)
            time.sleep(sleep)
    return obj
            
def click_handler(obj,
                  m = 'repeat click_handler',
                  Exception_ = (ElementNotVisibleException, StaleElementReferenceException),
                  sleep_0 = 2,
                  sleep_1 = 5):
    Clicked = False
    while not Clicked:
        try:
            obj.click()
            time.sleep(sleep_0)
            Clicked = True
        except Exception_:
            print(m)
            time.sleep(sleep_1)
            
def search_contacts(class_name = 'contact'):
    contacts_BLOCK = None
    timeout = 0
    while not contacts_BLOCK and timeout < 5:
        timeout += 1
        try:
            contacts_BLOCK = browser.find_element_by_class_name(class_name)
        except NoSuchElementException:
            print('repeat search_contacts')
            try:
                contacts_BLOCK = browser.find_element_by_class_name('mediaContacts__block')
            except NoSuchElementException:
                time.sleep(3)
                
    if not contacts_BLOCK:
        print('contacts not found')
        
    if contacts_BLOCK:
        contacts_BLOCK_html = contacts_BLOCK.get_attribute('innerHTML')
        soup = BeautifulSoup(contacts_BLOCK_html, 'html.parser')
        elems = soup.find_all('a')

        Site_found = False
        for elem in elems:
            href = elem.get('href')
            if 'http://link.2gis.ru' in href and not Site_found :
                l = link.search(href)
                if l:
                    if '//m.' in href:
                        href = href.replace('m.', '')
                    href = l.group(0)[1:]
                    contacts_dict['site'] = href
                    write_list[2] = href
                    Site_found == True
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
    BLOCK = obj_call(BLOCK_class, by = 'class', m = 'repeat searcher')
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
            #print(id_name)
            obj = obj_call(id_name)
            click_handler(obj, sleep_0 = 1)
            search_contacts()
            log.append(name+address)
        
def find_text(class_name):
    text_elem = elem.find_all(class_ = class_name)
    text = text_elem[0].string
    text = text.replace('\xa0', ' ')
    return text

browser = webdriver.PhantomJS('%s/phantomjs' % PATH)
#Chrome('/home/la9ran9e/chromedriver')
#PhantomJS('%s/phantomjs' % PATH)
time.sleep(3)
Get_url = False
while not Get_url:
    try:
        browser.get(URL)
        Get_url = True
    except:
        print('repeat get_url')
        time.sleep(3)

RESULTS_elem = obj_call(RESULTS_class, by = 'class', m = 'repeat RESULT_elem')
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

iteration = 0        
try:
    while iteration < int(RESULTS):
        searcher(BLOCK_class)
        next_page = obj_call(next_page_xpath, by = 'xpath', m = 'repeat next_page')
        if next_page:
            click_handler(next_page)
    browser.close()
    w.close()
    print('Done')
except KeyboardInterrupt:
    print('Interrupted')
    w.close()
    log_file = open('%s/log' % PATH, 'w')
    log_file.write(';'.join(log))
    log_file.close()
