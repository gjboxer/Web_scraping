import pandas as pd
import requests
from bs4 import BeautifulSoup

# Making a GET request
headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36' }
r = requests.get("https://webcache.googleusercontent.com/search?q=cache:https://clutch.co/web-developers", headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

Companies = []
Websites = []
Locations = []
Contacts = []
Ratings = []
Review_counts = []
Hourly_rates = []
Min_project_sizes = []
Employee_Sizes = []

Company = []
Website = []
Location = []
Contact = []
Rating = []
Review_count = []
Hourly_rate = []
Min_project_size = []
Employee_Size = []

a = soup.find({'section'}, attrs={'class': 'container'})
Companies = a.find_all('a', attrs={'class': 'company_title directory_profile'})
Websites = a.find_all('a', attrs={'class': 'website-link__item'})
Locations = a.find_all('span', attrs={'class': 'locality'})
Contacts = a.find_all('a', attrs={'class': 'provider-detail-contact'})
Ratings = a.find_all('span', attrs={'class': 'rating sg-rating__number'})
Review_counts = a.find_all('a', attrs={'class': 'reviews-link sg-rating__reviews directory_profile'})
Hourly_rates = a.find_all('div', attrs={'class': 'list-item custom_popover','data-content':"<i>Avg. hourly rate</i>"})
Min_project_sizes = a.find('div', attrs={'class': 'list-item custom_popover','data-content':"<i>Min. project size</i>"})
Employee_Sizes = a.find('div', attrs={'class': 'list-item custom_popover','data-content':"<i>Employees</i>"})

for a in Companies:
  Company.append(a.text)
for a in Websites:
  Website.append(a.get("href"))
for a in Locations:
  Location.append(a.text)
for a in Contacts:
  Contact.append(a.get("href"))
for a in Ratings:
  Rating.append(a.text)
for a in Review_counts:
  Review_count.append(a.text)
for a in Hourly_rates:
  Hourly_rate.append(a.text)
# for a in Min_project_sizes:
#   Min_project_size.append(a.text)
# for a in Employee_Sizes:
#   Employee_Size.append(a.text)



df = pd.DataFrame({'Company':Company,'Website':Website,'Location':Location,'Contact':Contact,'Rating':Rating,'Review_count':Review_count,'Hourly_rate':Hourly_rate})
df.to_csv('products.csv', index=False, encoding='utf-8')

