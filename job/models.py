from django.db import models
Job_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)
# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=100)
    #location
    job_type=models.CharField(max_length=100,choices=Job_TYPE)
    description=models.CharField(max_length=100)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)

    def __str__(self):
        return self.title
