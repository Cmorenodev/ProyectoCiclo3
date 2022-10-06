from ast import mod
from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.


## Creación de la tabla administradores junto con sus campos

class ADMINISTRATOR(models.Model):
    AD_USER=models.TextField(primary_key=True, max_length=50,null=False,unique=True)
    AD_PASSWORD=models.IntegerField(null=False)
    AD_EMAIL=models.TextField(max_length=50,null=False)
    AD_EMAIL=models.EmailField(max_length=50,null=False)
    AD_NAMES=models.TextField(max_length=50,null=False)
    AD_LASTNAMES=models.TextField(max_length=50,null=False)
    AD_CELLPHONE=models.TextField(max_length=50,null=False)
    AD_ROL=models.TextField(max_length=50,null=False)

## Creación de la tabla empresas junto con sus campos


class BUSINESS(models.Model):  
    EM_IDName=models.TextField(max_length=50,null=False)
    EM_NIT=models.IntegerField(primary_key=True)
    EM_CITY=models.TextField(max_length=50)
    EM_ADDRESS=models.TextField(max_length=50)
    EM_CELLPHONE=models.TextField(max_length=10)
    EM_DATECREATE=models.DateField()
    EM_PRODUCTIVE_SECTOR=models.TextField(max_length=50)
    EM_AD_USER=models.ForeignKey(ADMINISTRATOR,on_delete=models.CASCADE)

    
## Creación de la tabla empleados junto con sus campos

class EMPLOYEES(models.Model):
    EMP_USER=models.TextField(primary_key=True,max_length=50,null=False,unique=True)
    EMP_PASSWORD=models.IntegerField(null=False)
    EMP_EMAIL=models.TextField(max_length=50,null=True)
    EMP_NAMES=models.TextField(max_length=50,null=False)
    EMP_LASTNAMES=models.TextField(max_length=50,null=False)
    EMP_CELLPHONE=models.TextField(max_length=50,null=False)
    EMP_ROLE=models.TextField(max_length=50,null=False)
    EMP_EM_NIT=models.ForeignKey(BUSINESS,on_delete=models.CASCADE)
    EMP_AD_USER=models.ForeignKey(ADMINISTRATOR,on_delete=models.CASCADE)

class PRODUCTS(models.Model):
    PRO_Code=models.AutoField(primary_key=True)
    PRO_Name=models.CharField(max_length=50,null=False)
    PRO_Cost=models.IntegerField(null=False)
    PRO_Description=models.TextField(max_length=50,null=False)
    PRO_Stock=models.IntegerField(null=False)

class INCOME(models.Model):
    ING_Code = models.AutoField(primary_key=True,null=False,unique=True)
    ING_EM_NIT=models.ForeignKey(BUSINESS, on_delete=models.CASCADE)
    ING_EMP_User=models.ForeignKey(EMPLOYEES,on_delete=models.CASCADE)
    ING_PRO_Code=models.ForeignKey(PRODUCTS, on_delete=models.CASCADE)
    ING_Fecha= models.DateField(auto_now=True)
    ING_Quantity= models.IntegerField(null=False)
    ING_Total = models.IntegerField(null=False) #RELACIONARLO CON TOTAL DE PRODUCTO

class WORKINGHOURS(models.Model):
    WORH_Code=models.TextField(primary_key=True, max_length=50,unique=True)
    WORH_TipeHours=models.TextField(max_length=50,null=True,unique=True)
    WORH_Costs=models.IntegerField(null=True)    
    
class EMPLOYEEPAYROLL(models.Model):
    PAY_Id=models.AutoField(primary_key=True)
    PAY_EM_User=models.ForeignKey(EMPLOYEES, on_delete=models.CASCADE)
    PAY_NIT=models.ForeignKey(BUSINESS, on_delete=models.CASCADE)
    PAY_Hours=models.IntegerField(null=True)
    PAY_ExtraHours=models.IntegerField(null=True)
    PAY_parafiscal=models.IntegerField(null=True)
    PAY_WorkingHours=models.ForeignKey(WORKINGHOURS, on_delete=models.CASCADE)
    PAY_StartDate=models.DateField()
    PAY_FinalDate=models.DateField()
    PAY_TotalSalary=models.IntegerField(null=True)

class CUSTOMERS(models.Model):
    CLI_User = models.TextField(primary_key=True, max_length=25,null=False,unique=True)
    CLI_Password=models.IntegerField(null=False)  
    CLI_Names = models.TextField(max_length=50,null=False)
    CLI_LastNames= models.TextField(max_length=50,null=False)
    CLI_Email = models.EmailField(unique=True)
    CLI_CellPhone= models.TextField(max_length=15,unique=True)
    CLI_AD_User= models.ForeignKey(ADMINISTRATOR, on_delete=models.CASCADE)

class LISTBUY(models.Model):
    LBUY_Code = models.AutoField(primary_key=True)
    LBUY_PRO_Code = models.ForeignKey(PRODUCTS,on_delete=models.CASCADE)
    LBUY_CLI_User = models.ForeignKey(CUSTOMERS,on_delete=models.CASCADE)
    LBUY_Fecha= models.DateField(auto_now=True)


    
class EXPENSES(models.Model):
    EGR_Code = models.AutoField(primary_key=True)
    EGR_EM_NIT = models.ForeignKey(BUSINESS, on_delete=models.CASCADE)
    EGR_Name = models.TextField(max_length=50,null=False)
    EGR_Fecha = models.DateField(auto_now=True)
    EGR_Total = models.IntegerField(null=False)


    