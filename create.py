
from datetime import datetime
from models import Customer, Order, Invoice, PrintJob

def create_sample_data(orders_collection, customers_collection, invoices_collection, print_jobs_collection):
    num_customers = int(input("Enter the number of customers: "))
    for i in range(num_customers):
        customer_id = input(f"Enter customer ID for customer {i+1}: ")
        name_surname = input(f"Enter name and surname for customer {i+1}: ")
        email = input(f"Enter email for customer {i+1}: ")
        customer = {
            'id': customer_id,
            'name_surname': name_surname,
            'contacts': {
                'email': email
            }
        }
        customers_collection.insert_one(customer)

    num_orders = int(input("Enter the number of orders: "))
    for i in range(num_orders):
        order_id = input(f"Enter order ID for order {i+1}: ")
        items = input(f"Enter items for order {i+1} (comma-separated): ").split(",")
        quantity = [int(q) for q in input(f"Enter quantities for order {i+1} (comma-separated): ").split(",")]
        price = [float(p) for p in input(f"Enter prices for order {i+1} (comma-separated): ").split(",")]
        order = {
            'id': order_id,
            'items': items,
            'quantity': quantity,
            'price': price
        }
        orders_collection.insert_one(order)

    num_invoices = int(input("Enter the number of invoices: "))
    for i in range(num_invoices):
        invoice_id = input(f"Enter invoice ID for invoice {i+1}: ")
        payment_status = input(f"Enter payment status for invoice {i+1}: ")
        invoice_amount = float(input(f"Enter invoice amount for invoice {i+1}: "))
        invoice = {
            'id': invoice_id,
            'payment_status': payment_status,
            'invoice_amount': invoice_amount
        }
        invoices_collection.insert_one(invoice)

    num_print_jobs = int(input("Enter the number of print jobs: "))
    for i in range(num_print_jobs):
        print_job_id = input(f"Enter print job ID for print job {i+1}: ")
        printing_machines = input(f"Enter printing machines for print job {i+1} (comma-separated): ").split(",")
        job_status = input(f"Enter job status for print job {i+1}: ")
        order_nr = input(f"Enter order number for print job {i+1}: ")
        print_job = {
            'print_job_id': print_job_id,
            'printing_machines': printing_machines,
            'job_status': job_status,
            'order_nr': order_nr
        }
        print_jobs_collection.insert_one(print_job)

    print("Sample data inserted successfully.")