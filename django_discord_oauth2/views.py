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

import requests
from django.conf import settings
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

DISCORD_API_ENDPOINT = 'https://discord.com/api/v10'


def discord_login(request):
    redirect_uri = request.build_absolute_uri(reverse('discord_callback'))
    discord_login_url = (
        f"https://discord.com/api/oauth2/authorize"
        f"?client_id={settings.DISCORD_CLIENT_ID}"
        f"&redirect_uri={redirect_uri}"
        "&response_type=code"
        "&scope=identify email"
    )
    return redirect(discord_login_url)


@csrf_exempt
def discord_callback(request):
    if 'error' in request.GET or 'code' not in request.GET:
        return HttpResponseBadRequest('Error: Missing or invalid code parameter')

    code = request.GET['code']
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': request.build_absolute_uri(reverse('discord_callback')),
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(
        f'{DISCORD_API_ENDPOINT}/oauth2/token',
        data=data,
        headers=headers,
        auth=(settings.DISCORD_CLIENT_ID, settings.DISCORD_CLIENT_SECRET)
    )
    if response.status_code != 200:
        print('Error fetching token:', response.text)
        return HttpResponseBadRequest(f"Error fetching token: {response.status_code} - {response.text}")

    tokens = response.json()
    access_token = tokens.get('access_token')
    if not access_token:
        return HttpResponseBadRequest('No access token received')

    user_info_response = requests.get(
        f'{DISCORD_API_ENDPOINT}/users/@me',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    if user_info_response.status_code != 200:
        print('Error fetching user info:', user_info_response.text)
        return HttpResponseBadRequest(
            f"Error fetching user info: {user_info_response.status_code} - {user_info_response.text}"
        )

    user_info = user_info_response.json()
    user_data = {
        'id': user_info['id'],
        'username': user_info['username'],
        'avatar': user_info['avatar'],
        'email': user_info.get('email')
    }

    # Post the user data to another endpoint if configured
    if hasattr(settings, 'DISCORD_POST_URL'):
        post_response = requests.post(settings.DISCORD_POST_URL, json=user_data)
        if post_response.status_code != 200:
            try:
                error_details = post_response.json()
            except json.JSONDecodeError:
                error_details = post_response.text
            return HttpResponseBadRequest(
                json.dumps({
                    'status_code': post_response.status_code,
                    'error': error_details
                }),
                content_type='application/json'
            )
        return redirect(settings.DISCORD_POST_URL)

    return JsonResponse(user_data)
