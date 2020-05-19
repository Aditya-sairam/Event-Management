from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from PIL import Image 
from ckeditor.fields import RichTextField


User = settings.AUTH_USER_MODEL
CHOICES = (('self','self'),('group','group'),('corporate','corporate'),('others','others'))

# Create your models here.
class Event(models.Model):
	full_name = models.CharField(max_length=500)
	registration_number = models.IntegerField(null=True)
	mobile_number = models.IntegerField(null=True)
	id_card = models.ImageField(upload_to='images')
	registration_type=models.CharField(max_length=100,choices=CHOICES)
	number_of_tickets = models.IntegerField(default=1)
	date_registered = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('event-detail', kwargs={'pk': self.pk})


