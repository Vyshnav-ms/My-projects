from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . models import Task
from .forms import TodoForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView

class TaskListview(ListView):
     model=Task
     template_name='add.html'
     context_object_name='task1'

class TaskDetailview(DetailView):
     model=Task
     template_name='details.html'
     context_object_name='task'


class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task_name','task_priority','task_date')

    def get_success_url(self):
         return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

     














def add(request):
    task1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task_name', '')  
        priority = request.POST.get('task_priority', '')  
        date=request.POST.get('task_date','')
        task = Task(task_name=name, task_priority=priority, task_date=date)
        task.save()

    return render(request, 'add.html',{'task1':task1})

# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task = Task.objects.get(id = taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')



def update(request,taskid):
    task = Task.objects.get(id = taskid)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})
