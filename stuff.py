
import requests

r = requests.get('https://www.google.com')

print(r.status_code)

# Its better if we print some of the output from the site
# be more descriptive about what you're printing
print("This is the text: " + r.text)
