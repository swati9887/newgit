# ""Employee Resource Planning
# Different Kind of Employees are there ie employees with different designations.
# Different Designation employees have different attributes
# Designations: Manager, Trainer, Director
#
# Manager Properties: Id, Name, Age, Mob, Area
# Trainer Properties: Id, Name, Age, Mob, Course
# Director Properties: Id, Name, Age, Mob, shares
#
# CRUD Operations.
# Add Employee, Search, Delete, Modify, Display All, Exit
# """

# #BLL
# class Employee:
#     emplist=[]    #emplist=[1000,2000,3000,4000...]
#     def __init__(self):
#         self.id=0
#         self.name=0
#         self.age=0
#         self.mob=0
#         self.desig=0
#     def addEmployee(self):
#         Employee.emplist.append(self)
#     def searchEmployee(self):     #self.id=20, self is having 5 variable
#         for e in Employee.emplist:  #e is having 6 variables
#             if(e.id==self.id):
#                 return e
#     @staticmethod
#     def deleteEmployee(id):   #id=20
#         for e in Employee.emplist:  #e is having 6 variables
#             if(e.id==id):
#                 Employee.emplist.remove(e)
#
#     def modifyEmployee(id, name, age, mob, desig):
#             for e in Employee.emplist:
#                 if (e.id == id):
#                     e.name =name
#                     e.age = age
#                     e.mob =mob
#                     e.desig =choice_desig
#                     return True
#             return False
#
#
# class Manager(Employee):  #Now if we create Manager Class Object, total 6 variables will be created.
#     def __init__(self):
#         self.area=0
#         super().__init__()
#     def addEmployee(self):
#         super().addEmployee()
# class Trainer(Employee):  #Now if we create Trainer Class Object, total 6 variables will be created.
#     def __init__(self):
#         self.course=0
#         super().__init__()
#     def addEmployee(self):
#         super().addEmployee()
# class Director(Employee):  #Now if we create Directors Class Object, total 6 variables will be created.
#     def __init__(self):
#         self.share=0
#         super().__init__()
#
#
#
# #PL
# print("Welcome to Swati's Employee Resource Planning")
# def showEmployee(e):    #e=2000
#     print(f"Empl Id:{e.id}, Empl Name:{e.name}, Empl Age:{e.age}, Empl Mob:{e.mob}, Empl Desig:{e.desig},",end=" ")
#     if(e.desig=="Manager"):
#         print("Empl Area:",e.area)
#     elif (e.desig == "Trainer"):
#         print("Empl Course:", e.course)
#     else:
#         print("Empl Area:", e.share)
#
#
# while(1):
#     choice=input("""Enter 1 to Add Employee, 2 to Search Employee, 3 to Delete Employee
#     4 to Modify Employee, 5 to Display all Employees, 6 to Exit:""")
#     if(choice=="1"):  #Add Employee
#         choice_desig=input("Enter 1 to Add Manager, 2 to Add Trainer, 3 to Add Director:")
#         if(choice_desig=="1"):  #Add Manager
#             mgr=Manager()     #Address 1000, mgr.id=0,mgr.name=0,mgr.age=0...
#             mgr.id=input("Enter Employee Id:")
#             mgr.name=input("Enter Employee Name:")
#             mgr.age = input("Enter Employee Age:")
#             mgr.mob = input("Enter Employee Mob:")
#             mgr.desig = "Manager"
#             mgr.area = input("Enter Employee Area:")
#             mgr.addEmployee()
#             print("Employee Added Successfully")
#         elif (choice_desig == "2"):  # Add Trainer
#             tr = Trainer()  # Address 1000, mgr.id=0,mgr.name=0,mgr.age=0...
#             tr.id = input("Enter Employee Id:")
#             tr.name = input("Enter Employee Name:")
#             tr.age = input("Enter Employee Age:")
#             tr.mob = input("Enter Employee Mob:")
#             tr.desig = "Trainer"
#             tr.course = input("Enter Employee Course:")
#             tr.addEmployee()
#             print("Employee Added Successfully")
#         elif (choice_desig == "3"):
#             dir = Director()
#             dir.id = input("enter Employee id:")
#             dir.name = input("enter Employee name:")
#             dir.age = input("enter Employee age:")
#             dir.mob = input("enter Employee mob:")
#             dir.desig = input("enter Employee desig:")
#             dir.shares = input("enter Employee shares")
#             dir.addEmployee()
#             print("Employee Added Suceessfully")
#
#
#
#     elif(choice=="2"):  #Search Employee
#         emp=Employee()    #Total 5 Variable created
#         emp.id=input("Enter Employee Id:")  #emp.id=20
#         e=emp.searchEmployee() #Now e is having that employee which we were searching
#         showEmployee(e)
#     elif (choice == "3"):  # Delete Employee
#         id = input("Enter Employee Id:")  # id=20,
#         Employee.deleteEmployee(id)
#         print("Employee Deleted Successfully")
#     elif(choice=="4"):
#         id = input("enter Employee id to modify data:")
#         name=input("Enter Employee updated Name:")
#         age=input("Enter Employee updated Age:")
#         mob=input("Enter Employee updated Mob:")
#         desig = input("Enter Employee updated desig")
#         print("Customer Modified Successfully")
#     elif(choice=="5"):
#         for e in Employee.emplist:
#             showEmployee(e)
#     elif (choice == "6"):
#         print("Thanks for using Swati's Employee Resource Planning System")
#         break
#     else:
#         print("Incorrect Choice")
#
#
#
