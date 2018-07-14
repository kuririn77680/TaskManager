from django.db import models

# Create your models here.
class Task(models.Model):
    action = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    priority = models.IntegerField(unique=True, null=True)

    def __str__(self):
        '''
        String method returning self.title.
        '''
        return self.action

    def switch(self, new_priority):
        old_priority = self.priority
        self.priority = None
        self.save()
        for obj in Task.objects.all().order_by('-priority'):
            # except self object
            if obj != self:
                if obj.priority >= new_priority and obj.priority < old_priority:
                    obj.priority += 1
                obj.save()
        self.priority = new_priority
        self.save()
        return
