from django.shortcuts import render

from customapiapp.models import train
from customapiapp.serializer import trainserializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage
@csrf_exempt
def train_api_view(request,id=0):
    if request.method =='GET':
        traindata= train.objects.all()
        train_serializer = trainserializer(traindata,many=True)
        return JsonResponse(train_serializer.data,safe=False)
    elif request.method=='POST':
        trains= JSONParser().parse(request)
        train_serializer=trainserializer(data= trains)
        if train_serializer.is_valid():
            train_serializer.save()
            return JsonResponse("record added",safe=False)
    elif request.method=='PUT':
        trains=JSONParser().parse(request)
        traindata = train.objects.get(id=trains['id'])
        train_serializer=trainserializer(traindata,data=trains)
        if train_serializer.is_valid():
            train_serializer.save()
            return JsonResponse("record added",safe=False)
    elif request.method=='DELETE':
        traindata = train.objects.get(id=id)
        traindata.delete()
        return JsonResponse("record deleted",safe=False)

@csrf_exempt
def savefile(request):
    files = request.FILES['file']
    file_name=default_storage.save(files.name,file_name)
    return JsonResponse(file_name,safe=False)

