from .models import Division, Blood_doner
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from blood_doner import settings


@shared_task(bind=True)
def send_test_email(self):
  users = get_user_model().objects.all()
  for user in users:
    mail_subject = 'Celery Test'
    text = 'This is celery test'
    to_email = user.email
    print(user)
    send_mail(
      subject = mail_subject,
      message = text,
      from_email = settings.EMAIL_HOST_USER,
      recipient_list = [to_email],
      fail_silently = True,
    )
  return 'Done'


@shared_task(bind=True)
def check_user_is_active(self):
  doners = Blood_doner.objects.all()
  for doner in doners.iterator():
      if doner.is_active == False:        
        obj = Blood_doner.objects.get(id=doner.id)
        obj.last_donation_date = doner.last_donation_date
        obj.save()
  return 'Done'