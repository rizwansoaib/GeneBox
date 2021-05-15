from django.db import models

# Create your models here.


class Authors(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Books(models.Model):
    AuthorName=models.ForeignKey(Authors,on_delete=models.CASCADE)
    BookName=models.CharField(max_length=100)

    def __str__(self):
        return self.BookName







