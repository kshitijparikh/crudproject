from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
# Create your views here.
#Add/Show
class UserAddShowView(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stud=User.objects.all()
        context={'stu':stud,'form':fm}
        return context
    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
             fm.save()
             fm=StudentRegistration()
             return HttpResponseRedirect('/')   


# def add_show(request):
#     if request.method=='POST':
#         fm=StudentRegistration(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm=StudentRegistration() #This is done in order to generate blank form again
#     else:
#         fm=StudentRegistration()
#     stud=User.objects.all()
#     return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#Function to Edit/Update
class UserUpdateView(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'enroll/updatestudent.html',{'form':fm})
    
    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
                 fm.save()
        return render(request,'enroll/updatestudent.html',{'form':fm})
# def update_data(request,id):
#     if request.method=='POST':
#         pi=User.objects.get(pk=id)
#         fm=StudentRegistration(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#             pi=User.objects.get(pk=id)
#             fm=StudentRegistration(instance=pi)
#     return render(request,'enroll/updatestudent.html',{'form':fm})

#Function to delete
class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)

# def delete_data(request,id):
#     if request.method=='POST':
#         pi=User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')