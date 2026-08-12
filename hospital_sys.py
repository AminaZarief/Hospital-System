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


NUMBER_OF_SPECIALIZATIONS = 20
STATUS = ['Normal', 'Urgent', 'Super Urgent']

class Patient: 
    def __init__(self, name, status, specialization):
        self.name = name
        self.status = status 
        self.specialization = specialization 

    def __repr__(self):
        return f'Patient: {self.name} is {STATUS[self.status]}'
        



class Hospital:
    def __init__(self):
        self.patients_lst = [ [] for i in range(NUMBER_OF_SPECIALIZATIONS)] 

    def add_patient(self):
        # Step1 get patient data
        specialization = get_valid_input('Enter specialization ', 1, NUMBER_OF_SPECIALIZATIONS)    
        name = input('Enter patient name: ')                 
        status = get_valid_input('Enter status(0 normal / 1 urgent / 2 super urgent: )', 0, 2)
        
        # step2 create patient obj 
        patient = Patient(name, status, specialization)

        # step3 add patient 
        self.patients_lst[specialization-1].append(patient)

    def print_all_patients(self):
        
        
        for idx, patients in enumerate(self.patients_lst):
           if len(patients) > 0:
               print(f'Specialization {idx + 1}: There are {len(patients)} patients.')
               for patient in patients:
                    print(patient)

    def get_next_patient(self):...


if __name__ == '__main__':
    hospital = Hospital()
    while True:
        print('Program Options:')
        print('1) Add new patients')
        print('2) print all patients')
        print('3) Get next patient')
        print('4) Remove a leaving patient')
        print('5) End the progeam')

        choice = int(input('Enter your choice(from 1 to 5): '))
        if choice == 1:
            hospital.add_patient()
        elif choice == 2:
            hospital.print_all_patients()
        elif choice == 3: 
            hospital.get_next_patient()
        elif choice == 5:
            break
        else:
            print('Not valid number, please enter number from 1 to 5')



        
         