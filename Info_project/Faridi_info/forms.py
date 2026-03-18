from django import forms
from .models import Information

class InformationForm(forms.ModelForm):
    class Meta:
        model=Information

        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth', 
                  'profile_picture','document_file',]
        
        label = {
            'first_name':'First Name', 'last_name':'Last Name', 'email':'Email', 'phone_number':'Phone', 
            'address':'Address', 'date_of_birth':'Date of birth', 'profile_picture':'Upload picture', 'document_file':'Upload document',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-3 px-4 w-full border-purple-400 border-2 rounded-lg focus:ring-blue-500',
                'placeholder': 'Enter your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-3 px-4 w-full border-purple-400 border-2 rounded-lg focus:ring-blue-500',
                'placeholder': 'Enter your last name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-3 px-4 w-full border-purple-400 border-2 rounded-lg focus:ring-blue-500',
                'placeholder': 'e.g. doe@gmail.com',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-3 px-4 w-full border-purple-400 border-2 rounded-lg focus:ring-blue-500',
                'placeholder': 'Enter your phone number', 'pattern':"0\d{9}", 'title':"Phone number must be 10 digits starting with 0",
                'type':'tel',
            }),
            'address': forms.TextInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-3 px-4 w-full border-purple-400 border-2 rounded-lg focus:ring-blue-500',
                'placeholder': 'e.g. City, Country',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-3 px-4 w-full border-purple-400 border-2 rounded-lg focus:ring-blue-500',
                'type': 'date',
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-2 px-4 w-full border-purple-400 border-2 rounded-lg bg-gray-100 focus:ring-blue-500',
                'accept':'image/*',
            }),
            'document_file': forms.ClearableFileInput(attrs={
                'class': 'text-md font-medium text-gray-900 py-2 px-4 w-full border-purple-400 border-2 rounded-lg bg-gray-100 focus:ring-blue-500',
                'accept': '.pdf,.doc,.docx',
            }),
        }


from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full py-3 px-4 border-purple-400 border-2 rounded-lg focus:ring-blue-500 '}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full py-3 px-4 border-purple-400 border-2 rounded-lg focus:ring-blue-500 '}), label = 'Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'enter your username', 'class':'w-full py-3 px-4 border-purple-400 border-2 rounded-lg focus:ring-blue-500 '}),
        }

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')

            if password and confirm_password and password != confirm_password:
                raise forms.ValidationError('passwords do not match')
            
            return cleaned_data

       
       
   