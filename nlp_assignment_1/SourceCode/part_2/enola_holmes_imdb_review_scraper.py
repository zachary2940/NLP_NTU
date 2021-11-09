from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.imdb.com/title/tt7846844/reviews?ref_=tt_ql_3"

browser.get(url)

while True:
    try:
        loadMoreButton = browser.find_element_by_class_name('ipl-load-more__button')
        # time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        break
print("Complete")
time.sleep(10)

reviews_soup = BeautifulSoup(browser.page_source)

with open('imdb_enola_holmes_reviews.csv', mode='w', encoding='utf-8') as csv_file:
  fieldnames = ['user_name', 'review_title', 'review_date', 'review_text', 'rating']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  for review in reviews_soup.find_all('div', {'class': 'review-container'}):
    user_name = review.find('span', {'class': 'display-name-link'}).text.strip()
    review_title = '\"' + review.find('a', {'class': 'title'}).text.strip() + '\"'
    review_date = review.find('span', {'class': 'review-date'}).text.strip()
    review_text = '\"' + review.find('div', {'class': ['text show-more__control', 'text show-more__control clickable']}).text.strip() + '\"'

    # if review has rating, write it to csv, else skip review
    if review.find('span', {'class': 'rating-other-user-rating'}) is not None:
      rating = review.find('span', {'class': 'rating-other-user-rating'}).text.strip()
      rating = int(rating.split('/')[0])
    else:
      continue
    writer.writerow({'user_name': user_name, 'review_title': review_title, 'review_date': review_date, 'review_text': review_text, 'rating': rating})

browser.quit()
