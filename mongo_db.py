from pymongo import MongoClient

class PrintingHouseDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['printing_house_db']
        self.orders_collection = self.db['orders']
        self.customers_collection = self.db['customers']
        self.invoices_collection = self.db['invoices']
        self.print_jobs_collection = self.db['print_jobs']
        
    def sort_invoices_by_amount(self):
        criteria = {"invoice_amount": 1}
        pipeline = [{"$sort": criteria}]
        return self.invoices_collection.aggregate(pipeline)
    
    def project_invoice_fields(self):
        pipeline = [
            {"$project": {
                "customer_id": 1,
                "payment_status": 1,
                "invoice_amount": 1
            }}
        ]
        return self.invoices_collection.aggregate(pipeline)
    
    def group_invoices_by_customer(self):
        pipeline = [
            {"$group": {
                "_id": "$customer_id",
                "total_invoices": {"$sum": 1}
            }}
        ]
        return self.invoices_collection.aggregate(pipeline)
    
    def get_projecting_pipeline(self):
        pipeline = [
            {"$sort": {"invoice_amount": -1}},
            {"$project": {
                "customer_id": 1,
                "payment_status": 1,
                "invoice_amount": 1
            }},
            {"$group": {
                "_id": "$customer_id",
                "total_invoices": {"$sum": 1}
            }}
        ]
        return self.invoices_collection.aggregate(pipeline)
    
