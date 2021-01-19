from django.shortcuts import render,redirect
from .models import Growth,Farm,Manage
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

farm_id=None
# Create your views here.
class FarmListView(ListView):
    model=Farm
    def form_valid(self,form):
        farm_id=self.request.farm.id
        
class DetailView(DetailView):
    model=Farm
    success_url=reverse_lazy('index')
    context_object_name = 'farm'
    template_name='polls/detail.html'
    
class GrowthView(CreateView):
    global farm_id
    model=Growth
    fields=['pub_date','flower_part','growpoint_shape','leaf_size',
            'geodetic_form','stem_color','flower_size',
            'root_form','weekly_growth','fruit_load',
            'number_bloom','growpoint_leafcolor','flower_shape','flower_distance']
    template_name='polls/GrowthSurvey_create.html'
    context_object_name = 'farm'
    template_name_suffix='_create'
    
    def form_valid(self,form):
        form.instance.farm_id=farm_id
        if form.is_valid():
            form.instance.save()
            return redirect('/polls')
        else:
            return self.render_to_response({'form':form})

class ManageView(CreateView):
    global farm_id
    model=Manage
    fields=['pub_date','temp','DIF_AM','DIF_PM','D','N','HD','Pband','CO','Light',
            'WC','StartW','WEC','WRatio','WType','RHead',
            'RLeaf','RFruit','Overload','Geodetic','LAI','acc_light']
    template_name='polls/ManageSurvey_create.html'
    context_object_name = 'farm'
    template_name_suffix='_create'
    
    def form_valid(self,form):
        form.instance.farm_id=farm_id
        if form.is_valid():
            form.instance.save()
            return redirect('/polls')
        else:
            return self.render_to_response({'form':form})
    
