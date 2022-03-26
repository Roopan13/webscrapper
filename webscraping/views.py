from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests

# Create your views here.
def home(request):
    url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"

    response = requests.get(url)
    #print(response.status_code)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent,'html.parser')

    titles = []
    prices = []
    images = []

    for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
        title = d.find('div',attrs={'class':'_4rR01T'})
        #print(title.string)

        price = d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
        #print(price.string)

        image = d.find('img',attrs={'class':'_396cs4 _3exPp9'})
        #print(image.get('src'))

        titles.append(title.string)
        prices.append(price.string)
        images.append(image.get('src'))

        foo = zip(titles,prices,images)

    return render(request,'webscraping/home.html',{'list':foo})

