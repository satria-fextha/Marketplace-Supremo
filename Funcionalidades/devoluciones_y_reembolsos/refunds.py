Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/devoluciones_y_reembolsos/refunds.py
from datetime import datetime

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class RefundPolicy:
    def __init__(self):
        # Initialize refund policy criteria and settings
        self.return_days = 30
        self.refund_threshold = 100

    def check_eligibility(self, product, purchase_date):
        # Check if the product is eligible for a refund based on criteria
        days_since_purchase = (datetime.now() - purchase_date).days
        if days_since_purchase <= self.return_days:
            return True
        return False

    def process_refund(self, product, purchase_date):
        # Process the refund for an eligible product
        if self.check_eligibility(product, purchase_date):
            if product.price <= self.refund_threshold:
                # Process refund directly
                return "Refund processed successfully."
            else:
                # Coordinate return with the seller
                return "Return coordination initiated."
        else:
            return "Product is not eligible for a refund."

# Example usage
refund_policy = RefundPolicy()
product = Product("Example Product", 50)  # Replace with your product details
purchase_date = datetime(2022, 1, 1)  # Replace with the actual purchase date

refund_status = refund_policy.process_refund(product, purchase_date)
print(refund_status)
