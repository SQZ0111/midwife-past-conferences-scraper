import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

def get_soup_from_url(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')


def fetch_past_conferences_page():
    driver = webdriver.Chrome()
    driver.get('https://www.midwiferytoday.com/')
    time.sleep(1)
    conference_button = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div/ul/li[2]')
    hover = ActionChains(driver).move_to_element(conference_button)
    hover.perform()
    past_conferences_button = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div/ul/li[2]/ul/li[4]/a')
    past_conferences_button.click()
    current_url = driver.current_url
    driver.quit()
    return current_url

def extract_conference_details(li, default_time):
    # Extracting place
    if li.find('a'):
        place = li.find('a').get_text()
        
        # Check if the place is not related to conferences, and if so, return None
        irrelevant_phrases = ["Click to share on", "Privacy Policy", "Terms of Use", "Contact Us", "FAQ", "Order FAQ", "My Account", "Accessibilty Statement"]
        for phrase in irrelevant_phrases:
            if phrase in place:
                return None
        
        # Extracting title
        title = None
        em_tag = li.find('em')
        if em_tag:
            title = em_tag.get_text()
        
        # Extracting time
        time_text = li.get_text()
        # We split by "•" and get the part that contains the date. The split will give parts: place, time, title.
        time_parts = time_text.split('•')
        time = default_time  # set default time from h3 heading
        if len(time_parts) > 1:
            potential_time = time_parts[1].strip()
            # Try to match the date pattern to avoid getting irrelevant details
            date_pattern = re.compile(r"(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2} – (?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}")
            match = date_pattern.search(potential_time)
            if match:
                time = match.group()
        
        return {
            "place": place,
            "title": title,
            "time": time
        }
    else:
        pass
