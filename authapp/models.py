from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver


class StreamUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)


class StreamUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(
        StreamUser, unique=True, null=False, db_index=True,
        on_delete=models.CASCADE)
    tagline = models.CharField(
        verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(
        verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(
        verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=StreamUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            StreamUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=StreamUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.streamuserprofile.save()
