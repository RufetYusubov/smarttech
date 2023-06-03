from django.db import models

class LaptopModel(models.Model):
    brend = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to= 'porters/')
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    destination = models.CharField(max_length=300)
    operating_system = models.CharField(max_length=200)
    prosessor = models.CharField(max_length = 200)
    ram = models.IntegerField(default=0)
    memory_size = models.IntegerField(default=0)
    videocard = models.CharField(max_length=100)
    screen_size = models.FloatField(default=0)
    bluetooth = models.BooleanField(default=True)
    wifi = models.BooleanField(default=True)
    connection = models.BooleanField(default=True)
    weight = models.FloatField(blank=True,null=True)
    warranty = models.IntegerField(default=0)
    about = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.brend
    
    class Meta:
        verbose_name = "laptop"
        verbose_name_plural = "laptops"





