Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/gestión_de_comisiones/Payments.py
class Payments:
    def __init__(self):
        self.sales = []
        self.commission_rate = 0.1

    def make_sale(self, amount):
        commission = amount * self.commission_rate
        self.sales.append({"amount": amount, "commission": commission})

    def get_total_sales(self):
        return sum(sale["amount"] for sale in self.sales)

    def get_total_commission(self):
        return sum(sale["commission"] for sale in self.sales)

    def generate_report(self):
        report = "Sales Report:\n"
        report += f"Total Sales: ${self.get_total_sales()}\n"
        report += f"Total Commission: ${self.get_total_commission()}\n"
        return report


# Example usage
payments = Payments()
payments.make_sale(1000)
payments.make_sale(2000)
payments.make_sale(1500)

print(payments.generate_report())
