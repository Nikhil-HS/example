from django.contrib import admin

from basic_app.models import AccessRecord,WebPage,Topic,UserProfileInfo

admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(UserProfileInfo)
