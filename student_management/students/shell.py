from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
user=User.objects.get(username='gokul')
Token,created= Token.objects.get_or_create(user=User)
print(Token.key)