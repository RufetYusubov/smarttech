from django.db import models
from django.contrib.auth.models import User

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

    
    class Meta:
        verbose_name = "laptop"
        verbose_name_plural = "laptops"


    def __str__(self):
        return self.brend
    
  
#----------------------------------------------------------------------------------
class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="user_comments")
    laptop = models.ForeignKey(LaptopModel, on_delete = models.CASCADE, blank=True, null=True, related_name="laptop_comments")
    parent = models.ForeignKey("self",on_delete = models.CASCADE,blank=True,null=True, related_name="replies")
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "comment"
        ordering = ("id",)

    def __str__(self) -> str:
        return self.user.username + " " + str(self.id)





