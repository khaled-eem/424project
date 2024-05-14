from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *

# Create your views here.
def login_page(request):
    if request.method=='POST':
        form=LoginForm(request.POST) 
        
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            
            if user:
                 login(request,user)
                 return HttpResponseRedirect(reverse('main'))
            else:
                return render(request,'app1/login.html',{
                     "message":"Inavalid Password or Username",
                     'form':LoginForm()
                })

            

        else:
                return render(request,'app1\login.html',{
                'form':LoginForm()})

    return render(request,'app1/login.html',{
                'form':LoginForm()})
    
def main_page(request):
    return render(request,'app1/main.html',{
         'tasks':Task.objects.all()
    })

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            
            return HttpResponseRedirect(reverse('login'))  
    else:
        form = RegisterForm()
        return render(request, 'app1/register.html', {'form': form})
    
    return render(request,'app1/register.html',{
         'form':RegisterForm(),
         'message':'some thing wrong',
    })

def logout_page(request):
     logout()
     return render(request,'app1/login.html',{
          'message':'Logged out',
          'form':LoginForm()
     })

def tsak_page(request,task_id):
     print(task_id)
     task1=Task.objects.get(id_task=task_id)
   
     employees=task1.employee.all()
     non_employee= Employee.objects.exclude(task=task1).all()
     #for i in employees:
      #    print(i.__str__())

     if request.method=='POST':
         task1=Task.objects.get(id_task=task_id) 
         print(task1.n_task)
         employee_id=int(request.POST['employee'])
         print(employee_id,'>>>get id')
         employee=Employee.objects.get(id_employee=employee_id)
         print(employee.n_employee,'>>>name')
         employee.task.add(task1)

         return HttpResponseRedirect(reverse('task',args=(task_id,)))
     else:
         
         return render(request,'app1/task.html',{
          'task':task1,
          'employee':employees,
          'nonEmployee':non_employee
                                        })
          

  


     

def add_page(request):

     if request.method=='POST':
          form=TaskForm(request.POST)
          if(form.is_valid):
               form.save()
               return HttpResponseRedirect(reverse('main'))
          else:
               return render(request,'app1//add.html',{
                    'TaskForm':TaskForm(),
                    'message':'Invalid data'
               })     


     return render(request,'app1//add.html',{
          'form':TaskForm()
     })


def modify_page(request,task_id):
     
     tk=Task.objects.get(id_task=task_id)
     task = get_object_or_404(Task, pk=tk.id)  
     id=task.id_task
     if request.method == 'POST':
        form = ModifyTaskForm(request.POST, instance=task)  
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('task', args=(task_id,)))  
        else:
          form = ModifyTaskForm(instance=task)  
          return render(request,'app1/modify.html',{'ModifyForm':form,'tid':task_id})
    
     return render(request,'app1/modify.html',{
         'form':ModifyTaskForm(instance=task),
         'tid':task_id
         })


def delete_task(request, id):
    task = get_object_or_404(Task, id_task=id)  # This ensures the task exists or raises a 404 error
    if request.method == 'POST':
        task.delete()
        return render(request, 'app1/main.html', {'tasks': Task.objects.all()})

#add emp to task
#d 
#modify task
#reg validation

