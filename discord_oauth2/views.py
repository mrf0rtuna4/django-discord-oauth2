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
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect

DISCORD_API_ENDPOINT = 'https://discord.com/api/v10'


def discord_login(request):
    discord_login_url = (
        f"https://discord.com/api/oauth2/authorize"
        f"?client_id={settings.DISCORD_CLIENT_ID}"
        f"&redirect_uri={settings.DISCORD_REDIRECT_URI}"
        "&response_type=code"
        "&scope=identify email"
    )
    return redirect(discord_login_url)


def discord_callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponseBadRequest('Missing code')

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.DISCORD_REDIRECT_URI,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

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
            f"Error fetching user info: {user_info_response.status_code} - {user_info_response.text}")

    user_info = user_info_response.json()

    return JsonResponse({
        'id': user_info['id'],
        'username': user_info['username'],
        'avatar': user_info['avatar'],
        'email': user_info.get('email')
    })
