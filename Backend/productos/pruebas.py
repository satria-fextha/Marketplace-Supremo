# Models for Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add more attributes as needed

    def __str__(self):
        return self.name

# CRUD functions for Products
def create_product(name, category, price):
    product = Product(name=name, category=category, price=price)
    product.save()

def read_product(product_id):
    product = Product.objects.get(id=product_id)
    return product

def update_product(product_id, name, category, price):
    product = Product.objects.get(id=product_id)
    product.name = name
    product.category = category
    product.price = price
    product.save()

def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

# Views for API
class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logic for publishing products
def publish_product(user, name, category, price):
    if user.is_authenticated:
        create_product(name, category, price)
        return True
    return False

# Search and filter logic
def search_products(query):
    products = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
    return products

def filter_products(price_min, price_max, category=None):
    products = Product.objects.filter(price__gte=price_min, price__lte=price_max)
    if category:
        products = products.filter(category=category)
    return products
