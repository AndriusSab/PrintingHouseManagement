class PrintingHouse:
    def __init__(self):
        self.orders_collection = []
        self.customers_collection = []
        self.invoices_collection = []
        self.print_jobs_collection = []

class Order:
    def __init__(self, order_id, customer_id, print_job_ids):
        self.order_id = order_id
        self.customer_id = customer_id
        self.print_job_ids = print_job_ids

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class Invoice:
    def __init__(self, invoice_id, order_id, amount, issued_date):
        self.invoice_id = invoice_id
        self.order_id = order_id
        self.amount = amount
        self.issued_date = issued_date

class PrintJob:
    def __init__(self, print_job_id, order_id, file_name, print_date):
        self.print_job_id = print_job_id
        self.order_id = order_id
        self.file_name = file_name
        self.print_date = print_dat