from django.shortcuts import render
from django.http import HttpResponse
from .models import Area, Set

# Create your views here.
def Index(request):
    temp_name = 'index.html'
    area_list = Area.objects.all()
    set_list = Set.objects.all()

    return render(request,temp_name,{'area_list':area_list,'set_list':set_list})



def set_info(request,set_id):
    temp_name ='update_set.html'

    set_info = Set.objects.get(id=set_id)
    print(set_info)
    return render(request,temp_name,{'set_info':set_info})

def update_set_info(request,set_id):
    temp_name = 'index.html'

    user_name =request.POST.get('user_name')
    end_day = request.POST.get('end_day')
    print(set_id)
    set_id = int(set_id)
    set_obj= Set.objects.get(id = set_id)
    set_obj.user = user_name
    set_obj.counts = set_obj.counts+1


    set_obj.save()
    area_list = Area.objects.all()
    set_list = Set.objects.all()

    return render(request, temp_name,{'area_list':area_list, 'set_list':set_list})

