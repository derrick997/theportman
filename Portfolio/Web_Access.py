from selenium import webdriver
import bs4
import re
import requests
#import browsercookie
#import json
import urllib.request

# Access a site that requires javascript, and wait for an element to be loaded (optional)
def accessWithJavascript(direccion, waittime=12):

    driver = webdriver.PhantomJS()
    #print(timestamp())
    driver.implicitly_wait(waittime)
    driver.get(direccion)

    # page_source gets page after rendering is complete
    page = bs4.BeautifulSoup(driver.page_source, "lxml")

    #driver.save_screenshot('screenc.png')
    driver.quit()

    return str(page)

def accessWithBs(direccion):
    r = requests.get(direccion)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    #data = soup.find('span', attrs={'id': 'yfs_l84_'.format(name)})
    return soup.text



# Try to access url up to 10 times
def access(direccion):
    page = read(direccion)
    attempts = 1
    while (page == "<COULDN'T ACCESS WEBSITE>") and (attempts <= 10):
        page = read(direccion)
        attempts += 1
    return page

# Read page with urllib
def read(direccion):
    try:
        stream = urllib.request.urlopen(direccion)
        page = stream.read()
        stream.close()
        return page

    except IOError:
        return "<COULDN'T ACCESS WEBSITE>"


def obtenerCookies(direccion):
    r = requests.get(direccion)
    c = r.headers
    i = c.items()
    #print(c.values())
    #print(c.items())

    for name, value in i:
        if name == "Set-Cookie":
            # print(value)
            endIndex = value.find(";")
            # print(value[:endIndex])
            return str(value[:endIndex+1])
    return str(0)
