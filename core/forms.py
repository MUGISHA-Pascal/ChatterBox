from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class usercreationform(UserCreationForm):
    class meta:
        model=User
        fields =["username","password1","password2"]