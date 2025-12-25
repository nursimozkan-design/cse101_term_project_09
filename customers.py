def register_customer(customers, profile):
    """Registers a new customer with their profile details[cite: 42]."""
    customers.append(profile)
    print(f"Customer {profile['name']} registered successfully.")
    return profile

def authenticate_customer(customers, license_number, pin):
    """Verifies customer using license number and PIN[cite: 42]."""
    for customer in customers:
        if customer['license_number'] == license_number and customer['pin'] == pin:
            return customer
    return None