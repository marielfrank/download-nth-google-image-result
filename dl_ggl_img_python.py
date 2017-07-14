from bs4 import BeautifulSoup
import urllib.request
import os
import json

# creating a function that takes a search query and
# a desired Google image result number

# defining some stuff that both functions need... 
user_agent = "[YOUR USER AGENT]"
headers = {'User-Agent':user_agent}

# starting off with our BeautifulSoup function first
def get_soup(search_url, headers):
	page = urllib.request.Request(search_url, headers=headers)
	html = urllib.request.urlopen(page).read()
	return BeautifulSoup(html,'html.parser')

# now we get down to business
def getImg (search_query, result_number):
	## clean up the search query to add it into our url
	formatted_query = search_query.strip().replace(' ', '+')
	
	## next we create our search url
	search_url = "https://www.google.com/search?q=" + formatted_query + "&source=lnms&tbm=isch"
	
	## set browser & run search by calling BeautifulSoup
	print(f"Getting {search_query} for you. Hang on just a moment...")
	run_search = get_soup(search_url, headers)
	
	## grab the first 200 image urls and their file types
	img_list = []
	for each_image in run_search.find_all("div", {"class":"rg_meta"}):
		link, Type = json.loads(each_image.text)["ou"], json.loads(each_image.text)["ity"]
		img_list.append((link, Type))
	
	## select target url
	img_num = int(result_number) - 1
	target_img = img_list[img_num][0]
	
	## set up download location
	DIR = "[ADD YOUR DIRECTORY PATH HERE]"
	if not os.path.exists(DIR):
		DIR = os.mkdir(DIR)
	
	## download image file from url
	urllib.request.urlretrieve(target_img, DIR + target_img.split('/')[-1] + "." + Type)
	print(f"You can find the {search_query} in {DIR}. Go take a look!")
		
new_query = input("What would you like to see an image of? ")
new_result = input("Which number result would you like? (You can choose up to #200) ")
getImg(new_query, new_result)
