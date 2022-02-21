from django.shortcuts import render

from django.http import HttpResponse
from app1.models import tablemodel

import xlwings as xw
import pandas as pd



# Create your views here.
def upload_check(request):
    if request.method == 'POST':
        tablemodel.objects.create(exel=request.FILES['exel'])
        tab=tablemodel.objects.all()
        pointer=len(tab)
        res1=tablemodel.objects.get(id=pointer)
        fielname=r'media/{}'.format(res1.exel)
        data_frame = pd.read_excel('media/{}'.format(res1.exel))
        wb = xw.Book(fielname)
        sht = wb.sheets[0].activate()
        count = 0
        for i in range(2, (len(data_frame.index) + 2)):
            print(xw.Range('D{}'.format(i)).value)
            if len(str(int(xw.Range('D{}'.format(i)).value)))!=10:
                print(len(str(int(xw.Range('D{}'.format(i)).value))))
                xw.Range('D{}'.format(i)).color = (220,20,60)
                count+=1
        wb.save(fielname)
        if count > 0:
            res=tablemodel.objects.get(id=pointer)
            return render(request, 'upload.html', {'res': res})
        else:
            res=None
            return HttpResponse('all done ...........!')

    return render(request,'upload.html')
