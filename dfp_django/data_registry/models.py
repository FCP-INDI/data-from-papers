from django.db import models

# Create your models here.
# In the future we may want to enable a method to check
# that the entered subjects conform to what is known about
# the study, for now lets not worry about it
# class DataFromStudies(models):
    
# database table to include the links between data and papers
#  this is super-unnorm'd maybe this isn't the best way to do it??

    
  
 
class Papers(models.Model):
    cite = models.TextField()
    doi = models.CharField(max_length=200,unique=True)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.doi
 

class Studies(models.Model):
    doi = models.CharField(max_length=200,unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200)
    data_path_template = models.CharField(max_length=200,)
    
    def __str__(self):
        return "%s (%s)"%(self.name,self.doi)
    
class Data(models.Model):
    individual = models.CharField(max_length=200)
    session = models.CharField(max_length=20)
    scan_type = models.CharField(max_length=20)
    url = models.URLField(max_length=200)
    paper = models.ManyToManyField(Papers)
    study = models.ForeignKey('Studies')
      
    def __str__(self):
        return "::".join([self.individual,self.session,self.scan_type])
    
    
