FILEPATH: /c:/Users/jorge/OneDrive/Escritorio/Marketplace/aplicaciones/administración/admin.py
import users
import products
import orders
import analytics

class AdminPanel:
    def __init__(self):
        self.user_manager = users.UserManager()
        self.product_manager = products.ProductManager()
        self.order_manager = orders.OrderManager()
        self.analytics_tool = analytics.AnalyticsTool()

    def manage_users(self):
        self.user_manager.manage()

    def manage_products(self):
        self.product_manager.manage()

    def manage_orders(self):
        self.order_manager.manage()

    def monitor_performance(self):
        self.analytics_tool.monitor()

admin_panel = AdminPanel()
