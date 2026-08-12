def get_valid_input(prompt, min_val, max_val):
    """Reusable method for getting validated integer input"""
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val 
            print(f'Not valid. Enter value between {min_val} and {max_val}')
        except ValueError:
            print('please enter a valid number')

class Patient: 
    def __init__(self, name, status, specialization):
        self.name = name
        self.status = status 
        self.specialization = specialization 

    def __repr__(self):
        return f'Patient: {self.name} is {self.status}'
        



class Hospital:
    def __init__(self):
        self.patients_lst = [] 

    def add_patient(self):
        # Step1 get patient data
        specialization = get_valid_input('Enter specialization ', 1, 20)    
        name = input('Enter patient name: ')                 
        status = get_valid_input('Enter status(0 normal / 1 urgent / 2 super urgent: )', 0, 2)
        
        # step2 create patient obj 
        patient = Patient(name, status, specialization)

        # step3 add patient 
        self.patients_lst.append(patient)

    def print_all_patients(self):
        for patient in self.patients_lst:
           print(patient)


if __name__ == '__main__':
    hospital = Hospital()
    print(len(hospital.patients_lst))
    hospital.add_patient()
    print(len(hospital.patients_lst))
    hospital.print_all_patients()



        
         