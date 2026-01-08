# cse101_term_project_09
Vehicle Rental Management System

This project is a modular Python-based terminal application designed to manage car rentals, customer data, and vehicle availability using JSON for persistent data storage.

## Setup
1. Ensure you have **Python 3.x** installed on your system.
2. Clone this repository or download the project files.
3. Make sure the `data/` folder exists with the necessary JSON files (`customers.json`, `vehicles.json`, `reservations.json`).

## Usage
1. Open your terminal or command prompt.
2. Navigate to the project directory and run:
   ```bash
   python main.py
3. Use the on-screen menu to register, login, view vehicles, and make reservations.
4. The system will automatically calculate costs and generate invoices.

 Project Progress (İlerleme)
The project was developed in three main phases to ensure stability and modularity:
Phase 1: Data Architecture: Created the storage logic using Python Dictionaries and JSON files to ensure data persistence.
Phase 2: Core Logic: Developed the reservation system, including date validation and price calculation algorithms.
Phase 3: User Experience: Implemented a clean terminal interface with table-formatted outputs and error handling.

 File Structure
main.py: Entry point and menu controller.
storage.py: Handles file I/O operations.
reservations.py: Manages booking logic and calculations.
data/: Directory containing JSON databases.
