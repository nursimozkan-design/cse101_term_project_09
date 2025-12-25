from vehicles import add_vehicle
from customers import register_customer, authenticate_customer
from storage import save_state, load_state
from reservations import is_available, calculate_cost

def main():
    vehicles, customers, reservations = load_state("data")
    
    while True:
        print("\n--- VEHICLE RENTAL SYSTEM ---")
        print("1. Staff Login (Add Vehicle)")
        print("2. Customer Register")
        print("3. Customer Login (Rent a Vehicle)")
        print("4. Save and Exit")
        
        choice = input("\nSelect an option: ")

        if choice == "1":
            v_id = input("Vehicle ID: ")
            make = input("Make: ")
            model = input("Model: ")
            rate = float(input("Daily Rate (e.g. 50): "))
            vehicle_data = {
                "id": v_id, 
                "make": make, 
                "model": model, 
                "status": "available", 
                "rate_per_day": rate
            }
            add_vehicle(vehicles, vehicle_data)
            
        elif choice == "2":
            name = input("Name: ")
            lic = input("License Number: ")
            pin = input("4-digit PIN: ")
            profile = {"name": name, "license_number": lic, "pin": pin}
            register_customer(customers, profile)

        elif choice == "3":
            lic = input("License Number: ")
            pin = input("PIN: ")
            user = authenticate_customer(customers, lic, pin)
            
            if user:
                print(f"\nWelcome, {user['name']}!")
                print("Available Vehicles:")
                for v in vehicles:
                    print(f"ID: {v['id']} | {v['make']} {v['model']} | Price: {v['rate_per_day']}/day | Status: {v['status']}")
                
                v_id = input("\nEnter Vehicle ID to rent: ")
                start_date = input("Start Date (YYYY-MM-DD): ")
                end_date = input("End Date (YYYY-MM-DD): ")
                
                if is_available(reservations, v_id, start_date, end_date):
                    v_rate = next((v['rate_per_day'] for v in vehicles if v['id'] == v_id), 50)
                    total = calculate_cost(start_date, end_date, v_rate)
                    
                    print("\n" + "="*30)
                    print("       RENTAL INVOICE")
                    print("="*30)
                    print(f"Customer: {user['name']}")
                    print(f"Vehicle:  {v_id}")
                    print(f"Period:   {start_date} to {end_date}")
                    print(f"Total:    ${total}")
                    print("="*30)
                    
                    confirm = input("Confirm rental? (y/n): ")
                    if confirm.lower() == 'y':
                        res_data = {
                            "vehicle_id": v_id,
                            "customer_lic": lic,
                            "start_date": start_date,
                            "end_date": end_date,
                            "total_cost": total
                        }
                        reservations.append(res_data)
                        
                        for v in vehicles:
                            if v['id'] == v_id:
                                v['status'] = 'rented'
                        
                        print("Rental successful! Vehicle status updated to rented.")
                else:
                    print("Error: Vehicle is already booked for these dates!")
            else:
                print("Login failed! Invalid license or PIN.")

        elif choice == "4":
            save_state("data", vehicles, customers, reservations)
            print("Data saved. Goodbye!")
            break

if __name__ == "__main__":
    main()