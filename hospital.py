class Patient:
    def __init__(self, pateint_id, pateint_name, age, gender, contact):
        self.__pateint_id = pateint_id
        self.__pateint_name = pateint_name
        self.__age = age
        self.__gender = gender
        self.__contact = contact

    def getPateintInfo(self):
        return {
            "pateint_id": self.__pateint_id,
            "pateint_name":self.__pateint_name,
            "gender": self.__gender,
            "age": self.__age,
            "contact": self.__contact
        }
    
    def display_details(self):
        return f'''
Pateint Id: {self.__pateint_id}
Pateint Name: {self.__pateint_name}
Mobile Number: {self.__age}'''
    
class Doctor:
    __pateints_handled = []
    def __init__(self, doctor_id, name, specialization):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
    
    def add_pateint(self, pateint_id):
        self.__pateints_handled.append(pateint_id)


pat1 = Patient("pat-1", "shubhang", 12, 'M', 975859101092)
print(pat1.getPateintInfo()['pateint_id'])
doc1 = Doctor("doc-123", "Nimit", "eye")
doc1.add_pateint("pat-1")