from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import PyPDF2

# Create your views here.

def Home(request):
    return render(request,'Home.html')

import os

def Upload(request):
    if request.method == 'POST':
        myfile = request.FILES['file'] 
        file_name = myfile.name
        file_path = os.path.join('Artist\\pdf-safe', file_name) 
        
        with open(file_path, 'wb') as file:
            for chunk in myfile.chunks():
                file.write(chunk) 


        text = ''
        

        file_obj = open(file_path,'rb')

        file = PyPDF2.PdfReader(file_obj)

        page = file.pages[0]

        for page_num,page in enumerate (file.pages):
            text += ('Page Number : ' + str(page_num+1))
            text += page.extract_text()   
        return JsonResponse({'text': text})
    else:
        return JsonResponse({'text':"OCR isn't possible for this PDF - AI"})