filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/redes_sociales/Analytics.py
import requests

def share_on_social_media(product_url, message):
    # Replace the following placeholders with your actual social media API credentials
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'

    # Make a POST request to the social media API endpoint to share the product URL and message
    response = requests.post(
        f'https://api.socialmedia.com/share?api_key={api_key}&api_secret={api_secret}&access_token={access_token}',
        json={'product_url': product_url, 'message': message}
    )

    if response.status_code == 200:
        print('Product shared successfully on social media!')
    else:
        print('Failed to share product on social media.')

# Example usage
product_url = 'https://example.com/product/123'
message = 'Check out this amazing product!'
share_on_social_media(product_url, message)
