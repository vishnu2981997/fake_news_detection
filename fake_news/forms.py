from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'Confirm New Password'}))

    class Meta:
        model = User
        fields = ('password', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'Last Name'}))
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'User Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow-sm bg-white rounded', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control shadow-sm bg-white rounded'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ""
        self.fields[
            'username'].help_text = "<span class='form-text text-muted'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>"

        self.fields['password1'].widget.attrs['class'] = 'form-control shadow-sm bg-white rounded'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = "<ul class='form-text text-muted small'>" \
                                             "<li>Your password can\'t be too similar to your other personal information.</li>" \
                                             "<li>Your password must contain at least 8 characters.</li>" \
                                             "<li>Your password can\'t be a commonly used password.</li>" \
                                             "<li>Your password can\'t be entirely numeric.</li>" \
                                             "</ul>"

        self.fields['password2'].widget.attrs['class'] = 'form-control shadow-sm bg-white rounded'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields[
            'password2'].help_text = "<span class='form-text text-muted'><small>Enter the same password as before, for verification.</small></span>"
