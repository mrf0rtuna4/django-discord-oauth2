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

<details>
<summary>How to get this varibles?</summary>
1. Visit https://discord.com/developers/applications

2. Create App or use any your app
3. Откройте Oauth2 в левой панели:

![image](https://github.com/user-attachments/assets/face3685-4ee8-4c9e-a706-dc634069220b)

5. Copy the CLIENT ID:

![image](https://github.com/user-attachments/assets/0e76649b-3d9b-4a5c-8744-d19fc3257d24)

7. This is your DISCORD_CLIENT_ID.
8. Press "Reset Secret" button and copy that token:

![image](https://github.com/user-attachments/assets/d2b899b3-84f4-42b0-8e4f-6a72979aaa30)

10. I'ts your DISCORD_CLIENT_SECRET.
11. Add redirect url, example:

![image](https://github.com/user-attachments/assets/d43dada4-cd0d-4cfe-bdea-39638cb0fee1)


</details>

5. Start the development server and visit `http://127.0.0.1:8000/oauth2/login/` to initiate the login process.
