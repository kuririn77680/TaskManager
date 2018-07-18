from django.db import models


def nbr_obj():
    nbr = Task.objects.count()
    nbr = int(nbr) + 1
    return nbr

# Create your models here.
class Task(models.Model):
    action = models.CharField(max_length=255)
    # priority is auto indented function of the number of object
    priority = models.PositiveIntegerField(unique=True, null=True, default=nbr_obj)

    def __str__(self):
        '''
        String method returning self.title.
        '''
        return self.action

    # function to use when we need to change the task's priority
    def switch(self, new_priority):
        old_priority = self.priority
        self.priority = None
        self.save()
        for obj in Task.objects.all().order_by('-priority'):
            # except self object
            if obj != self:
                # change the priority of all object with priorities lower than the
                # new priority
                if obj.priority >= new_priority and obj.priority < old_priority:
                    obj.priority += 1
                obj.save()
        self.priority = new_priority
        self.save()
        return

    # function to use when task is delete/cancel or over
    def task_over(self):
        priority = self.priority
        self.delete()
        # update all action with lower priority
        for obj in Task.objects.all().order_by('-priority'):
            if obj.priority > priority:
                obj.priority -= 1
            obj.save()
