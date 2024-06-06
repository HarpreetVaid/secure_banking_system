from django.db import models
import os

def profile_pic_upload_path(instance, filename):
    print(filename)
    extension = os.path.splitext(filename)[1]
    return f"profile_pics/{instance.account_no}profilepic{extension}"

def signature_upload_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return f"signatures/{instance.account_no}signature{extension}"

class Account(models.Model):
    account_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text='name')
    unique_id = models.BigIntegerField(unique=True, blank=False, null=False, help_text="unique id")
    profile_pic = models.ImageField(upload_to=profile_pic_upload_path, help_text="Profile picture")
    signature = models.ImageField(upload_to=signature_upload_path, help_text="Signature")
    balance = models.FloatField(help_text="Float number")

    def __str__(self):
        return f"Account {self.account_no} - {self.name}"
