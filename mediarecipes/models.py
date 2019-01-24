from django.db import models
from django.urls import reverse
from django.conf import settings
from django.forms import ModelForm
# Create your models here.


from django.contrib.auth import get_user_model
from inventory.models import Chemical
User = get_user_model()

CONTAINER_CHOICES =(
    ('a','Split Plate'),
    ('b','Thin Plate'),
    ('c','Thick Plate'),
    ('d','Plant Con'),
    ('e','Sundae Cup'),
    ('f','other')
)

UNIT_CHOICES =(
    ('1','g'),
    ('2','mg'),
    ('3','ug'),
    ('4','M'),
    ('5','mM'),
    ('6','uM'),
)

ACID_BASE_CHOICES =(
    ('1','KOH'),
    ('2','NaOH'),
    ('3','HCl'),
)


class Recipe(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    name = models.CharField(max_length=256)
    container = models.CharField(max_length=100,choices=CONTAINER_CHOICES)
    recipe_id = models.CharField(max_length=4,unique=True)
    comments = models.TextField()

    def __str__(self):
        return str(self.recipe_id) + "-" + str(self.name)

    class Meta:
        ordering = ['recipe_id']


class Request(models.Model):
    media_recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    volume = models.IntegerField()
    number_requested = models.IntegerField()
    requested_by = models.ForeignKey(User,related_name='requested_by_user',on_delete=models.CASCADE)
    date_requested = models.DateTimeField()
    date_needed = models.DateField()
    initial_comments = models.TextField(max_length=180)
    completed = models.BooleanField(default=False)
    cancelled_by = models.ForeignKey(User,related_name='cancelled_by_user',on_delete=models.CASCADE,null=True,blank=True)
    date_cancelled = models.DateTimeField(null=True,blank=True)
    batchid = models.CharField(max_length=150,blank=True)
    container = models.CharField(max_length=150,blank=True)
    volume_made = models.IntegerField(null=True,blank=True)
    number_made = models.IntegerField(null=True,blank=True)
    total_volume_made = models.IntegerField(null=True,blank=True)
    made_by = models.ForeignKey(User,related_name='made_by_user',on_delete=models.CASCADE,null=True,blank=True)
    date_made = models.DateTimeField(null=True,blank=True)
    final_recipe = models.TextField(max_length=180,blank=True)
    final_comments = models.TextField(max_length=180,blank=True)
    number_contaminated = models.IntegerField(null=True,blank=True)
    date_contamination_found = models.DateField(null=True,blank=True)
    number_wasted = models.IntegerField(null=True,blank=True)
    date_wasted = models.DateField(null=True,blank=True)
    waste_comments = models.TextField(max_length=180,blank=True)

    def __str__(self):
        return 'REQ'+str(self.pk)


class Step(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    number = models.IntegerField()

class ReagentStep(Step):
    ingredient = models.ForeignKey(Chemical,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=3)
    unit = models.TextField(choices=UNIT_CHOICES)

class pHStep(Step):
    ingredient = models.TextField(choices=ACID_BASE_CHOICES)
    ph_to = models.DecimalField(max_digits=4, decimal_places=2)

class SterilizeStep(Step):
    sterilize = models.TextField(choices=(('1','Autoclave for 25 minutes'),('2','Filter Sterilize')))
