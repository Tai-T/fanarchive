from django.shortcuts import render

# import to enable super-simple index page
from django.http import HttpResponse

# super-simple index page
def index(request):
	# now with Jinja2~
	return render(request, 'fanarchive/index.jinja')