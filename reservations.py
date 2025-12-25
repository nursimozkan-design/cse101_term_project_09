from datetime import datetime

def is_available(reservations, vehicle_id, start_date_str, end_date_str):
    """Checks if the vehicle is available for the requested period."""
    new_start = datetime.strptime(start_date_str, "%Y-%m-%d")
    new_end = datetime.strptime(end_date_str, "%Y-%m-%d")

    for res in reservations:
        if res['vehicle_id'] == vehicle_id:
            res_start = datetime.strptime(res['start_date'], "%Y-%m-%d")
            res_end = datetime.strptime(res['end_date'], "%Y-%m-%d")
            
            if not (new_end < res_start or new_start > res_end):
                return False 
    return True  

def calculate_cost(start_date_str, end_date_str, daily_rate):
    """Calculates total rental price based on days."""
    start = datetime.strptime(start_date_str, "%Y-%m-%d")
    end = datetime.strptime(end_date_str, "%Y-%m-%d")
    days = (end - start).days
    if days <= 0: days = 1  
    return days * daily_rate