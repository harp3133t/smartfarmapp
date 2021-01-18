from django.shortcuts import render,redirect
from .models import Growth,Environment,Farm,Manage
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
    model=Manage
    fields=['pub_date','temp','DIF_AM','DIF_PM','D','N','HD','Pband','CO','Light',
            'WC','StartW','WEC','WRatio','wtype_choice','WType','RHead',
            'RLeaf','RFruit','Overload','geo_choice','Geodetic','LAI','acc_light']
    template_name_suffix='_create'
    
class EnvView(CreateView):
    model=Environment
    fields=['temp','CO','humidity','acc_light']
    template_name_suffix='_create'


    
##def growth_survey(request,farm_id):
##    farm=get_object_or_404(Farm,pk=farm_id)
##    try:
##        flower_part=farm.growth_set.get(pk=request.POST['flower_part'])
##        growpoint_shape=farm.growth_set.get(pk=request.POST['growpoint_shape'])
##        leaf_size=farm.growth_set.get(pk=request.POST['leaf_size'])
##        geodetic_form=farm.growth_set.get(pk=request.POST['geodetic_form'])
##        stem_color=farm.growth_set.get(pk=request.POST['stem_color'])
##        flower_size=farm.growth_set.get(pk=request.POST['flower_size'])
##        root_form=farm.growth_set.get(pk=request.POST['root_form'])
##        weekly_growth=farm.growth_set.get(pk=request.POST['weekly_growth'])
##    
##        fruit_load=farm.growth_set.get(pk=request.POST['fruit_load'])
##        number_bloom=farm.growth_set.get(pk=request.POST['number_bloom'])
##        growpoint_leafcolor=farm.growth_set.get(pk=request.POST['growpoint_leafcolor'])
##        flower_shape=farm.growth_set.get(pk=request.POST['flower_shape'])
##        flower_distance=farm.growth_set.get(pk=request.POST['flower_distance'])
##
##    except (KeyError, Growth.DoesNotExist):
##        return render(request,'polls/growth_survey.html',{'farm':farm,
##                                                  'error_message':"You didn't select a choice."})
##    else:
##        return HttpResponseRedirect(reverse('polls:growth',args=(farm.id,)))
