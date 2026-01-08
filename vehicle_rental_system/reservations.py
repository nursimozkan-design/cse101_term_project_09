import datetime

def create_reservation(current_customer, vehicles, reservations):
    v_id = input("Enter Vehicle ID to rent: ")
    vehicle = next((v for v in vehicles if v['vehicle_id'] == v_id), None)
    
    if not vehicle:
        print("Vehicle not found!")
        return

    try:
        start_str = input("Start Date (YYYY-MM-DD): ")
        end_str = input("End Date (YYYY-MM-DD): ")
        
        start_date = datetime.datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_str, "%Y-%m-%d")
        days = (end_date - start_date).days
        
        if days <= 0:
            print("Error: End date must be after start date!")
            return

        total = days * vehicle['price_per_day']
        
        print("\n" + "="*35)
        print("          RENTAL INVOICE")
        print("="*35)
        print(f"Customer: {current_customer.name}")
        print(f"Vehicle:  {vehicle['brand']} {vehicle['model']}")
        print(f"Period:   {start_str} to {end_str} ({days} days)")
        print(f"Total:    ${total}")
        print("="*35)
        
        confirm = input("Confirm rental? (y/n): ")
        if confirm.lower() == 'y':
            new_res = {
                "customer": current_customer.name,
                "vehicle_id": v_id,
                "start_date": start_str,
                "end_date": end_str,
                "total_price": total
            }
            reservations.append(new_res)
            print("Rental successful! Transaction recorded.")
        else:
            print("Rental cancelled.")

    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")

def get_customer_history(customer_name, reservations):
    """Müşterinin geçmiş kiralamalarını filtreler."""
    return [res for res in reservations if res['customer'] == customer_name]