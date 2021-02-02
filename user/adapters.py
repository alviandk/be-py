from django.conf import settings
from django.shortcuts import reverse, HttpResponseRedirect

from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import (
    DefaultSocialAccountAdapter,
    get_adapter
)
from allauth.account.utils import perform_login

from .models import DplUser


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)

    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user

        if user.id:
            return

        if not user.email:
            raise ImmediateHttpResponse(
                response=HttpResponseRedirect(reverse(
                    'home'
                ))
            )

        try:
            # if user exists, connect the account to the existing account and
            # login
            user = DplUser.objects.get(email=user.email)
            sociallogin.state['process'] = 'connect'
            next_url = request.GET.get('next')
            if not next_url:
                next_url = reverse('home')
            perform_login(request, user, 'none', redirect_url=next_url,
                          signal_kwargs=None, signup=False)
        except DplUser.DoesNotExist:
            pass

    def get_connect_redirect_url(self, request, socialaccount):
        """
        Returns the default URL to redirect to after successfully
        connecting a social account.
        """
        url = reverse('home')
        return url
