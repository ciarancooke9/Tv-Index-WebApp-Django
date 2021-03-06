from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


from . models import Page
from . models import Show, Genre, Actor
from . forms import Addactor_form, Addshow_form

@login_required(login_url=settings.FORCE_SCRIPT_NAME + '/accounts/login/')
def addshow_view(request, pagename='addshow'):
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	submitted = False
	if request.method == 'POST':
		form = Addshow_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print(form.errors.as_data())

			return HttpResponseRedirect(reverse('addshow') + '?submitted=True')
		else:
			print(form.errors.as_data())
	else:
		form = Addshow_form()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted,
	}

	return render(request, "addshow.html", context)

@login_required(login_url=settings.FORCE_SCRIPT_NAME + '/accounts/login/')
def addactor_view(request, pagename='addactor'):

	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	context = {
		'page_list': Page.objects.all(),
		'context': pg.bodytext, # note the end-of-line comma
	}
	submitted = False
	if request.method == 'POST':
		form = Addactor_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			print(form.errors.as_data())

			return HttpResponseRedirect(reverse('addactor') + '?submitted=True')
		else:
			print(form.errors.as_data())
	else:
		form = Addactor_form()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted,
		'name': settings.FORCE_SCRIPT_NAME,
	}
	return render(request, "addactor.html", context)



def index(request, pagename=''):
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	num_actor = Actor.objects.all().count()
	num_shows = Show.objects.all().count()
	num_genres = Genre.objects.all().count()
	ac = Actor.objects.all()
	sh = Show.objects.all()
	context = {
		'num_actor': num_actor,
		'num_shows': num_shows,
		'num_genres': num_genres,
		'title': pg.title,
		'context': pg.bodytext, # note the end-of-line comma
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
		'tv_show_list': Show.objects.all(),
		'actor_list': Actor.objects.all(),
	}
	return render(request, 'pages/page.html', context)

# Create your views here.
