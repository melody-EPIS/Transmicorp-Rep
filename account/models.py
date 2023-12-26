from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


#class Interest(models.Model):
	#name = models.CharField(max_length=80, unique=True, verbose_name='Nombre')

	#class Meta:
		#verbose_name = 'Interés'
		#verbose_name_plural = 'Intereses'
		#ordering = ['name']

	#def __str__(self):
		#return self.name



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	nombres = models.CharField(max_length=80, null=True, blank=True)
	apellidos = models.CharField(max_length=80, null=True, blank=True)
	location = models.CharField(max_length=80, null=True, blank=True)
	image = models.ImageField(default='', upload_to='users/')
	location = models.CharField(max_length=80, null=True, blank=True)
	bio = models.TextField(max_length=400, null=True, blank=True)
	age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(150)])
	email = models.EmailField(max_length=255, null=True, blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)
	puestoTrabajo = models.CharField(max_length=80, null=True, blank=True)
	#interests = models.ManyToManyField(Interest, verbose_name='Intereses'

	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfiles'
		ordering = ['-id']
            

	


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)