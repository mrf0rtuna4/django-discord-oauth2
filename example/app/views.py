"""

Copyright 2024 mr_fortuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import json

from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import User
import logging

logger = logging.getLogger(__name__)


def home(request):
    user_data = request.session.get('user_data')
    print(user_data)
    return render(request, 'home.html', {'user_data': user_data})


def save_user_data(user_data):
    user, created = User.objects.update_or_create(
        discord_id=user_data['id'],
        defaults={
            'username': user_data['username'],
            'avatar': user_data.get('avatar'),
            'email': user_data.get('email'),
        }
    )
    return user


@csrf_exempt
@require_http_methods(['POST'])
def oauth2_callback(request):
    try:
        user_data = json.loads(request.body)
        logger.debug(f"User data received: {user_data}")

        # Save user data in session
        request.session['user_data'] = user_data
        request.session.permanent = True
        logger.debug(f"User data saved in session: {request.session['user_data']}")

        return JsonResponse({'user_data': user_data})
    except json.JSONDecodeError:
        logger.error("Invalid JSON received")
        return HttpResponseBadRequest('Invalid JSON')


def oauth2_error(request):
    return HttpResponseBadRequest("Authentication failed")
