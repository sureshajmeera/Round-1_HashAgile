import pandas as pd

# Load the employee data
employee_data = pd.read_csv('C:\Users\Dell\Downloads\archive\EmployeeSampleData.csv')

# Dictionary to store collections
collections = {}

# Function to create a collection
def createCollection(p_collection_name):
    collections[p_collection_name] = pd.DataFrame()

# Function to index employee data, excluding a specified column
def indexData(p_collection_name, p_exclude_column):
    if p_collection_name in collections:
        indexed_data = employee_data.drop(columns=[p_exclude_column], errors='ignore')
        collections[p_collection_name] = indexed_data

# Function to search within a collection by a specific column and value
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name in collections:
        return collections[p_collection_name][collections[p_collection_name][p_column_name] == p_column_value]

# Function to get the count of employees in a collection
def getEmpCount(p_collection_name):
    if p_collection_name in collections:
        return len(collections[p_collection_name])

# Function to delete an employee by ID
def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name in collections:
        collections[p_collection_name] = collections[p_collection_name][collections[p_collection_name]['Employee ID'] != p_employee_id]

# Function to retrieve count of employees grouped by department
def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        return collections[p_collection_name].groupby('Department').size()

# Variable names
v_nameCollection = 'Hash_YourName'
v_phoneCollection = 'Hash_1234'

# Create collections
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# Index data
indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

# Get employee count
print("Employee count before deletion:", getEmpCount(v_nameCollection))

# Delete employee with ID 'E02003'
delEmpById(v_nameCollection, 'E02003')

# Get employee count after deletion
print("Employee count after deletion:", getEmpCount(v_nameCollection))

# Search by column
print("Search by Department = IT:\n", searchByColumn(v_nameCollection, 'Department', 'IT'))
print("Search by Gender = Male:\n", searchByColumn(v_nameCollection, 'Gender', 'Male'))
print("Search in phone collection by Department = IT:\n", searchByColumn(v_phoneCollection, 'Department', 'IT'))

# Get department facets
print("Department facets for v_nameCollection:\n", getDepFacet(v_nameCollection))
print("Department facets for v_phoneCollection:\n", getDepFacet(v_phoneCollection))
