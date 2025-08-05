from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random

# Set path to ChromeDriver (Replace this with the correct path)
CHROMEDRIVER_PATH = "./chromedriver"  # Change this to match your file location

# Initialize WebDriver with Service
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()


options.add_argument("--window-size=1920,1080")  # Set window size


driver = webdriver.Chrome(service=service, options=options)

# Open Google Search URL
search_url = "https://www.google.com/search?q=filetype:pdf+sample"

driver.get(search_url)

def load_words():
	fh = open("google-10000-english.txt", "r")
	words = fh.readlines()
	fh.close()
	for i in range(len(words)):
		if "\n" == words[i][-1]:
			words[i] = words[i][:-1]
		assert "\n" not in words[i]
	return words

index = 0
words = load_words()
time.sleep(30)
MAX_THING = 10000000
while True:

	# Wait for the page to load

	page_html = driver.page_source
	# print(page_html)

	# Do the stuff...
	
	fh = open("out/"+str(random.randrange(MAX_THING)), "w")
	fh.write(page_html)
	fh.close()

	word = random.choice(words)

	# Now do the shit...
	search_url = "https://www.google.com/search?q=filetype:pdf+"+word+"&start="+str(random.randrange(5)*10) # Do the stuff...
	print("word: "+str(word))
	driver.get(search_url)


	time.sleep(1)


	index += 1