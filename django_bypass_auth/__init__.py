from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()

class BypassAuthBackend(object):
    def authenticate(self, username=None, password=None, bypass=False):
        return User.objects.get(email=username)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class BypassAuthMiddleware(RemoteUserMiddleware):
    def process_request(self, request):
        user = User.objects.get(id=1)
        request.user = user
        auth.login(request, user, backend='django_bypass_auth.BypassAuthBackend')
