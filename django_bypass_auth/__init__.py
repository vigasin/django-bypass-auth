from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib import auth
from licensing.models import Account


class FakeAuthBackend(object):
    def authenticate(self, username=None, password=None, bypass=False):
        return Account.objects.get(email=username)

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None


class BypassAuthMiddleware(RemoteUserMiddleware):
    def process_request(self, request):
        user = Account.objects.get(id=1)
        request.user = user
        auth.login(request, user, backend='licensing.middleware.FakeAuthBackend')
