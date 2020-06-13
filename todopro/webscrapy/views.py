from django.shortcuts import render

#from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

# Create your views here.
SCRAPY_URL = 'https://losangeles.craigslist.org/search/?query={}'

def scrapyprocess(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    final_url = SCRAPY_URL.format(quote_plus(search))
    print(final_url)
    #soup = BeautifulSoup(page.content, 'html.parser')
    response = requests.get(final_url)


    return render(request,'webscrapy/scrapyprocess.html',{'search':response})
