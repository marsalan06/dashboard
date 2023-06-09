from django.contrib import admin
from .models import Influencer, Business

# Register your models here.


class InfluencerAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'city', 'zip_code', 'rank', 'status')


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_no', 'start_date', 'end_date', 'reference_no','user', 'type_of_business')
    readonly_fields = ('reference_no',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('reference_no',)
        return self.readonly_fields

admin.site.register(Business, BusinessAdmin)


admin.site.register(Influencer, InfluencerAdmin)