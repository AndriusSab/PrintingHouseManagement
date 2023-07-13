# Tasks:

# Set up the project repository on GitHub and initialize the project structure.

# Create a virtual environment and install the necessary dependencies, including pymongo.

# Implement a database module:

# Define the database schema using JSON schemas for each collection (orders, print jobs, inventory, customers, invoices).
# Create separate collections for orders, print jobs, inventory, customers, and invoices in MongoDB.
# Establish a connection to the MongoDB database using pymongo and handle connection errors.
# Implement data validation to ensure the integrity of the stored information.
# Implement an order management module:

# Create an Order class to handle the creation, modification, and retrieval of print job orders.
# Implement methods for adding items to an order, calculating order totals, and applying discounts.
# Validate the order data against the order schema before storing it in the orders collection.
# Handle errors such as invalid order details or duplicate orders.
# Implement a print job management module:

# Create a PrintJob class to manage the print job lifecycle, from creation to completion.
# Implement methods for assigning print jobs to printers, tracking job progress, and updating job status.
# Validate the print job data against the print job schema before storing it in the print jobs collection.
# Handle errors such as unavailable printers, invalid job assignments, or incorrect job status updates.







# Sorting: Use the $sort stage in the aggregation pipeline to sort documents based on specific fields. 
# For example, you can sort print jobs by their creation.

# Projecting Documents: Utilize the $project stage to reshape documents and include or exclude specific fields. 
# This can be helpful when generating reports or displaying specific information to users.

# Grouping Documents: Use the $group stage to group documents based on certain criteria. 
# For instance, you can group print jobs by customer or inventory items by category to analyze patterns or calculate aggregated metrics

# Combining Pipelines: Aggregation pipelines allow you to combine multiple stages together to perform complex data transformations. 
# You can chain multiple stages, such as $match, $group, and $sort, to filter, group, and sort data based on your requirements.


# The Printing House Management System is a project that aims to streamline the operations of a printing house
# by automating various tasks such as order management, print job tracking, inventory management, and customer communication.
# The project will involve capturing and processing print job orders, managing print equipment and supplies, tracking job progress,
# generating invoices, and generating reports. The project will utilize MongoDB for data storage and implement an object-oriented approach, 
# including schema validation and error handling.


#The Printing House Management:

# Program description:
# Program  that manages printing house orders, cusstomers, jobs and invoices

# use OOP implementation for MongoDB,
# pipelines aggregations


#create Printing house database,

#create collection Order with fields id,items,  quantity, price, 

#create collection Customer with fields id,  name-surname, contacts, order_id,

#create collection Invoice with fields id, payment status, invoice amount 

#create collection PrintJobs with printing machines, job status, order nr 

# task1 - sort the invoices in descending order based on the "invoice_amount" field.

# task2  project only the "customer_id", "payment_status", and "invoice_amount" fields from the invoices collection.

# task3 pipeline taht  groups invoices by the "customer_id" field and calculates the total number of invoices for each customer.

# task4   use  the above pipelines to use projecting pipeline


# Create separate branches for each module/task to allow for isolated development and testing.

# Merge the branches into the main branch after completing

from mongo_db import PrintingHouseDB
from cli import PrintingHouseCLI

def main():
    printing_house_db = PrintingHouseDB()
    cli = PrintingHouseCLI(printing_house_db)

    cli.print_menu()

if __name__ == '__main__':
    main()