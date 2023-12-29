from django.shortcuts import render,redirect
from .models import Tasks
# Create your views here.
def home(request):
    if request.method=="POST":
        task_name=request.POST.get('task_name')
        due_date=request.POST.get('due_date')
        print(task_name)
        task=Tasks(task_name=task_name,
                   due_date=due_date)
        print(task)
        task.save()
        return redirect("/")

    else:
        task=Tasks.objects.filter(is_completed=False)
        completed_task=Tasks.objects.filter(is_completed=True)
        context={"tasks":task,
                "completed_tasks":completed_task
                }

        return render(request,"home.html",context)
    
def delete(request,pk):
    task=Tasks.objects.get(pk=pk)
    task.delete()
    return redirect("/")


def mark_as_done(request,pk):
    task=Tasks.objects.get(pk=pk)
    task.is_completed=True
    task.save()
    return redirect("/")
def edittask(request,pk):
    return render(request,"edit_task.html")
    
    
