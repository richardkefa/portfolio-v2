from django.db import models

# Create your models here.
class Projects(models.Model):
  project_name = models.CharField(max_length=50)
  description = models.TextField()
  live_link = models.CharField()
  
  
  def __str__(self):
    return self.project_name
  
  def save_project(self):
    self.save()
    
  def get_projects(cls):
    projects = cls.objects.all()
    return projects
    