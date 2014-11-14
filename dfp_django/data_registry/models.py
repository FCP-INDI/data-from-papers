from django.db import models

# Create your models here.
# In the future we may want to enable a method to check
# that the entered subjects conform to what is known about
# the study, for now lets not worry about it
# class DataFromStudies(models):
    
# database table to include the links between data and papers
#  this is super-unnorm'd maybe this isn't the best way to do it??
class DataFromPapers(models.Model):
    paper_cite = models.CharField(max_length=1000)
    paper_doi = models.CharField(max_length=200)
    paper_url = models.CharField(max_length=200)
    study_doi = models.CharField(max_length=200)
    data_id = models.CharField(max_length=200)
    data_url = models.CharField(max_length=200)
    
    
    
    
