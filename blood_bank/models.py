from django.db import models
from accounts.models import CustomUser
from datetime import timedelta, date
from django.core.exceptions import ValidationError

# Create your models here.
class Division(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  bn_name = models.CharField(max_length=50)
  url = models.URLField()

  def __str__(self):
        return f'{self.name}'

class District(models.Model):
  id = models.AutoField(primary_key=True)
  division_id = models.ForeignKey(Division, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  bn_name = models.CharField(max_length=50)
  lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
  lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
  url = models.URLField(null=True, blank=True)

  def __str__(self):
        return f'{self.name}'

class Upazila(models.Model):
  id = models.AutoField(primary_key=True)
  district_id = models.ForeignKey(District, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  bn_name = models.CharField(max_length=50)
  url = models.URLField(null=True, blank=True)

  def __str__(self):
        return f'{self.name}'


class Blood_bank(models.Model):    

  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  contact_no = models.CharField(max_length=50)
  address_line_1 = models.CharField(max_length=500)
  upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE, blank=True, null=True)
  district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
  division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)
  zip_code = models.CharField(max_length=100, blank=True, null=True)
  country = models.CharField(max_length=100)
  is_active = models.BooleanField(default=False)

  def __str__(self):
        return f'{self.name}'


  class Meta:
    verbose_name = 'Blood Bank'
    verbose_name_plural = 'Blood Banks'

  def check_doner_exe(self, user):
    if Blood_doner.objects.filter(user = user):
      # if you'll not check for self.pk 
      # then error will also raised in update of exists model
      raise ValidationError('This email already used as doner')
    else:
       return False
     

  def save(self, *args, **kwargs):
    exe = self.check_doner_exe(self.user)
    if not exe:
      return super(Blood_bank, self).save(*args, **kwargs)


blood_choises =(
  ('A+', 'A+'),
  ('A-', 'A-'),
  ('B+', 'B+'),
  ('B-', 'B-'),
  ('O+', 'O+'),
  ('O-', 'O-'),
  ('AB+', 'AB+'),
  ('AB-', 'AB-'),
  
)

gender_choice = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
)

class Blood_doner(models.Model):

  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  blood_group = models.CharField(max_length=5, choices=blood_choises)
  contact_no = models.CharField(max_length=30)
  address_line_1 = models.CharField(max_length=500)
  upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE, blank=True, null=True)
  district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
  division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)
  country = models.CharField(max_length=100)
  data_of_birth = models.DateField()
  gender = models.CharField(max_length=15, choices=gender_choice)
  last_donation_date = models.DateField(blank=True, null=True)
  is_active = models.BooleanField(default=False)

  class Meta:
    verbose_name = 'Blood Doner'
    verbose_name_plural = 'Blood Doners'
    
  def __str__(self):
        return f'{self.user}'

  def date_count(self, days):
    target_date = date.today() - timedelta(days)
    return target_date

  def set_age(self):
    age_date = self.date_count(days=16*365)
    if self.data_of_birth < age_date:
      return True

  def set_donation_date(self):
    if self.last_donation_date == None:
      return True
    else:
      donation_period = self.date_count(days=30*2)
      if self.last_donation_date < donation_period:
        return True

  def save(self, *args, **kwargs):
    age = self.set_age()
    donation_date = self.set_donation_date()
    if age and donation_date == True:
      self.is_active = True
    else:
      self.is_active = False     
    super(Blood_doner, self).save(*args, **kwargs)