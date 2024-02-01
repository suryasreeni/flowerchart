from django.http import HttpResponse
from django.shortcuts import  render,redirect
from . models import flower
from . forms import flowerform
def index(request):
    fl=flower.objects.all()
    context={
        'flower_list':fl
    }
    return render(request,'index.html',context)
def detail(request,flower_id):
    fl=flower.objects.get(id=flower_id)
    return render(request,"detail.html",{'flower':fl})

def add_flower(request):
    if request.method=='POST':
        name=request.POST.get('name')
        sname=request.POST.get('sname')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        fl=flower(name=name,sname=sname,desc=desc,img=img)
        fl.save()

    return render(request,'add.html')

def update(request,id):
    fl=flower.objects.get(id=id)
    form=flowerform(request.POST or  None, request.FILES,instance=fl)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'flower':fl})
def delete(request,id):
    if request.method=='POST':
        fl=flower.objects.get(id=id)
        fl.delete()
        return redirect('/')
    return render(request,'delete.html')




# Create your views here.
