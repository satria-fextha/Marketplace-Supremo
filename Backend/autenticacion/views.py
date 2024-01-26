from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def create_user(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        
        if user_type == 'agricultor':
            # Create agricultor user
            # Implement logic to create agricultor user
            agricultor = Agricultor.objects.create(user=request.user)
            agricultor.save()
            
            return JsonResponse({'message': 'Agricultor user created successfully'})
        elif user_type == 'ganadero':
            # Create ganadero user
            # Implement logic to create ganadero user
            ganadero = Ganadero.objects.create(user=request.user)
            ganadero.save()
            
            return JsonResponse({'message': 'Ganadero user created successfully'})
        elif user_type == 'consumidor':
            # Create consumidor user
            # Implement logic to create consumidor user
            consumidor = Consumidor.objects.create(user=request.user)
            consumidor.save()
            
            return JsonResponse({'message': 'Consumidor user created successfully'})
        else:
            return JsonResponse({'error': 'Invalid user type'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@login_required
def read_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        # Implement logic to read user
        
        return JsonResponse({'user': user.username})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'})

@login_required
def update_user(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            # Implement logic to update user
            
            return JsonResponse({'message': 'User updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@login_required
def delete_user(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            # Implement logic to delete user
            
            return JsonResponse({'message': 'User deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

