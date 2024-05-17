from django.contrib import admin

from htmlwebsite.models import Contact, Nominee, Voterdetails, signin, signup

# Register your models here.

admin.site.register(Contact)

admin.site.register(Voterdetails)

admin.site.register(signin)

admin.site.register(signup)

admin.site.register(Nominee)