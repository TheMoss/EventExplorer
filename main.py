import requests
import datetime

date = input("Write which day would you like to check (in MM/DD format) or \"today\" to use current date: ")

if date == "today":
  today = datetime.datetime.now()
  date = today.strftime('%m/%d')

url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date

response = requests.get(url)
#The response is encoded to JSON
data = response.json()
print(data)