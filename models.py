import datetime

from django.db import models
from django.utils import timezone
#from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here

class Review(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    review_txt=models.CharField(max_length=3000)
    review_points=models.DecimalField(default=0.0, max_digits=3,
        decimal_places=1)
    
    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - 
            datetime.timedelta(days=1))
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
