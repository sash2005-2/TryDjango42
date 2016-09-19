from django.contrib import admin

# Register your models here.

#from trydjango.forms import sing_up_form
from .forms import sing_up_form
from .models import singup

class sing_up_admin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "update"]
    form = sing_up_form
    #my_form = sing_up_form
    class Meta:
        model = singup

admin.site.register(singup, sing_up_admin)