
import requests

r = requests.get('https://www.google.com')

print(r.status_code)

# Its better if we print some of the output from the site

print(r.text)
