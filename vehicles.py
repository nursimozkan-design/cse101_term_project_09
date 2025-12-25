def add_vehicle(vehicles, vehicle_data):
    vehicles.append(vehicle_data)
    print(f"Vehicle {vehicle_data['id']} added successfully: {vehicle_data['make']} {vehicle_data['model']}")
    return vehicle_data