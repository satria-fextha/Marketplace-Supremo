from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse

def register_user(request):
    if request.method == 'POST':
        # Get user data from request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Create user object
        user = User.objects.create_user(username=username, email=email, password=password)

        # Set user type based on selection
        if user_type == 'agricultor':
            user.is_agricultor = True
        elif user_type == 'ganadero':
            user.is_ganadero = True
        elif user_type == 'consumidor':
            user.is_consumidor = True

        # Save user object
        user.save()

        # Send verification email
        send_verification_email(user)

        return JsonResponse({'message': 'User registered successfully!'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def send_verification_email(user):
    # Logic to send verification email
    # You can use Django's built-in email sending functionality or a third-party library

    # Example using Django's send_mail function
    subject = 'Verify your email'
    message = f'Hi {user.username}, please click the link to verify your email.'
    from_email = 'noreply@example.com'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
