import csv

# Create empty lists to store data from csv file with headers - age ,sex    ,bmi    ,children ,smoker ,region    ,charges
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []



#Import the csv file columns to the empty lists
with open('/Users/balajiguntur/Documents/CodeAcademy_Projects/python-datascience-us-medicalcosts-project/insurance.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ages.append(int(row['age']))
        sexes.append(row['sex'])
        bmis.append(float(row['bmi']))
        num_children.append(int(row['children']))
        smoker_statuses.append(row['smoker'])
        regions.append(row['region'])
        insurance_charges.append(float(row['charges']))


#Creating a class to store the data
class patientInfo:
    def __init__(self, patientsages, patientssexes, patientsbmis, patientsnum_children, patientsmoker_statuses, patientsregions, patientsinsurance_charges):
        self.patientsages = patientsages
        self.patientssexes = patientssexes
        self.patientsbmis = patientsbmis
        self.patientsnum_children = patientsnum_children
        self.patientsmoker_statuses = patientsmoker_statuses
        self.patientsregions = patientsregions
        self.patientsinsurance_charges = patientsinsurance_charges
    
    #Calculating the average age of the patients
    def average_age(self):
        total_age = 0
        for age in self.patientsages:
            total_age += age
        average_age = total_age / len(self.patientsages)
        return f"Average Age: {average_age}"
    #Calculating the average bmi of the patients
    def average_bmi(self):
        total_bmi = 0
        for bmi in self.patientsbmis:
            total_bmi += bmi
        average_bmi = total_bmi / len(self.patientsbmis)
        return f"Average BMI: {average_bmi}"
    #Calculating the average charges of the patients
    def average_charges(self):
        total_charges = 0
        for charge in self.patientsinsurance_charges:
            total_charges += charge
        return "Average Charges: " + str(total_charges / len(self.patientsinsurance_charges))
    #Calculating the average charges of the patients who are smokers and non-smokers
    def average_charges_smoker_non_smoker(self):
        total_charges_smoker = 0
        total_charges_non_smoker = 0
        count_smoker = 0
        count_non_smoker = 0
        for i in range(len(self.patientsinsurance_charges)):
            if self.patientsmoker_statuses[i] == 'yes':
                total_charges_smoker += self.patientsinsurance_charges[i]
                count_smoker += 1
            else:
                total_charges_non_smoker += self.patientsinsurance_charges[i]
                count_non_smoker += 1
        average_charges_smoker = total_charges_smoker / count_smoker
        average_charges_non_smoker = total_charges_non_smoker / count_non_smoker
        return f"Average Charges for Smokers: {average_charges_smoker}", f"Average Charges for Non-Smokers: {average_charges_non_smoker}"
    #Calculating the average charges of the patients who have children and those who have no children
    def average_charges_children_no_children(self):
        total_charges_children = 0
        total_charges_no_children = 0
        count_children = 0
        count_no_children = 0
        for i in range(len(self.patientsinsurance_charges)):
            if self.patientsnum_children[i] > 0:
                total_charges_children += self.patientsinsurance_charges[i]
                count_children += 1
            else:
                total_charges_no_children += self.patientsinsurance_charges[i]
                count_no_children += 1
        average_charges_children = total_charges_children / count_children
        average_charges_no_children = total_charges_no_children / count_no_children
        return f"Average Charges for Patients with Children: {average_charges_children}", f"Average Charges for Patients without Children: {average_charges_no_children}"
    #calculating the majority of the patients region
    def majority_region(self):
        region_count = {}
        for region in self.patientsregions:
            if region in region_count:
                region_count[region] += 1
            else:
                region_count[region] = 1
        majority_region = max(region_count, key=region_count.get)
        return f"Majority Region: {majority_region}, Count: {region_count[majority_region]}"
    
    #Calculating unique regions
    def unique_regions(self):
        unique_regions = []
        for region in self.patientsregions:
            if region not in unique_regions:
                unique_regions.append(region)
        return f"Unique Regions: {unique_regions}"
    #calculating the average charges of the patients based on the region
    def average_charges_region(self):
        region_charges = {}
        region_count = {}
        for i in range(len(self.patientsregions)):
            if self.patientsregions[i] in region_charges:
                region_charges[self.patientsregions[i]] += self.patientsinsurance_charges[i]
                region_count[self.patientsregions[i]] += 1
            else:
                region_charges[self.patientsregions[i]] = self.patientsinsurance_charges[i]
                region_count[self.patientsregions[i]] = 1
        for region in region_charges:
            region_charges[region] = region_charges[region] / region_count[region]
        region_average_charges = {}
        for region in region_charges:
            region_average_charges[region] = f"Average Charges for {region}: {region_charges[region]}"
        return region_average_charges
    #Average age of the patients who have atleast one child
    def average_age_children(self):
        total_age_children = 0
        count_children = 0
        for i in range(len(self.patientsages)):
            if self.patientsnum_children[i] > 0:
                total_age_children += self.patientsages[i]
                count_children += 1
        average_age_children = total_age_children / count_children
        return f"Average Age of Patients with Children: {average_age_children}"
    #Method to create dictionary of all the patient data.
    def create_dict(self):
        self.patient_dict = {}
        self.patient_dict['ages'] = [int(age) for age in self.patientsages]
        self.patient_dict['sexes'] = self.patientssexes
        self.patient_dict['bmis'] = self.patientsbmis
        self.patient_dict['num_children'] = self.patientsnum_children
        self.patient_dict['smoker_statuses'] = self.patientsmoker_statuses
        self.patient_dict['regions'] = self.patientsregions
        self.patient_dict['insurance_charges'] = self.patientsinsurance_charges
        return self.patient_dict

patientInformation = patientInfo(ages,sexes,bmis,num_children,smoker_statuses,regions,insurance_charges)
print(patientInformation.average_age())
print(patientInformation.average_bmi())
print(patientInformation.average_charges())
print(patientInformation.average_charges_smoker_non_smoker())
print(patientInformation.average_charges_children_no_children())
print(patientInformation.majority_region())
print(patientInformation.unique_regions())
print(patientInformation.average_charges_region())
print(patientInformation.average_age_children())
print(patientInformation.create_dict())

#Predicting the insurance charges based on the bmi of the patients
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Reshaping the bmi data
bmi_reshaped = np.array(bmis).reshape(-1,1)
insurance_charges_reshaped = np.array(insurance_charges).reshape(-1,1)





