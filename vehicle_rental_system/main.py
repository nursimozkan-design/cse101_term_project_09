import os
from storage import load_data, save_data
from customers import Customer
from vehicles import Vehicle
from reservations import create_reservation, get_customer_history

def main_menu():
    base_dir = "data"
    vehicles, customers, reservations = load_data(base_dir)

    while True:
        print("\n===== VEHICLE RENTAL SYSTEM =====")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Register New Customer")
        print("4. Save and Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            admin_menu(customers, vehicles)
        elif choice == '2':
            current_customer = customer_login(customers)
            if current_customer:
                customer_menu(current_customer, vehicles, reservations)
        elif choice == '3':
            register_customer(customers)
        elif choice == '4':
            save_data(base_dir, vehicles, customers, reservations)
            print("Data saved. Goodbye!")
            break

def register_customer(customers):
    print("\n--- Register ---")
    name = input("Name: ")
    lic = input("License No: ")
    pin = input("4-digit PIN: ")
    customers.append({"name": name, "license_no": lic, "pin": pin}) 
    print("Success!")

def customer_login(customers):
    lic = input("License No: ")
    pin = input("PIN: ")
    for c in customers:
        if c.get('license_no') == lic and c.get('pin') == pin:
            return Customer(c['name'], c['license_no'], c['pin'])
    print("Login failed.")
    return None

def customer_menu(current_customer, vehicles, reservations):
    while True:
        print(f"\n--- Welcome {current_customer.name} ---")
        print("1. Rent a Vehicle")
        print("2. View History")
        print("3. Logout")
        choice = input("Option: ")
        if choice == '1':
            create_reservation(current_customer, vehicles, reservations)
        elif choice == '2':
            history = get_customer_history(current_customer.name, reservations)
            if history:
                for res in history:
                    print(f"Vehicle: {res['vehicle_id']} | Total: ${res['total_price']}")
            else:
                print("No history.")
        elif choice == '3':
            break

def admin_menu(customers, vehicles):
    print("\n1. Add Vehicle\n2. List Customers")
    choice = input("Option: ")
    if choice == '1':
        v_id = input("ID: "); brand = input("Brand: "); model = input("Model: ")
        price = float(input("Price: "))
        vehicles.append({"vehicle_id": v_id, "brand": brand, "model": model, "price_per_day": price})
    elif choice == '2':
        for c in customers: print(f"Name: {c['name']}")

if __name__ == "__main__":
    main_menu()
