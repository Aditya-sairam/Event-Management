from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Event
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.messages.views import SuccessMessageMixin


#from django.db.models import F
#from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import random
from django.contrib.auth.decorators import login_required

### Rest views for Chart Display ###
from rest_framework.views import APIView 
from rest_framework.response import Response

## Search Form imports ##
from .forms import PostSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

# Create your views here.

class EventCreateView(CreateView):
    model = Event
    fields = ['full_name','mobile_number','id_card','registration_type','number_of_tickets']

    #success_message = 'Your registration was successfull!'
    def form_valid(self, form):
        form.instance.registration_number = random.randint(100000,1000000)
        return super().form_valid(form)


class EventDetailView(DetailView):
    model = Event

class EventUpdateView(UpdateView):
    model = Event
    fields = ['full_name','mobile_number','id_card','registration_type','number_of_tickets']

    def form_valid(self, form):
        #form.instance.author = self.request.user
        return super().form_valid(form)

class EventDeleteView(SuccessMessageMixin,DeleteView):
    model = Event
    success_url = '/create'
    success_message = 'Your registration was cancelled!'

def HomeView(request,event_id,*args,**kwargs):
	obj1 = Event.objects.all()
	obj2 = Event.objects.get(id=event_id)
	context = {'obj1':obj1,'obj2':obj2}
	return render(request,"event/homepage.html",context)



class ChartData(APIView):

	authentication_classes = []
	permission_classes = []

	def get(self,request,format=None):
		self_count = Event.objects.filter(registration_type='self').count()
		group_count = Event.objects.filter(registration_type='group').count()
		corporate_count = Event.objects.filter(registration_type='corporate').count()
		others_count = Event.objects.filter(registration_type='others').count()
		labels = ["self-count","group-count","coroprate-count","others-count"]
		default_items = [self_count,group_count,corporate_count,others_count]
		data = {
		"labels":labels,
		"self":self_count,
		"g_count":group_count,
		"c_count":corporate_count,
		"o_count":others_count,
		"default": default_items
		}
		return Response(data)

@login_required
def chart(request,*args,**kwargs):
	obj = Event.objects.all()
	context = {'obj':obj}
	return render(request,"event/chart.html",context) 



############################Search Views########################

class ActorsFilter(BaseFilter):
    search_fields = {
        'search_text' : ['full_name',],
        'search_reg_exact' : { 'operator' : '__exact', 'fields' : ['registration_number'] },
    }

class EventSearchList(LoginRequiredMixin,SearchListView):
    model = Event
    paginate_by = 30
    template_name = "event/event_list.html"
    form_class = PostSearchForm
    filter_class = ActorsFilter