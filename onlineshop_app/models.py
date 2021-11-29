from django.db import models

class ContactUs(models.Model):
	name = models.CharField(max_length=100)
	tel = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	info = models.TextField()

	def __str__(self):
		return self.name


class Fikrlar(models.Model):
	ism = models.CharField(max_length=100)
	fikr = models.CharField(max_length=300)

	def __str__(self):
		return self.ism