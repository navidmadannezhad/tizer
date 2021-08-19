from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput

class EmailForm(forms.Form):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}), error_messages={'required': 'لطفا نام خود را وارد کنید'})
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'placeholder': 'ایمیل (در جایی منتشر نخواهد شد)'}), error_messages={'required': 'لطفا ایمیل خود را وارد کنید', 'invalid': 'لطفا یک ایمیل معتبر وارد کنید'})
    subject = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'موضوع پیام'}), error_messages={'required': 'لطفا موضوع پیام خود را وارد کنید'})
    message = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder': 'متن پیام'}), error_messages={'required': 'لطفا پیام خود را بنویسید'})

    captcha = CaptchaField(label=False, widget=CaptchaTextInput(attrs={'placeholder': 'لطفا متن تصویر را وارد کنید'}), error_messages={'required': 'لطفا متن تصویر را وارد کنید', 'invalid': 'متن تصویر صحیح وارد نشده است'})
