# Ex02 Django ORM Web Application

## Date: 28.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![er](<er diagram.jpeg>)

## DESIGN STEPS

## STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py
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


admin.py
from django.contrib import admin
from .models import BookDetails,BookDetailsAdmin
admin.site.register(BookDetails,BookDetailsAdmin)
```


## OUTPUT
![output](<Screenshot 2024-02-28 093442.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully.
