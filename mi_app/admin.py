from django.contrib import admin
from mi_app.models import Topic, Webpage, AccessRecord,ToyotaLegacy, Comments
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(ToyotaLegacy)
admin.site.register(Comments)