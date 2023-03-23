from django.contrib import admin
from .models import Blood_bank, Blood_doner, Division, District, Upazila
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Blood_bank)
class Blood_bankAdmin(admin.ModelAdmin):
   fields = ('user', 'name', 'contact_no', 'address_line_1', 'division', 'district', 'upazila', 'zip_code', 'country', 'is_active')

   class Media:
      js = ('addressajax.js',)

@admin.register(Blood_doner)
class Blood_donerAdmin(admin.ModelAdmin):
   fields = ('user', 'first_name', 'last_name', 'blood_group', 'contact_no', 'address_line_1', 'division', 'district', 'upazila', 'country', 'data_of_birth', 'gender', 'last_donation_date', 'is_active')

   class Media:
      js = ('addressajax.js',)

class DivisionResource(resources.ModelResource):
   class Meta:
      model = Division

@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin):
   resource_class = DivisionResource

   
class DistrictResource(resources.ModelResource):
   class Meta:
      model = District

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
   resource_class = DistrictResource


class UpazilaResource(resources.ModelResource):
   class Meta:
      model = Upazila

@admin.register(Upazila)
class UpazilaAdmin(ImportExportModelAdmin):
   resource_class = UpazilaResource