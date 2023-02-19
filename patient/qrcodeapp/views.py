# from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time

def qr_gen(request):
    if request.method == 'POST':
        my_dict = {}
        my_dict['name'] = request.POST['name']
        my_dict['age'] = request.POST['age']
        my_dict['phone'] = request.POST['phone']
        my_dict['gender'] = request.POST['gender']
        my_dict['company'] = request.POST['company']
        my_dict['plan'] = request.POST['plan']
        my_dict['insurance_number'] = request.POST['insurance_number']

        img = make(my_dict)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')
