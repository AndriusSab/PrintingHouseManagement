from create import create_sample_data

class PrintingHouseCLI:
    def __init__(self, printing_house):
        self.printing_house = printing_house

    def print_menu(self):
        print("Printing House Management System")
        print("Select an action:")
        print("1. Create sample data")
        print("2. Sort invoices by amount")
        print("3. Project invoice fields")
        print("4. Group invoices by customer")
        print("5. Project and group invoices")

        choice = input("Enter the number corresponding to your choice (1-5): ")

        if choice == "1":
            confirm = input("Are you sure you want to create sample data? (Y/N): ")
            if confirm.lower() == "y":
                self.create_sample_data()
                print("Sample data created.")
            else:
                print("Sample data creation cancelled.")
        elif choice == "2":
            self.print_sorted_invoices()
        elif choice == "3":
            self.print_projected_invoices()
        elif choice == "4":
            self.print_grouped_invoices()
        elif choice == "5":
            self.print_projected_and_grouped_invoices()
        else:
            print("Invalid choice. Exiting...")

    def create_sample_data(self):
            orders_collection = self.printing_house.orders_collection
            customers_collection = self.printing_house.customers_collection
            invoices_collection = self.printing_house.invoices_collection
            print_jobs_collection = self.printing_house.print_jobs_collection

            create_sample_data(
                orders_collection,
                customers_collection,
                invoices_collection,
                print_jobs_collection
            )

    def print_sorted_invoices(self):
        sorted_invoices = self.printing_house.sort_invoices_by_amount()
        print("Sorted invoices by amount:")
        for invoice in sorted_invoices:
            print(invoice)

    def print_projected_invoices(self):
        projected_invoices = self.printing_house.project_invoice_fields()
        print("Projected invoice fields:")
        for invoice in projected_invoices:
            print(invoice)

    def print_grouped_invoices(self):
        grouped_invoices = self.printing_house.group_invoices_by_customer()
        print("Grouped invoices by customer:")
        for invoice in grouped_invoices:
            print(invoice)

    def print_projected_and_grouped_invoices(self):
        result = self.printing_house.get_projecting_pipeline()
        print("Projected and grouped invoices:")
        for item in result:
            print(item)