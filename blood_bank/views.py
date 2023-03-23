from django.shortcuts import render
from datetime import timedelta, date
from .task import send_test_email, check_user_is_active
from django.http import HttpResponse
from time import sleep
from .models import Division, Blood_doner, District, Upazila, Blood_bank, blood_choises
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
import json
# Create your views here.


def date_count(days):
    dureation = date.today() - timedelta(days)
    return dureation


def set_age():
  age_date = date_count(16*365)
  dob = date(1984, 1, 3)
  if dob < age_date:
    return True

def index(request):    
    blood_group = ['Select']
    for item in blood_choises:      
      blood_group.append(item[1])
    # print(blood_group)
    doners = Blood_doner.objects.values()
    # don = Blood_doner.objects.filter(user__email = 'foisal03@gmail.com')
    # # don = list(don)
    # # print(don)
    # if don.exists():
    #   print(True)

    # print(blood_group)
    # for doner in doners:
    #   if doner['is_active'] == False:
    #     print(doner)
    #     blood_doner = Blood_doner(doner)
        # print(blood_doner)
    # doners = Blood_doner.objects.all()
    # for doner in doners.iterator():
    #   if doner.is_active == False:        
    #     obj = Blood_doner.objects.get(id=doner.id)
    #     print(obj.first_name, obj.last_donation_date)
    #     obj.save()  

      
    # print(item.first_name)
    # day1 = date.today()
    # day2 = date(1984,1,3)
    # year = day1 - timedelta(days=56)
    # print(year)
    # if day2 <= year:
    #   print(True) 
   
  #print(user)
  # if user.is_active == True:
  #   act_user = user
    return render(request, 'index.html', {'doners' : doners, 'blood_groups' : blood_group})

def test(request):
  send_test_email.delay()
  return HttpResponse('Done')
  

def check_bd(request):
  check_user_is_active.delay()
  return HttpResponse('Done')


@login_required
def district_data(request):
    get = json.loads(request.body)
    division = get['id']
    district = {}
    if division:
        districts = District.objects.filter(division_id__id = division)
        district = {pp.name: pp.id for pp in districts}
    return JsonResponse(data=district, safe=False)


@login_required
def upazila_data(request):
    get = json.loads(request.body)
    district = get['id']
    upazila = {}
    if district:
        upazilas = Upazila.objects.filter(district_id__id = district)
        upazila = {pp.name: pp.id for pp in upazilas}
    return JsonResponse(data=upazila, safe=False)


def searchresult(request):
   if request.method == 'POST':
      blood = request.POST.get('blood_group')
      location = request.POST.get('location')
      doners = Blood_doner.objects.filter(blood_group=blood, division__name = location)
      print(doners)
      return render(request, 'result.html', {'doners' : doners})
      