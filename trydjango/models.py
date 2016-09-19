from django.db import models

# Create your models here.
class singup(models.Model):
    email = models.EmailField(max_length=250)
    full_name = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email