from django.db import models

# Create your models here.
class BookKeeper(models.Model):
	loginname = models.CharField(max_length=30)
	password = models.CharField(max_length=10)
	fullname = models.CharField(max_length=40)
	def __str__(self):
		return self.fullname

class Author(models.Model):
	aname = models.CharField(max_length=30)
	def __str__(self):
		return self.aname

class Publisher(models.Model):
	pname = models.CharField(max_length=30)
	def __str__(self):
		return self.pname

class Book(models.Model):
	bname = models.CharField(max_length=30)
	bcode = models.CharField(max_length=10)
	bprice = models.IntegerField(default=0)
	bauthor = models.ForeignKey(Author, on_delete=models.CASCADE)
	bpublisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	bedition = models.CharField(max_length=2)
	bstock = models.IntegerField(default=0)
	def __str__(self):
		return self.bname+" ("+self.bcode+")"
