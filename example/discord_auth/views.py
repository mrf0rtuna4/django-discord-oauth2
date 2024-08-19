from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import json


@csrf_exempt
def save_discord_user(request):
    if request.method == 'POST':
        try:
            user_data = json.loads(request.body)
            # Process and save user_data as needed, e.g., save to the database
            # Here you could also create or update a user model instance
            # For demonstration, we're just returning the received data
            return JsonResponse({'status': 'success', 'user_data': user_data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
