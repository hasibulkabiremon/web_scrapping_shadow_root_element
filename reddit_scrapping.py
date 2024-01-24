from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def comment_scrapper(driver):
    item = driver.find_elements(By.XPATH,"//post-consume-tracker/div/faceplate-tracker[1]/a")
    print(len(item))
    list_link = [x.get_attribute('href') for x in item]
    print(list_link)
    print(len(list_link))
    for x in list_link:
        print(list_link.index(x),'/',len(list_link))
        print('Link:',x)
        driver.get(x)
        time.sleep(3)
        comments = driver.find_elements(By.XPATH,"//div[@id='-post-rtjson-content']")
        list_comment = [x.text for x in comments]
        print(len(list_comment),list_comment)
        


# Set the path to your webdriver (e.g., chromedriver.exe)

q = input('What do you want to search about:')


# Initialize the webdriver (assuming you are using Chrome)
driver = webdriver.Firefox()

# Open Reddit
driver.get("https://www.reddit.com/")

# Wait for the page to load (you might need to adjust the sleep time)


driver.maximize_window()

time.sleep(3)

search_area = driver.execute_script('return document.querySelector("body > shreddit-app").querySelector("reddit-header-large").querySelector("reddit-header-action-items").querySelector("header").querySelector("nav").querySelector("div:nth-child(2)").querySelector("div > div > search-dynamic-id-cache-controller > reddit-search-large").shadowRoot.querySelector("div").querySelector("div > form > faceplate-search-input").shadowRoot.querySelector("label").querySelector("div > span:nth-child(3) > input")')
search_area.click()
search_area.send_keys(q)
search_area.send_keys(Keys.ENTER)



time.sleep(5)


comment_scrapper(driver)


# # Find the search input element
# search_input = driver.find_elements(By.XPATH, "/html/body/shreddit-app/search-dynamic-id-cache-controller/div/div/div[1]/div[2]/main/div/reddit-feed/faceplate-tracker")
# driver.back()

# print(len(search_input))
# for x in search_input:
#     # print(x.text)
#     x.click()
#     driver.back()
    