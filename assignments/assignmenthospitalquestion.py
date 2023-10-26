#Write a program to build a simple hospital management system using Python 

class Hospital:
   
    def __init__(self):
        self.patients= []

    def add_patient(self,Patient_Id,Patient_Name,Patient_Age,Patient_Gender,Patient_Healthissue):
        patient = {
            "ID"        : Patient_Id,
            "Name"      : Patient_Name,
            "Age"       : Patient_Age,
            "Gender"    : Patient_Gender,
            "Healthissue" : Patient_Healthissue
        }

        self.patients.append(patient)

    def display_patients(self):

        if not self.patients:
            print("No Patients in this Hospital....")

        else:
            for x in self.patients:
                print("Patient ID        : ",x['ID'])
                print("Patient Name      : ",x['Name'])
                print("Patient Age       : ",x['Age'])
                print("Patient Gender    : ",x['Gender'])    
                print("Patient Healthissue : ",x['Health issue'])
                print("     ")

    def search_patient(self,Patient_id):

        for x in self.patients:
            if x['ID'] ==Patient_id:
                print("Patient Found")
                print("Patient ID :",x['ID'])
                print("Patient Name :",x["Name"])
                print("Patient Age : ",x['Age'])
                print("Patient Gender : ",x['Gender'])
                print("Patient Healthissue : ",x['Healthissue'])
                return
        print("Patient With ID : ",Patient_id," Not Found")

    def delete_patient(self,patient_id):

        for x in self.patients:
            if x['ID'] ==patient_id:
                self.patients.remove[x]
                print("Patient With ID", patient_id," Deleted Sucess fully...")
                return
        print("Patient With ID ",patient_id, " Not Found ")
        
    def update_patient(self,patient_id,Healthissue):

        for x in self.patients:
            if x['ID'] == patient_id:
                x['Health issue'] = Healthissue
                print("Patients information updated")
                return
        print("patient with ID ",patient_id, " Not Found ")

main = Hospital()

while True:
    print(".....................WELCOME TO STARPINACLE....................")
    print("     a. ADD A NEW PATIENT                : ")
    print("     b.DISPLAY ALL PATIENTS              : ")
    print("     c.SEARCH A PATIENT BY ID            : ")
    print("     d.DELETE A PATIENT BY ID            :  ")
    print("     e.UPDATE A PATIENT HEALTHISSUE BY ID  : ")
    print("     f.EXIT")
    choice =input("Enter your option :  ")

    if choice== 'a':
        Patient_Id        = int(input("Enter Patient ID     : "))
        Patient_Name      = input("Enter Patient Name       : ")
        Patient_Age       = int(input("Enter Patient Age    : "))
        Patient_Gender    = input("Enter patient Gender     : ")
        Patient_Healthissue = input("Enter patient Healthissue  : ")
        main.add_patient(Patient_Id,Patient_Name,Patient_Age,Patient_Gender,Patient_Healthissue)

    elif choice =='b':
        main.display_patient()

    elif choice == 'c':
        patient_id = int(input("Entet Patient ID : "))
        main.search_patient(patient_id)

    elif choice == 'd':
        patient_id = int(input("Enter  Patient ID : "))
        main.delete_patient(patient_id)
    
    elif choice == 'e':
        patient_id = int(input("Enter Your Patinet ID : "))
        Patient_Diagnosiss = input("Enter Patient Healthissue : ")
        main.update_patient(patient_id,Patient_Healthissue)
    
    elif choice == 'f':
        print(" Thank You - Speedy Recovery ")
        break

    else:
        print("Invalid option, Please try Again ")