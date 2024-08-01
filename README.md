<!--
Copyright 2023 mr_fortuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# django-discord-oauth2

> [!WARNING]
> App under development!!

## Installation

   ```bash
   pip install django-discord-oauth2
   ```

## Usage

1. Add `django_discord_oauth2` to your `INSTALLED_APPS` setting like this:

   ```python
   INSTALLED_APPS = [
       ...
       'django_discord_oauth2',
   ]
   ```

2. Include the `django_discord_oauth2` URLconf in your project `urls.py` like this:

   ```python
   path('oauth2/', include('django_discord_oauth2.urls')),
   ```

3. Run `python manage.py migrate` to create the necessary models.

4. Add your Discord application credentials to your settings:

   ```python
   DISCORD_CLIENT_ID = 'your_client_id'
   DISCORD_CLIENT_SECRET = 'your_client_secret'
   DISCORD_REDIRECT_URI = 'your_redirect_uri'
   ```

5. Start the development server and visit `http://127.0.0.1:8000/oauth2/login/` to initiate the login process.

   ```
