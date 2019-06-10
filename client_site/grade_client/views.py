from django.shortcuts import render
from rest_framework.response import Response
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
def _url(path):
    return 'http://localhost:8010' + path

def _url1(path):
    return 'http://localhost:8020' + path

def present(name,names):

    flag = True
    for i in range(len(names)) :
        if name == names[i]:
            flag = False

    # print(flag)
    return flag


@csrf_exempt
# @api_view(['POST',])
def grades_view(request):

    courses = requests.get(_url('/get_course'))
    unique_keys=[]
    names=[]
    # print(courses.json())
    courses = courses.json()
    for course in courses:
        # if course['display_name'] not in names:
        if present(course['display_name'],names) :
            unique_keys.append(course['coursekey'])
            names.append(course['display_name'])

    if request.method == "POST" :
        index = request.POST.getlist('courseList',None)[0]
        # print(unique_keys)
        # print(index)
        # print(type(unique_keys))
        # print(type(index))
        # print(unique_keys[index])
        index = int(index)
        return HttpResponse(requests.get(_url1('/api/grade/v0/grades/'+unique_keys[index])))
    return render(request,'grade_course_list.html',{'names':names})
