from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'project.html')

def about(request):

    return render(request,'about.html')

def contact(request):
    
    value=0
    try:
        if request.method=='Post':
          name=request.Post.get['name']
          email=request.post.get['email']
          content=request.post.get['message']
          value=name+email+content
    except:
        pass

    return render(request,'contact.html',{'value':value})

def services(request):
    return render(request,'services.html')

def calculator(request):
    c=''
    try:
        if request.method=='post':
            n1=int(request.post.get('value_1'))
            n2=int(request.post.get('value_2'))
            opr=(request.post.get('opr'))

            if opr=='+':
              c=n1 + n2
            elif opr=='-':
              c=n1 - n2
            elif opr=='*':
              c=n1 * n2
            elif opr=='/':
              c=n1 / n2
    except:
        c="An error occurred"
        print(c)
    return render(request,'calculator.html',{'c':c})




