Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/gestión_de_comisiones/reports.py
class SalesReport:
    def __init__(self, sales):
        self.sales = sales

    def calculate_commission(self, commission_rate):
        commissions = []
        for sale in self.sales:
            commission = sale * commission_rate
            commissions.append(commission)
        return commissions

    def generate_report(self):
        total_sales = sum(self.sales)
        total_commissions = sum(self.calculate_commission(commission_rate))
        report = f"Total Sales: {total_sales}\nTotal Commissions: {total_commissions}"
        return report


if __name__ == "__main__":
    sales = [1000, 2000, 1500, 3000]
    commission_rate = 0.1

    sales_report = SalesReport(sales)
    report = sales_report.generate_report()
    print(report)
