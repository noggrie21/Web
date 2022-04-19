from webbrowser import get
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields



class CustomUserChangeform(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name',)

