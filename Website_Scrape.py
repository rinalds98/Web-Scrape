from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%204814%20601201888%20601203793%20601204369%20601296707%20601301599&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2'

uClient = uReq(my_url)				#opens the URL

page_html = uClient.read()			#Reads in the data

uClient.close()						#closes the URL

page_soup = soup(page_html, 'html.parser')		#Parses the data

containers = page_soup.findAll('div', {"class":"item-container"})	#finds the item container class in the data

filename = input("Name your file: ")
f = open(filename+".csv", "w")				#opens a excel file were we will be placing all the info we need

headers = "brand, product_name, shipping, price(if available) \n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]							#finds the brand

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text								#Finds the name of the product
	
	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()						#finds shipping

	price_container = container.findAll("li",{"class":"price-current"})
	price = price_container[0].text.strip().split()
	price = "".join(price[1])											#finds the price

#	print("price: " + str(price[1]))
#	print("brand: " + brand)
#	print("product_name: " + product_name)
#	print("shipping: " + shipping)

	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "," + price + "\n")		#writes the data to the excel file

f.close()