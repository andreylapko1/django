import os
from django.utils import timezone
from datetime import timedelta, datetime
import django
from django.db.models import Q


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()



from task_manager.models import Task, SubTask

# task = Task(
#     title="Prepare presentation",
#     description="Prepare materials and slides for the presentation",
#     status="New",
#     deadline=datetime.now() + timedelta(days=3)
# )
# task.save()
#
sub_tasks = [
    SubTask(
        title="Gather information",
        description="Find necessary information for the presentation",
        status="New",
        deadline=datetime.now() + timedelta(days=2),
        task=Task.objects.get(id=6),
    ),
    SubTask(
        title="Create slides",
        description="Create presentation slides",
        status="New",
        deadline=datetime.now() + timedelta(days=1),
        task=Task.objects.get(id=6)
    )
]

SubTask.objects.bulk_create(sub_tasks)


print(Task.objects.filter(status='new').values())
print(SubTask.objects.filter(Q(status='Done') & Q(deadline__lt=timezone.now())))

task = Task.objects.get(id=1)
task.status = 'In progress'
task.save()
print(Task.objects.filter(status='In progress').values())

subtask = SubTask.objects.get(id=1)
subtask.deadline = timezone.now() - timedelta(days=2)
subtask.save()

print(SubTask.objects.filter(id=1).values())

del_task = Task.objects.get(id=4).delete()