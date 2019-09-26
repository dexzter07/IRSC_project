from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .models import Hotels
# Create your views here.
def index(request):
    hotel = Hotels.objects.all()
    return render(request,"hotels/base.html", {'hotel': hotel})

def state(request, template_name='base.html'):

    if request.GET.get('search'):
        search_filter = request.GET.get('search')
        hotels = Hotels.objects.filter(search_choice=search_filter)

    else:
        hotels = Hotels.objects.all()

    context_dict = {'hotels':hotels}
    return render(request, template_name, context_dict)



