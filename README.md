<!--
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
-->

<div align="center">
    <h1>Django & Discord Oauth2</h1>
</div>

<div align="center">
    <a href="https://badge.fury.io/py/django-discord-oauth2">
        <img src="https://badge.fury.io/py/django-discord-oauth2.svg">
    </a>
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue">
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0">
        <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
    </a>
</div>

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
       'django_discord_oauth2',
   ]
   ```

2. Include the `django_discord_oauth2` URLconf in your project `urls.py` like this:

   ```python
   from django.urls import include, path

   urlpatterns = [
       path('oauth2/', include('django_discord_oauth2.urls')),
   ]
   ```

3. Run `python manage.py migrate` to create the necessary models.

4. Add your Discord application credentials to your settings:

   ```python
   DISCORD_CLIENT_ID = 'your_client_id'
   DISCORD_CLIENT_SECRET = 'your_client_secret'
   DISCORD_REDIRECT_URI = 'your_redirect_uri'
   ```

<details>
<summary>How to get these variables?</summary>

1. Visit [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application or use an existing one.
3. Open the OAuth2 section in the left panel:

![image](https://github.com/user-attachments/assets/face3685-4ee8-4c9e-a706-dc634069220b)

5. Copy the CLIENT ID:

![image](https://github.com/user-attachments/assets/0e76649b-3d9b-4a5c-8744-d19fc3257d24)

7. This is your `DISCORD_CLIENT_ID`.
8. Press the "Reset Secret" button and copy the token:

![image](https://github.com/user-attachments/assets/d2b899b3-84f4-42b0-8e4f-6a72979aaa30)

10. This is your `DISCORD_CLIENT_SECRET`.
11. Add a redirect URL, for example:

![image](https://github.com/user-attachments/assets/d43dada4-cd0d-4cfe-bdea-39638cb0fee1)

</details>

5. Start the development server and visit `http://127.0.0.1:8000/oauth2/login/` to initiate the login process.

---

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
