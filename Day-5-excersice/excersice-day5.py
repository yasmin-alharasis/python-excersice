class Employee:
    number:int
    __name:str
    __address:str
    __salary:float
    __job:str
    def __init__(self,Employee_Number,Name,Address,Salary,Job_Title):
       self.number=Employee_Number
       self.__name=Name
       self.__address=Address
       self.__salary=Salary
       self.__job=Job_Title

        
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address
    
    def setAddress(self,newAddress):
        self.__address=newAddress
        
    def getSallary(self):
        return self.__salary
    
    def getJobTitle(self):
        return self.__job
    def printfunction(self):
        return "Employee1 information:\nEmployee number:"+str(self.number)+"\nName:"+self.__name+"\nAddress: "+self.__address+"\nSalary: "+str(self.__salary)+"\nJob Title:"+self.__job
    
    def print_function(self):
        return "Employee2 information:  Employee number:"+str(self.number)+",Name:"+self.__name+",Address: "+self.__address+",Salary: "+str(self.__salary)+",Job Title:"+self.__job
       
    def __del__(self):
        print(self.__name + " has been deleted")
        
Employee1 = Employee(1,'Mohammad khalid','Amman,Jordan',500,'Consultant')
Employee2 = Employee(2,'Hala Rana','Aqaba,Jordan',750,'Manager')
print(Employee1.printfunction())
print(Employee2.print_function())
Employee1.setAddress('USA')
print("Employee1 New Address :"+Employee1.getAddress())
del Employee1
del Employee2

      
        
        
        
       
    

