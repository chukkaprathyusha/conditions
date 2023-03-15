from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':'1000','b':'20','c':'500'}
    return render(request,"conditions.html",d)



def loops(request):
    d={'name':'prathyusha'}
    return render(request,'loops.html',context=d)