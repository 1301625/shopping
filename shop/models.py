from django.db import models
from shopping.utils import uuid_upload_to

from django.urls import reverse
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True,upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return f'<{self.pk}> {self.name}'

    def get_absolute_url(self):
        #return reverse('shop:item_detail' , args=[self.pk]) #detail ulr에는 pk인자가 1개 필요하니까
        return reverse('shop:item_detail', kwargs={'pk':self.pk})#사전형태로 pk란 이름이로 self.pk를 넘기겠다