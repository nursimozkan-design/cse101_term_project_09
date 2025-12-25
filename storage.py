import json
import os

def save_state(base_dir, vehicles, customers, reservations):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    with open(os.path.join(base_dir, 'vehicles.json'), 'w') as f:
        json.dump(vehicles, f, indent=4)
    with open(os.path.join(base_dir, 'customers.json'), 'w') as f:
        json.dump(customers, f, indent=4)
    with open(os.path.join(base_dir, 'reservations.json'), 'w') as f:
        json.dump(reservations, f, indent=4)

def load_state(base_dir):
    try:
        with open(os.path.join(base_dir, 'vehicles.json'), 'r') as f:
            v = json.load(f)
        with open(os.path.join(base_dir, 'customers.json'), 'r') as f:
            c = json.load(f)
        with open(os.path.join(base_dir, 'reservations.json'), 'r') as f:
            r = json.load(f)
        return v, c, r
    except:
        return [], [], []