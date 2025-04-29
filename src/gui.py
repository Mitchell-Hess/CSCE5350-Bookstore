import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from crud_operations.contact_operations import *
from crud_operations.customer_operations import *
from crud_operations.employee_operations import *
from crud_operations.inventory_operations import *
from crud_operations.management_operations import *
from crud_operations.promotion_operations import *
from crud_operations.purchase_order_operations import *
from crud_operations.review_operations import *

class BookstoreApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bookstore Management System")
        self.geometry("1000x700")

        # Create Tab Control
        tab_control = ttk.Notebook(self)
        
        # Main Tabs
        self.customer_tab = ttk.Frame(tab_control)
        self.inventory_tab = ttk.Frame(tab_control)
        self.employees_tab = ttk.Frame(tab_control)
        self.management_tab = ttk.Frame(tab_control)

        tab_control.add(self.customer_tab, text="Customer")
        tab_control.add(self.inventory_tab, text="Inventory")
        tab_control.add(self.employees_tab, text="Employees")
        tab_control.add(self.management_tab, text="Management")

        tab_control.pack(expand=1, fill="both")

        self.create_customer_tab()
        self.create_inventory_tab()
        self.create_employees_tab()
        self.create_management_tab()

    def create_customer_tab(self):
        customer_notebook = ttk.Notebook(self.customer_tab)

        # Subtabs
        search_tab = ttk.Frame(customer_notebook)
        cart_tab = ttk.Frame(customer_notebook)
        checkout_tab = ttk.Frame(customer_notebook)

        customer_notebook.add(search_tab, text="Search Books")
        customer_notebook.add(cart_tab, text="Cart")
        customer_notebook.add(checkout_tab, text="Checkout")

        customer_notebook.pack(expand=1, fill="both")

        # Search Tab
        tk.Label(search_tab, text="Search by Title, Author, ISBN, or Genre").pack(pady=10)
        self.search_entry = tk.Entry(search_tab, width=50)
        self.search_entry.pack(pady=5)

        #TODO: Add search books function
        #tk.Button(search_tab, text="Search", command=self.search_books).pack(pady=5)
        
        self.search_results = tk.Listbox(search_tab, width=100, height=20)
        self.search_results.pack(pady=10)

        #TODO: Add add to cart function
        #tk.Button(search_tab, text="Add to Cart", command=self.add_to_cart).pack(pady=5)

        # Cart Tab
        self.cart_list = tk.Listbox(cart_tab, width=100, height=20)
        self.cart_list.pack(pady=20)

        #TODO: Add remove from cart function
        #tk.Button(cart_tab, text="Remove Selected", command=self.remove_from_cart).pack(pady=5)

        # Checkout Tab
        tk.Label(checkout_tab, text="Name for Membership Discount:").pack(pady=5)
        self.name_entry = tk.Entry(checkout_tab)
        self.name_entry.pack(pady=5)

        tk.Label(checkout_tab, text="Membership ID:").pack(pady=5)
        self.membership_id_entry = tk.Entry(checkout_tab)
        self.membership_id_entry.pack(pady=5)

        #TODO: Add purchase book function
        #tk.Button(checkout_tab, text="Purchase", command=self.purchase_books).pack(pady=20)

    def create_inventory_tab(self):
        inventory_notebook = ttk.Notebook(self.inventory_tab)

        add_tab = ttk.Frame(inventory_notebook)
        manage_tab = ttk.Frame(inventory_notebook)

        inventory_notebook.add(add_tab, text="Add Book")
        inventory_notebook.add(manage_tab, text="Manage Inventory")

        inventory_notebook.pack(expand=1, fill="both")

        # Add Book Tab
        fields = ["Author's First Name", "Author's Last Name", "ISBN", "Title", "Publication Date", "Edition", "Price", "Page Count", "Description"]
        self.book_entries = {}

        for field in fields:
            frame = tk.Frame(add_tab)
            frame.pack(pady=5)
            tk.Label(frame, text=field).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=50)
            entry.pack(side=tk.LEFT)
            self.book_entries[field] = entry

        #TODO: Add add book to inventory function
        tk.Button(add_tab, text="Add Book", command=self.add_book_to_inventory).pack(pady=20)

        # Manage Inventory Tab
        tk.Label(manage_tab, text="Search by Title, Author, or ISBN").pack(pady=10)
        self.inventory_search_entry = tk.Entry(manage_tab, width=50)
        self.inventory_search_entry.pack(pady=5)

        #TODO: Add search inventory function
        #tk.Button(manage_tab, text="Search", command=self.search_inventory).pack(pady=5)

        self.inventory_results = tk.Listbox(manage_tab, width=100, height=20)
        self.inventory_results.pack(pady=10)

        #TODO: Add update and remove book functions
        #tk.Button(manage_tab, text="Update Book", command=self.update_book_info).pack(pady=5)
        #tk.Button(manage_tab, text="Remove Book", command=self.remove_book_from_inventory).pack(pady=5)

    def create_employees_tab(self):
        employees_notebook = ttk.Notebook(self.employees_tab)

        shift_tab = ttk.Frame(employees_notebook)
        membership_tab = ttk.Frame(employees_notebook)

        employees_notebook.add(shift_tab, text="Shift Check-in/out")
        employees_notebook.add(membership_tab, text="Manage Memberships")

        employees_notebook.pack(expand=1, fill="both")

        # Shift Tab
        tk.Label(shift_tab, text="Employee ID:").pack(pady=5)
        self.shift_employee_id_entry = tk.Entry(shift_tab)
        self.shift_employee_id_entry.pack(pady=5)
        
        #TODO: add check in/out functions
        #tk.Button(shift_tab, text="Check In", command=self.check_in_shift).pack(pady=20)
        #tk.Button(shift_tab, text="Check Out", command=self.check_out_shift).pack(pady=20)

        # Membership Tab
        tk.Label(membership_tab, text="Customer ID:").pack(pady=5)
        self.customer_id_entry = tk.Entry(membership_tab)
        self.customer_id_entry.pack(pady=5)

        #TODO: Add grant membership function
        #tk.Button(membership_tab, text="Grant Membership", command=self.grant_membership).pack(pady=20)

    def create_management_tab(self):
        management_notebook = ttk.Notebook(self.management_tab)

        store_tab = ttk.Frame(management_notebook)
        employee_tab = ttk.Frame(management_notebook)
        supplier_tab = ttk.Frame(management_notebook)

        management_notebook.add(store_tab, text="Store Management")
        management_notebook.add(employee_tab, text="Employee Management")
        management_notebook.add(supplier_tab, text="Supplier Management")

        management_notebook.pack(expand=1, fill="both")

        # Store Tab
        fields = ["Store ID", "Name", "Address", "Phone", "Email", "Opening Hours"]
        self.store_entries = {}

        for field in fields:
            frame = tk.Frame(store_tab)
            frame.pack(pady=5)
            tk.Label(frame, text=field).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=50)
            entry.pack(side=tk.LEFT)
            self.store_entries[field] = entry

        #TODO: Add add store button
        #tk.Button(store_tab, text="Add Store", command=self.add_store).pack(pady=20)

        # Employee Tab
        fields = ["Employee ID", "First Name", "Last Name", "Position", "Hire Date", "Salary", "Email", "Phone"]
        self.employee_entries = {}

        for field in fields:
            frame = tk.Frame(employee_tab)
            frame.pack(pady=5)
            tk.Label(frame, text=field).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=50)
            entry.pack(side=tk.LEFT)
            self.employee_entries[field] = entry

        #TODO: Add add employee function
        #tk.Button(employee_tab, text="Add Employee", command=self.add_employee).pack(pady=20)

        #TODO: Add employee functions
        # tk.Button(employee_tab, text="Edit Employee", command=self.edit_employee).pack(pady=5)
        # tk.Button(employee_tab, text="Remove Employee", command=self.remove_employee).pack(pady=5)
        # tk.Button(employee_tab, text="Schedule Shift", command=self.schedule_shift).pack(pady=5)

        # Supplier Tab
        fields = ["Supplier ID", "Name", "Contact Person", "Phone", "Email", "Lead Time Delays"]
        self.supplier_entries = {}

        for field in fields:
            frame = tk.Frame(supplier_tab)
            frame.pack(pady=5)
            tk.Label(frame, text=field).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=50)
            entry.pack(side=tk.LEFT)
            self.supplier_entries[field] = entry


        #TODO: Add supplier functions
        #tk.Button(supplier_tab, text="Add Supplier", command=self.add_supplier).pack(pady=20)
        #tk.Button(supplier_tab, text="Edit Supplier", command=self.edit_supplier).pack(pady=5)
        #tk.Button(supplier_tab, text="Remove Supplier", command=self.remove_supplier).pack(pady=5)

    def search_books(self):
        query = self.search_entry.get()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search term.")
            return

        results = search_books_by_title(query)

        self.search_results.delete(0, tk.END)
        for row in results:
            self.search_results.insert(tk.END, f"{row[0]} - {row[2]} - ${row[5]}")

    # --------- Customer Tab Helper Functions ----------

    # TODO

    # --------- Inventory Tab Helper Functions ----------

    def add_book_to_inventory(self):
        # Get user input
        author_first_name = self.book_entries["Author's First Name"].get()
        author_last_name = self.book_entries["Author's Last Name"].get()
        ISBN = self.book_entries["ISBN"].get()
        title = self.book_entries["Title"].get()
        publication_date = self.book_entries["Publication Date"].get()
        edition = self.book_entries["Edition"].get()
        price = float(self.book_entries["Price"].get())
        page_count = int(self.book_entries["Page Count"].get())
        description = self.book_entries["Description"].get()
        publisher_id = 1  # Placeholder; ideally selected from a dropdown

        try:
            book_id = create_book(ISBN, title, publication_date, edition, price, page_count, description, publisher_id)
            print("book id: ", book_id)
            author_id = find_author_id(author_first_name, author_last_name)
            print("author id: ", author_id)
            create_book_author(book_id, author_id, "primary author")
            messagebox.showinfo("Success", "Book added successfully.")
        except Exception as err:
            messagebox.showerror("Database Error", str(err))

    # TODO

    # --------- Employees Tab Helper Functions ----------

    #TODO

    # --------- Management Tab Helper Functions ----------

    #TODO


if __name__ == "__main__":
    app = BookstoreApp()
    app.mainloop()
