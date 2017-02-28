from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Extends User model to add profile and asymmetric relationship
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    relationships = models.ManyToManyField('self', through='Relationship',
                                           symmetrical=False,
                                           related_name='related_to')
    

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

RELATIONSHIP_FRIEND = 1
RELATIONSHIP_FAMILY = 2
RELATIONSHIP_BLOCKED = 3
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FRIEND, 'Friend'),
    (RELATIONSHIP_FAMILY, 'Family'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Relationship(models.Model):
    """
    Describe relationship between to people 
    """
    
    from_person = models.ForeignKey(Profile, related_name='from_people')
    to_person = models.ForeignKey(Profile, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
    
    def __str__(self):
        return str(self.from_person) + '_' + str(self.to_person) + '_' + str(self.get_status_display())