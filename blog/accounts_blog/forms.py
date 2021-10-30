from django.contrib.auth.forms import UserCreationForm

from accounts_blog.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "firstname",
            "lastname",
            "phone_number",
            "email",
            "email",
        )
