from django.contrib import admin

from users.models import Specification, User

admin.site.register(User)


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    fields = ('name', 'descriptions')




