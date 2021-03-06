import logging
logger = logging.getLogger(__name__)

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
            PERSONA_VERIFY_URL,
            data={'assertion': assertion, 'audience': settings.DOMAIN}
        )
        if response.ok and response.json()['status'] == 'okay':
            email = response.json()['email']
            # print('response email: {}'.format(email))
            try:
                user = User.objects.get(email=email)
                # print('authentication user exists: {}'.format(user.email))
                return user
            except User.DoesNotExist:
                user = User.objects.create(email=email)
                # print('authentication new user: {}'.format(user.email))
                return user
        else:
            logger.warning(
                'Persona says no. json was: {}'.format(response.json())
            )

    def get_user(self, email):
        try:
            user = User.objects.get(email=email)
            #print('get_user: user exists: {}'.format(user.email))
            return user
        except User.DoesNotExist:
            #print('get_user: user exists: {}'.format(None))
            return None
