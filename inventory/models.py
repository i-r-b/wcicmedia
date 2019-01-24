from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Chemical(models.Model):
    name = models.CharField(max_length=256)
    atomic_weight = models.DecimalField(max_digits=10,decimal_places=3)
    cas_number = models.CharField(max_length=25,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('inventory:chemicaldet',args=[self.slug])

    class Meta:
        ordering = ['name']
        unique_together = ('name','atomic_weight')

class Bottle(models.Model):
    chemical = models.ForeignKey(Chemical,on_delete=models.CASCADE)
    company = models.CharField(max_length=256)
    catalog_number = models.CharField(max_length=256)
    base_volume = models.DecimalField(default=0.0,max_digits=10,decimal_places=3)
    lot_number = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    current_volume = models.DecimalField(default=0.0, max_digits=10,decimal_places=3)
    expiration = models.DateField(null=True,blank=True)
    recieved = models.DateField()
    recieved_by = models.ForeignKey(User,related_name='recieved_by_user',on_delete=models.CASCADE)
    date_opened = models.DateTimeField(null=True,blank=True)
    opened_by = models.ForeignKey(User,related_name='opened_by_user',blank=True,null=True, on_delete=models.CASCADE)
    date_discarded = models.DateTimeField(null=True,blank=True)
    discarded_by = models.ForeignKey(User,related_name='discarded_by_user',blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        if self.date_opened == None:
            is_opened = ['False']
        else:
            is_opened = str(self.date_opened).split()
        return self.chemical.name + " (opened: " + is_opened[0] + ") " + str(self.id)

    def get_absolute_url(self):
        return reverse('inventory:inventoryhome')


    class Meta:
        ordering = ['chemical']


class Additive(models.Model):
    bottle = models.ForeignKey(Bottle,on_delete=models.CASCADE)
    concentration = models.DecimalField(max_digits=10,decimal_places=3)
    date_made = models.DateTimeField()
    made_by = models.ForeignKey(User,on_delete=models.CASCADE)
    batchid = models.CharField(max_length=256)
    filtered = models.BooleanField()
    volume = models.DecimalField(default=0.0,max_digits=10,decimal_places=3)
    # date_discarded = models.DateTimeField(null=True,blank=True)
    # discarded_by = models.ForeignKey(User,related_name='additive_discarded_by',blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        if str(self.concentration).split(".")[1] == '000':
            stringConcentration = str(self.concentration).split(".")[0]
        else:
            stringConcentration = str(self.concentration)
        stringVersion = self.bottle.chemical.name + " (" + stringConcentration + " mg/ml)"
        return stringVersion

    def get_absolute_url(self):
        return reverse('inventory:inventoryhome')

    class Meta:
        ordering = ['bottle','concentration']
