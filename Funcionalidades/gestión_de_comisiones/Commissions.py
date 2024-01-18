Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/gestión_de_comisiones/Commissions.py
class Commissions:
    def __init__(self):
        self.sales = []
        self.commission_rate = 0.1

    def add_sale(self, amount):
        commission = amount * self.commission_rate
        self.sales.append({"amount": amount, "commission": commission})

    def get_total_sales(self):
        return sum(sale["amount"] for sale in self.sales)

    def get_total_commissions(self):
        return sum(sale["commission"] for sale in self.sales)

    def generate_report(self):
        report = ""
        for sale in self.sales:
            report += f"Sale Amount: {sale['amount']}, Commission: {sale['commission']}\n"
        return report


# Example usage
commissions = Commissions()
commissions.add_sale(1000)
commissions.add_sale(2000)
commissions.add_sale(1500)

print(f"Total Sales: {commissions.get_total_sales()}")
print(f"Total Commissions: {commissions.get_total_commissions()}")
print(commissions.generate_report())
