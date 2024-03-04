from django.db import models
from django.contrib import admin
class BookDetails(models.Model):
   student_name=models.CharField(max_length=20);
   id_no=models.IntegerField();
   email=models.EmailField();
   BookName=models.CharField(max_length=100,primary_key="True");
   author_name=models.CharField(max_length=20);
   Total_page=models.IntegerField();

class BookDetailsAdmin(admin.ModelAdmin):
  list_display=("student_name","id_no","email","BookName","author_name","Total_page")
