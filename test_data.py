from hospital_sys import  Patient
import random

NUMBER_OF_SPECIALIZATIONS = 20
hospital_patients_lst = [ [] for i in range(NUMBER_OF_SPECIALIZATIONS)] 




for i in range(10):
    p = Patient(f'pat{i}',random.randint(0,2), 1)
    hospital_patients_lst[0].append(p)
    
for i in range(6):
    p = Patient(f'pat{i}',i%3, 7)
    hospital_patients_lst[6].append(p)

for i in range(3):
    p = Patient(f'pat{i}',i%3, 9)
    hospital_patients_lst[8].append(p)

