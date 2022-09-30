from django import forms 
import os
from dotenv import load_dotenv
load_dotenv() 
from django.core.mail import send_mail
class ContactForm(forms.Form):
    name = forms.CharField(max_length=35, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=400, required=True)
    inquiry = forms.CharField(max_length=150, required=False)

    def get_info(self):
        
        cleaned_data = super().clean()
        name = cleaned_data.get('name').strip()
        from_email = cleaned_data.get('email')
        msg = ''
        subject = cleaned_data.get('inquiry')
        msg = f'from {name}\n  using the mail id {from_email} \n '
        msg+=f' \n having \n{subject} \n '
        msg+=cleaned_data.get('message')

        return subject,msg

    def send(self):
        subject,msg = self.get_info()
        send_mail(
           subject=subject,
           message = msg,
           from_email=str(os.getenv('EMAIL_HOST_USER')),
           recipient_list=[str(os.getenv('RECIPIENT_ADDRESS'))]
        )
    