# Hospital Management System

A Python-based command-line application for managing patient queues in a hospital across different medical specializations.

## Project Description

The Hospital Management System is a simple yet effective tool for healthcare facilities to organize and manage patient queues. It allows hospitals to maintain patient information across 20 different medical specializations, prioritize patients based on urgency levels, and efficiently manage patient flow through the system.

## Features

- **Patient Management**: Add, view, and remove patients from the system
- **Multi-Specialization Support**: Organize patients across 20 different medical specializations
- **Priority-Based Queuing**: Patients are prioritized by urgency status (Normal, Urgent, Super Urgent)
- **Patient Tracking**: Track patient names, specialization, and urgency status
- **Capacity Management**: Each specialization can hold up to 10 patients maximum
- **Interactive Menu**: User-friendly command-line interface with menu-driven options

## Project Structure

```
hospital/
├── __init__.py           # Package initialization file
├── hospital_sys.py       # Main application with Hospital and Patient classes
├── test_data.py          # Pre-populated test data for demonstration
└── README.md             # Project documentation
```

## Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone or download the project to your local machine
2. Navigate to the project directory:
   ```bash
   cd hospital
   ```

## How to Run

Run the main program:
```bash
python hospital_sys.py
```

The application will start with a menu-driven interface displaying the following options:

```
Program Options:
1) Add new patients
2) Print all patients
3) Get next patient
4) Remove a leaving patient
5) End the program
```

## Usage Guide

### 1. Add New Patient
- Select option `1` from the menu
- Enter the specialization number (1-20)
- Enter the patient's name
- Enter the urgency status:
  - `0` = Normal
  - `1` = Urgent
  - `2` = Super Urgent

**Note**: Each specialization can accommodate a maximum of 10 patients. If a specialization is full, the system will reject new patients.

### 2. Print All Patients
- Select option `2` from the menu
- Displays all patients organized by specialization
- Shows the number of patients per specialization and their details

### 3. Get Next Patient
- Select option `3` from the menu
- Enter the specialization number
- The system will:
  - Sort patients by urgency (highest first)
  - Call the next patient to see the doctor
  - Remove the patient from the queue

### 4. Remove a Leaving Patient
- Select option `4` from the menu
- Enter the specialization number
- Enter the patient's name to be removed
- The patient will be removed from the queue

### 5. End Program
- Select option `5` to exit the application

## Code Overview

### Patient Class
```python
class Patient:
    def __init__(self, name, status, specialization)
```
Represents a single patient with:
- `name`: Patient's name
- `status`: Urgency status (0=Normal, 1=Urgent, 2=Super Urgent)
- `specialization`: Medical specialization number (1-20)

### Hospital Class
```python
class Hospital:
    def __init__(self)
```
Main management system with methods:
- `add_patient()`: Add a new patient to the system
- `print_all_patients()`: Display all patients organized by specialization
- `get_next_patient()`: Retrieve and call the next patient by priority
- `remove_leaving_patient()`: Remove a patient from the queue

### Helper Function
```python
def get_valid_input(prompt, min_val, max_val)
```
Validates user input to ensure it falls within specified range, with error handling for invalid inputs.

## Test Data

The application comes with pre-populated test data (`test_data.py`) that includes:
- 10 patients in specialization 1 with random urgency levels
- 6 patients in specialization 7 with varied urgency levels
- 3 patients in specialization 9

This test data is automatically loaded when the program runs, allowing you to immediately test all features.

## Example Usage

```
Program Options:
1) Add new patients
2) print all patients
3) Get next patient
4) Remove a leaving patient
5) End the progeam

Enter your choice(from 1 to 5): 2

Specialization 1: There are 10 patients.
Patient: pat0 is Normal
Patient: pat1 is Urgent
...

Enter your choice(from 1 to 5): 3
Enter Specialization: 1
pat1, Please go with Dr

Enter your choice(from 1 to 5): 5
```

## Future Enhancements

Potential improvements for future versions:
- Database integration for persistent data storage
- Doctor assignment to patients
- Appointment scheduling system
- Patient history tracking
- Graphical user interface (GUI)
- Export patient records to CSV/PDF

## License

This project is part of the Python Recap Udemy course applications.

## Author

Created as a learning project for hospital management system concepts in Python.
