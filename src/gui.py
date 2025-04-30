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
        manage_books_tab = ttk.Frame(inventory_notebook)
        restock_tab = ttk.Frame(inventory_notebook)
        manage_inventory_tab = ttk.Frame(inventory_notebook)

        inventory_notebook.add(add_tab, text="Add Book to Database")
        inventory_notebook.add(manage_books_tab, text="Manage Book Database")
        inventory_notebook.add(restock_tab, text="Stock/Restock Book")
        inventory_notebook.add(manage_inventory_tab, text="Manage Inventory")

        inventory_notebook.pack(expand=1, fill="both")

        # Add Book Tab
        tk.Label(add_tab, text="Insert a Book into Database").pack(pady=10)
        tk.Label(add_tab, text="Note: Please make sure Author and Publisher exist in the database.").pack(pady=10)

        fields = ["ISBN", "Title", "Author", "Publisher", "Publication Date", "Edition", "Price", "Page Count", "Description"]
        self.book_entries = {}

        for field in fields:
            frame = tk.Frame(add_tab)
            frame.pack(pady=5)
            tk.Label(frame, text=field).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=50)
            entry.pack(side=tk.LEFT)
            self.book_entries[field] = entry

        #TODO: Add add book to book list function
        tk.Button(add_tab, text="Add Book", command=self.add_book_to_book_list).pack(pady=20)

        # Manage Book Database Tab
        tk.Label(manage_books_tab, text="Search by Title, Author, or ISBN").pack(pady=10)
        self.inventory_search_entry = tk.Entry(manage_books_tab, width=50)
        self.inventory_search_entry.pack(pady=5)

        #TODO: Add search inventory function
        tk.Button(manage_books_tab, text="Search", command=self.search_book_list).pack(pady=5)

        self.inventory_results = tk.Listbox(manage_books_tab, width=100, height=20)
        self.inventory_results.pack(pady=10)

        #TODO: Add update and remove book functions
        tk.Button(manage_books_tab, text="Update Book", command=self.update_book_info).pack(pady=5)
        tk.Button(manage_books_tab, text="Remove Book", command=self.remove_book_from_book_list).pack(pady=5)

        # Add inventory tab
        tk.Label(restock_tab, text="Stock/Restock a Book").pack(pady=10)

        fields = ["BookID", "Quantity", "Restock Date", "Location"]
        self.inventory_entries = {}

        for field in fields:
            frame = tk.Frame(restock_tab)
            frame.pack(pady=5)
            tk.Label(frame, text=field).pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=50)
            entry.pack(side=tk.LEFT)
            self.inventory_entries[field] = entry

        #TODO: Add add book to inventory function
        tk.Button(restock_tab, text="Add Book", command=self.add_book_to_inventory).pack(pady=20)

        # Manage Inventory Tab
        tk.Label(manage_inventory_tab, text="Search by Title, Author, or ISBN").pack(pady=10)
        self.inventory_search_entry = tk.Entry(manage_inventory_tab, width=50)
        self.inventory_search_entry.pack(pady=5)

        #TODO: Add search inventory function
        tk.Button(manage_inventory_tab, text="Search", command=self.search_inventory_list).pack(pady=5)

        self.inventory_results = tk.Listbox(manage_inventory_tab, width=100, height=20)
        self.inventory_results.pack(pady=10)

        #TODO: Add update and remove book functions
        tk.Button(manage_inventory_tab, text="Update Book", command=self.update_inventory_entry).pack(pady=5)
        tk.Button(manage_inventory_tab, text="Remove Book", command=self.remove_book_from_inventory).pack(pady=5)

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

    def add_book_to_book_list(self):
        # Get user input
        author_name = self.book_entries["Author"].get()
        publisher_name = self.book_entries["Publisher"]  # Placeholder; ideally selected from a dropdown
        ISBN = self.book_entries["ISBN"].get()
        title = self.book_entries["Title"].get()
        publication_date = self.book_entries["Publication Date"].get()
        edition = self.book_entries["Edition"].get()
        price = float(self.book_entries["Price"].get())
        page_count = int(self.book_entries["Page Count"].get())
        description = self.book_entries["Description"].get()

        try:
            publisher_id = find_publisher_id(publisher_name)
            book_id = create_book(ISBN, title, publication_date, edition, price, page_count, description, publisher_id)
            print("book id: ", book_id)
            author_first_name, author_last_name = author_name.split()
            author_id = find_author_id(author_first_name, author_last_name)
            print("author id: ", author_id)
            create_book_author(book_id, author_id, "primary author")
            messagebox.showinfo("Success", "Book added successfully.")
        except Exception as err:
            messagebox.showerror("Database Error", str(err))

    def search_book_list(self):
        query = self.inventory_search_entry.get().strip()

        if not query:
            messagebox.showwarning("Input Error", "Please enter a search query.")
            return

        self.inventory_results.delete(0, tk.END)

        # Try each search strategy
        results = search_books_by_isbn(query)
        if results:
            self.inventory_results.insert(tk.END, f"[ISBN] {results[0]} - {results[2]}")
            return

        results = search_books_by_title(query)
        if results:
            for row in results:
                self.inventory_results.insert(tk.END, f"[Title] {row[0]} - {row[2]}")
            return

        results = search_books_by_author(query)
        if results:
            for row in results:
                self.inventory_results.insert(tk.END, f"[Author] {row[0]} - {row[2]}")
            return

        self.inventory_results.insert(tk.END, "No results found.")

    def get_selected_book_id(self):
        try:
            selection = self.inventory_results.get(self.inventory_results.curselection())
            return int(selection.split()[1])  # Assumes format: "[Title] book_id - title"
        except Exception:
            messagebox.showwarning("Selection Error", "Please select a valid book entry.")
            return None

    def update_book_info(self):
        book_id = self.get_selected_book_id()
        if not book_id:
            return
        
        ISBN = self.book_entries["ISBN"].get()
        title = self.book_entries.get("Title", None)
        publication_date = self.book_entries["Publication Date"].get()
        edition = self.book_entries["Edition"].get()
        price = float(self.book_entries["Price"].get())
        page_count = int(self.book_entries["Page Count"].get())
        description = self.book_entries["Description"].get()
        publisher_id = 1  # Placeholder

        update_book(book_id, ISBN, title, publication_date, edition, price, page_count, description, publisher_id)
        messagebox.showinfo("Success", f"Book ID {book_id} updated.")

    def remove_book_from_book_list(self):
        book_id = self.get_selected_book_id()
        if not book_id:
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Book ID {book_id}?")
        if confirm:
            delete_book(book_id)
            self.inventory_results.delete(self.inventory_results.curselection())
            messagebox.showinfo("Deleted", f"Book ID {book_id} removed.")

    def add_book_to_inventory(self):
        book_id = self.inventory_entries["BookID"].get()
        quantity_in_stock = self.inventory_entries["Quantity"].get()
        last_restock_date = self.inventory_entries["Restock Date"].get()
        location_in_store = self.inventory_entries["Location"].get()

        try:
            create_inventory_entry(book_id, quantity_in_stock, last_restock_date, location_in_store)
            messagebox.showinfo("Success", "Book added to inventory successfully.")
        except Exception as err:
            messagebox.showerror("Database Error", str(err))
    
    def format_book_result(self, row):
        return (f"[Book ID {row[0]}] ISBN: {row[1]} | Title: {row[2]} | Date: {row[3]} | "
                f"Edition: {row[4]} | Price: ${row[5]:.2f} | Pages: {row[6]} | "
                f"Desc: {row[7]} | Publisher ID: {row[8]}")

    def search_inventory_list(self):
        query = self.inventory_search_entry.get().strip()

        if not query:
            messagebox.showwarning("Input Error", "Please enter a search query.")
            return

        self.inventory_results.delete(0, tk.END)

        # Try each search strategy
        results = search_books_by_isbn(query)
        if results:
            self.inventory_results.insert(tk.END, self.format_book_result(row))
            return

        results = search_books_by_title(query)
        if results:
            for row in results:
                self.inventory_results.insert(tk.END, self.format_book_result(row))
            return

        results = search_books_by_author(query)
        if results:
            for row in results:
                self.inventory_results.insert(tk.END, self.format_book_result(row))
            return

        self.inventory_results.insert(tk.END, "No results found.")

    def get_selected_book_id(self):
        try:
            selection = self.inventory_results.get(self.inventory_results.curselection())
            return int(selection.split()[1])  # Assumes format: "[Title] book_id - title"
        except Exception:
            messagebox.showwarning("Selection Error", "Please select a valid book entry.")
            return None

    def update_inventory_entry(self):
        book_id = self.get_selected_book_id()
        if not book_id:
            return
        
        ISBN = self.book_entries["ISBN"].get()
        title = self.book_entries.get("Title", None)
        publication_date = self.book_entries["Publication Date"].get()
        edition = self.book_entries["Edition"].get()
        price = float(self.book_entries["Price"].get())
        page_count = int(self.book_entries["Page Count"].get())
        description = self.book_entries["Description"].get()
        publisher_id = 1  # Placeholder

        update_book(book_id, ISBN, title, publication_date, edition, price, page_count, description, publisher_id)
        messagebox.showinfo("Success", f"Book ID {book_id} updated.")

    def remove_book_from_inventory(self):
        book_id = self.get_selected_book_id()
        if not book_id:
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Book ID {book_id}?")
        if confirm:
            delete_book(book_id)
            self.inventory_results.delete(self.inventory_results.curselection())
            messagebox.showinfo("Deleted", f"Book ID {book_id} removed.")

    # TODO

    # --------- Employees Tab Helper Functions ----------

    #TODO

    # --------- Management Tab Helper Functions ----------

    #TODO


if __name__ == "__main__":
    app = BookstoreApp()
    app.mainloop()
