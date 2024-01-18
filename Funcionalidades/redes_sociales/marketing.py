El filepath es: /c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/redes_sociales/marketing.py
class SocialMedia:
    def __init__(self, name):
        self.name = name

    def share_product(self, product):
        print(f"Sharing {product} on {self.name}.")

    def run_marketing_campaign(self):
        print(f"Running marketing campaign on {self.name}.")


def main():
    # Create instances of social media platforms
    facebook = SocialMedia("Facebook")
    twitter = SocialMedia("Twitter")
    instagram = SocialMedia("Instagram")

    # Share a product on social media
    product = "New Product"
    facebook.share_product(product)
    twitter.share_product(product)
    instagram.share_product(product)

    # Run marketing campaigns on social media
    facebook.run_marketing_campaign()
    twitter.run_marketing_campaign()
    instagram.run_marketing_campaign()


if __name__ == "__main__":
    main()
