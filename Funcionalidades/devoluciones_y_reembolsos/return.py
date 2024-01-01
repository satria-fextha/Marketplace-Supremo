Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/devoluciones_y_reembolsos/return.py
class ReturnPolicy:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def return_product(self, product):
        if product in self.products:
            # Check if the product is eligible for return
            if self.is_eligible_for_return(product):
                # Process the return
                self.process_return(product)
            else:
                print("Product is not eligible for return.")
        else:
            print("Product not found.")

    def is_eligible_for_return(self, product):
        # Implement your logic to determine if the product is eligible for return
        return True

    def process_return(self, product):
        # Implement your logic to process the return
        print("Processing return for product:", product)


# Example usage
return_policy = ReturnPolicy()

# Add products to the return policy
return_policy.add_product("Product 1")
return_policy.add_product("Product 2")
return_policy.add_product("Product 3")

# Return a product
return_policy.return_product("Product 2")
