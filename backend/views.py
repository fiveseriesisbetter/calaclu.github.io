from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from .models import Event


def index(request):
	today = datetime.today()
	events_list = Event.objects.filter(date__gte = today).order_by("date")
	context = {'events_list': events_list}
	return render(request, 'index.html', context)


# Create your views here.
