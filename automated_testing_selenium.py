

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

firefox_options = Options()
firefox_options.add_argument("--incognito")
#firefox_options.add_argument("--headless")


result = []
stack = ["https://www.peminjaman-opagg.xyz"]
driver = webdriver.Firefox(options=firefox_options)
config = {
    'username': 'kagura',
    'password': 'kagura'
}

login_url = 'https://www.peminjaman-opagg.xyz/login.php'



while len(stack)> 0 and len(result) <5:
    driver.get(stack.pop())
    result.append(driver.title)
    elements = driver.find_elements_by_tag_name("a")
def main():
    driver = webdriver.Firefox()
    driver.get(login_url)
    
    elem = driver.find_element_by_name('username')
    elem.clear()
    elem.send_keys(config['username'])
    elem = driver.find_element_by_name('password')
    elem.clear()
    elem.send_keys(config['password'])
    elem.send_keys(Keys.RETURN)

    time.sleep(5)
if __name__ == '__main__':
    main()
    for elem in elements:
        url = elem.get_attribute('href')
        if url not in stack and url not in result and '#' not in url and 'https://www.peminjaman-opagg.xyz/login.php' in url:
        	stack.append(url)
    print(result)





