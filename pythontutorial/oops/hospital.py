class Patient(object):
    def __init__(self, id, name, allergies, bed_number=None):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.patients = []
        self.capacity = capacity

    def add(self, patient):
        if len(self.patients) >= self.capacity:
            print ('Sorry! The Hospital is full!')
        else:
            patient_dictionary = {
            'ID': patient.id,
            'Name': patient.name,
            'Allergies': patient.allergies,
            'Bed Number': patient.bed_number
            }
            self.patients.append(patient_dictionary)
            print ('{} has been admitted.'.format(patient.name))

    def discharge(self, name):
        for value in self.patients:
            if value['Name'] == name:
                value['Bed Number'] = None
                self.patients.remove(value)

hospital = Hospital('Hospital', 3)
patient1 = Patient(1, 'Ash', 'Wool', 1)
hospital.add(patient1)
patient2 = Patient(2, 'Sterling', 'Chocolate', 3)
hospital.add(patient2)
patient3 = Patient(3, 'Alish', 'Puppies', 7)
hospital.add(patient3)

patient4 = Patient(4, 'Andre', 'Kitties', 9)
hospital.add(patient4)
hospital.discharge('Alish')
hospital.discharge('Sterling')
