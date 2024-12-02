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

# django-discord-oauth2

[![PyPI Version](https://img.shields.io/pypi/v/django-discord-oauth2)](https://pypi.org/project/django-discord-oauth2/)
[![License](https://img.shields.io/pypi/l/django-discord-oauth2)](https://opensource.org/licenses/Apache-2.0)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-discord-oauth2)](https://pypi.org/project/django-discord-oauth2/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/django-discord-oauth2/test.yml)](https://github.com/mrf0rtuna4/django-discord-oauth2/actions)

> ⚠ **Warning:**  
> This package is under active development. Use with caution in production environments.

---

## Overview

`django-discord-oauth2` is a Django app that simplifies integrating Discord's OAuth2 authentication. It provides a ready-to-use OAuth2 flow to authenticate users with their Discord accounts.

### 🚨 Important Note on CSRF and Security  
While handling OAuth tokens, be cautious about CSRF vulnerabilities. CSRF protection may sometimes block unsafe token handling methods, especially when passing tokens directly to the database. It is essential to follow best practices by using secure storage and transmission methods for tokens.

---

## Installation

Install the package via pip:

```bash
pip install django-discord-oauth2
```

---

## Usage

### Step 1: Add to Installed Apps  
Add `django_discord_oauth2` to your Django `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django_discord_oauth2',
    # other apps
]
```

### Step 2: Configure URLs  
Include the app’s URL configuration in your project’s `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    path('oauth2/', include('django_discord_oauth2.urls')),
    # other paths
]
```

### Step 3: Apply Migrations  
Run the following command to create the necessary database models:

```bash
python manage.py migrate
```

### Step 4: Set Environment Variables  
Add your Discord application's credentials in `settings.py`:

```python
DISCORD_CLIENT_ID = 'your_client_id'
DISCORD_CLIENT_SECRET = 'your_client_secret'
DISCORD_REDIRECT_URI = 'your_redirect_uri'
```

---

<details>
<summary>📜 How to Get Discord Credentials</summary>

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application or use an existing one.
3. Navigate to the **OAuth2** tab:
   
   ![OAuth2 Tab](https://github.com/user-attachments/assets/face3685-4ee8-4c9e-a706-dc634069220b)

4. Copy your **Client ID**:

   ![Client ID](https://github.com/user-attachments/assets/0e76649b-3d9b-4a5c-8744-d19fc3257d24)

5. Click "Reset Secret" and copy the generated token:

   ![Client Secret](https://github.com/user-attachments/assets/d2b899b3-84f4-42b0-8e4f-6a72979aaa30)

6. Add a redirect URI matching your application:

   ![Redirect URI](https://github.com/user-attachments/assets/d43dada4-cd0d-4cfe-bdea-39638cb0fee1)

</details>

---

### Step 5: Start the Server  
Run the development server and initiate the login process at:

```
http://127.0.0.1:8000/oauth2/login/
```

---

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!

---

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more information.