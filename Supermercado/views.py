from django.shortcuts import render
from ast import Delete
import json
##from types import NoneType
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Supermercado.models import *
from django.http import JsonResponse

##CRUD ADMIN
class ADMINISTRATORView(View):
    ##consultar administradores
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,AD_USER=""):
        if len(AD_USER)>0:
            UserAdmin =list(ADMINISTRATOR.objects.filter(AD_USE=AD_USER).values())
            if len(UserAdmin)>0:
                datos={"mensaje":UserAdmin}
            else:
                datos={'mensaje: No se encontro administrador'}
        else:
            UserAdmin =list(ADMINISTRATOR.objects.values())
            if len(UserAdmin)>0:
                datos={"mensaje":UserAdmin}
            else:
                datos={'mensaje: no se encontro Ningun administrador registrado'}
        
        return JsonResponse(datos)
    
    ##crear administrador
    
    def post(self,request):
        data=json.loads(request.body) 
        Admin=ADMINISTRATOR(AD_USER=data['AD_USER'],AD_PASSWORD=data['AD_PASSWORD'],AD_EMAIL=data['AD_EMAIL']
                             , AD_NAMES=data[' AD_NAMES'],AD_LASTNAMES=data['AD_LASTNAMES'],
                             AD_CELLPHONE=data['AD_CELLPHONE'],AD_ROL=data['AD_ROL'])
        Admin.save()
        datos={'Mensaje': 'Administrador registrado exitosamente'}
        return JsonResponse(datos)
    
    ##Actualizar administrador

    def put(self,request,AD_USER):
        data=json.loads(request.body) 
        UserAdmin =list(ADMINISTRATOR.objects.filter(AD_USE=AD_USER).values())
        if len(UserAdmin)>0:
            admin=ADMINISTRATOR.objects.get(AD_USE=AD_USER)
            admin.AD_PASSWORD=data['AD_PASSWORD']
            admin.AD_EMAIL=data['AD_EMAIL']
            admin.AD_NAMES=data[' AD_NAMES']
            admin.AD_LASTNAMES=data['AD_LASTNAMES']
            admin. AD_CELLPHONE=data['AD_CELLPHONE']
            admin.AD_ROL=data['AD_ROL']
            admin.save()
            datos={'Mensaje': 'Administrador actualizado exitosamente'}
        else :
            datos={'Mensaje': 'Administrador no encontrado para actualizar'}
        return JsonResponse(datos)
        
    ##Borrar administrador
    
    def delete(self,request,AD_USER):
        UserAdmin =list(ADMINISTRATOR.objects.filter(AD_USE=AD_USER).values())
        if len(UserAdmin)>0:
           UserAdmin.objects.filter(AD_USE=AD_USER).delete()
           datos={'Mensaje': 'Administrador eliminado exitosamente'}
        else :
            datos={'Mensaje': 'Administrador no encontrado para eliminar'}
        return JsonResponse(datos)

class BUSINESSView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,EM_nit=0):
        if EM_nit>0:
            Business=list(BUSINESS.objects.filter(EM_NIT=EM_nit).values())
            if len(Business)>0:

                datos={"empresas":Business}

                datos={"empresas":Business, "Mensaje":"Resultado de la busqueda"}

            else:
                datos={"Error":"No hay empresas registradas con ese NIT"}
        else:
            Business=list(BUSINESS.objects.values())
            if len(Business)>0:
                datos={"empresas":Business}
            else:
                datos={"Error":"No hay empresas registradas"}
        return JsonResponse(datos)
    

    def post(self,request):
        try:
            dato=json.loads(request.body)
            
            admin=ADMINISTRATOR.objects.get(AD_USER=dato['EM_AD_USER'])
            Business=BUSINESS.objects.create(   
                EM_IDName=dato['EM_IDName'],
                EM_NIT=dato['EM_NIT'],
                EM_CITY=dato['EM_CITY'],
                EM_ADDRESS=dato['EM_ADDRESS'],
                EM_CELLPHONE=dato['EM_CELLPHONE'],
                EM_DATECREATE=dato['EM_DATECREATE'],
                EM_PRODUCTIVE_SECTOR=dato['EM_PRODUCTIVE_SECTOR'],
                EM_AD_USER=admin,)
            Business.save()
            datos={'mensaje':'Empresa agregada'}  
        except ADMINISTRATOR.DoesNotExist:
            datos={'mensaje':'Empresa no agregada administrador no existe'}
        return JsonResponse(datos)

    ##Actualizar empresa
    def put(self,request,EM_nit):
        
        data=json.loads(request.body)
        Business=list(BUSINESS.objects.filter(EM_NIT=EM_nit).values())
        if len(Business)>0:
            Busines=BUSINESS.objects.get(EM_NIT=EM_nit)
            Busines.EM_IDName=data["EM_IDName"]
            Busines.EM_CITY=data["EM_CITY"]
            Busines.EM_ADDRESS=data["EM_ADDRESS"]
            Busines.EM_CELLPHONE=data["EM_CELLPHONE"]
            Busines.EM_DATECREATE=data["EM_DATECREATE"]
            Busines.EM_PRODUCTIVE_SECTOR=data["EM_PRODUCTIVE_SECTOR"]
            Busines.save()
            mensaje={"mensaje":"Se actualizo la empresa requerida"}
        else:
            mensaje={"mensaje":"No existe la empresa  requerida"}
        return JsonResponse(mensaje)
    
    ##Eliminar empresas
    def delete(self,request,EM_nit):     
        business=list(BUSINESS.objects.filter(EM_NIT=EM_nit).values())
        if len(business)>0:
            BUSINESS.objects.filter(EM_NIT=EM_nit).delete()
            mensaje={"mensaje":"se a eliminado la empresa seleccionada"}
        else:
            mensaje={"mensaje":"no existe la empresa requerida no eliminada"}
        return JsonResponse(mensaje)
  
    
class EMPLOYEESView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,EMP_User=""):
        if len(EMP_User)>0:
            Employees=list(EMPLOYEES.objects.filter(EMP_USER=EMP_User).values())
            if len(Employees)>0:
                datos={"empleados":Employees}
            else:

                datos={"Mensaje":"No hay empleados registrados con ese Emp_user"}

                datos={"mensaje":"No hay empleados registrados con ese usuario"}

        else:
            Employees=list(EMPLOYEES.objects.values())
            if len(Employees)>0:
                datos={"empleados":Employees}
            else:
                datos={"Mensaje":"No hay empleados registradas"}

                datos={"mensaje":"No hay empleados registrados"}

        return JsonResponse(datos)
    
    ##insertar empleado 
    def post(self,request):
        try:
            dato=json.loads(request.body)
            

            empresa=BUSINESS.objects.get(EM_NIT=dato['EMP_EM_NIT_id'])
            admin=ADMINISTRATOR.objects.get(AD_USER=dato['EMP_AD_USER_id'])


            


            employees=EMPLOYEES.objects.create(
                                                EMP_USER=dato['EMP_USER'],
                                                EMP_PASSWORD=dato['EMP_PASSWORD'],
                                                EMP_EMAIL=dato['EMP_EMAIL'],
                                                EMP_NAMES=dato['EMP_NAMES'],
                                                EMP_LASTNAMES=dato['EMP_LASTNAMES'],
                                                EMP_CELLPHONE=dato['EMP_CELLPHONE'],
                                                EMP_ROLE=dato['EMP_ROLE'],
                                                EMP_EM_NIT=empresa,
                                                EMP_AD_USER=admin
                                                )
            employees.save()
            datos={'mensaje':'Empleado registrado exitosamente'}  
        except ADMINISTRATOR.DoesNotExist:
            datos={'mensaje':'Empleado no agregado administrador no existe'}
        return JsonResponse(datos)
    
    ##actualizar empleado
    def put(self,request,EMP_User):
        
        data=json.loads(request.body)
        Employees=list(EMPLOYEES.objects.filter(EMP_USER=EMP_User).values())
        if len(Employees)>0:
            empleado=EMPLOYEES.objects.get(EMP_USER=EMP_User)
            empleado.EMP_PASSWORD=data["EMP_PASSWORD"]
            empleado.EMP_EMAIL=data["EMP_EMAIL"]
            empleado.EMP_NAMES=data["EMP_NAMES"]
            empleado.EMP_LASTNAMES=data["EMP_LASTNAMES"]
            empleado.EMP_CELLPHONE=data['EMP_CELLPHONE']
            empleado.EMP_ROLE=data["EMP_ROLE"]
            
            empleado.save()
            mensaje={"mensaje":"Se actualizo el empleado requerido"}
        else:
            mensaje={"mensaje":"No existe el empleado  requerido"}
        return JsonResponse(mensaje)
    
    ##eliminar empleado
    
    def delete(self,request,EMP_User):
        
        EMP_USER=list(EMPLOYEES.objects.filter(EMP_USER=EMP_User).values())
        if len(EMP_USER)>0:
            EMPLOYEES.objects.filter(EMP_USER=EMP_User).delete()
            mensaje={"mensaje":"se a eliminado el empleado  seleccionada"}
        else:
            mensaje={"mensaje":"no existe el empleado requerida no eliminada"}
        return JsonResponse(mensaje)
    
    
    
    

class EMPLOYEEPAYROLLView(View):
     #metodos para utilisar json
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,PAY_id=0):
        if PAY_id>0:
            payemplo=list(EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id.values()))
            if len(payemplo)>0:
                datos={"mensaje":payemplo}
            else:
                datos={"mensaje":"no hay datos"}
        else:
            payemplo=list(EMPLOYEEPAYROLL.objects.values())
            if len(payemplo)>0:
                datos={"mensaje":payemplo}
            else:
                datos={"mensaje":"no hay datos"}
        return JsonResponse(datos)
        
    def post(self,request):
        try:
            dat=json.loads(request.body)
            #llaves foraneas
            emp=EMPLOYEES.objects.get(EMP_USER=dat['emp_user'])
            em_nit=BUSINESS.objects.get(EM_NIT=dat['em_nit1'])
            worh_code=WORKINGHOURS.objects.get(WORH_Code=dat['worh_code1'])
            
            
            #creación de json para enviar
            
            newemployeepayroll=EMPLOYEEPAYROLL.objects.create(emp_user=emp,
                                                              em_nit1=em_nit,
                                                              PAY_Hours=dat['PAY_Hours'],
                                                              PAY_ExtraHours=dat['PAY_ExtraHours'],
                                                              PAY_parafiscal=dat['PAY_parafiscal'],
                                                              worh_code1=worh_code,
                                                              PAY_StartDate=dat['PAY_StartDate'],
                                                              PAY_FinalDate=dat['PAY_FinalDate'],
                                                              PAY_TotalSalary=dat['PAY_TotalSalary'])
            newemployeepayroll.save()
            datos={'mensaje':'nomina registrada'}
        
        except EMPLOYEES.DoesNotExist:
            datos={'mensaje':'el empleado no existe'}
        except BUSINESS.DoesNotExist:
            datos={'mensaje':'la empresa no existe'}
        except WORKINGHOURS.DoesNotExist:
            datos={'mensaje':'ese estilo de hora no es posible ingresarla'}
        return JsonResponse(datos)
        
    def put(self,request,PAY_id):
        #crear conexion a body
        data=json.loads(request.body)
        #genero la busqueda con el dato
        emp=list(EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id).values())
        #genero la busqueda si hay valores con el dato de busqueda anterior
        if len(emp)>0:
            empPay=emp.objects.get(PAY_Id=PAY_id)
            empPay.PAY_EM_User=data["PAY_EM_User"]
            empPay.PAY_NIT=data["PAY_NIT"]
            empPay.PAY_Hours=data["PAY_Hours"]
            empPay.PAY_ExtraHours=data["PAY_ExtraHours"]
            empPay.PAY_parafiscal=data['PAY_parafiscal']
            empPay.PAY_WorkingHours=data["PAY_WorkingHours"]
            empPay.PAY_StartDate=data["PAY_StartDate"]
            empPay.PAY_FinalDate=data["PAY_FinalDate"]
            empPay.PAY_TotalSalary=data["PAY_TotalSalary"]
            empPay.save()
            
            mensaje={"mensaje":"se a actualizado la nomida requerida"}
        else:
            mensaje={"mensaje":"no existe la nomida requerida"}
        return JsonResponse(mensaje)
        
    def delete(self,request,PAY_id):
        
        PAY_id=list(EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id).values())
        if len(PAY_id)>0:
            EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id).delete()
            mensaje={"mensaje":"se a eliminado el registro"}
        else:
            mensaje={"mensaje":"no existe el dato, no se elimino nada"}
        return JsonResponse(mensaje)
        
class WORKINGHOURSView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,WORH_code=""):
        if len(WORH_code)>0:
            worhours=list(WORKINGHOURS.objects.filter(WORH_Code=WORH_code).values())
            if len(worhours)>0:
                datos={"mensaje":worhours}
            else:
                datos={"mensaje":"no hay datos"}
        else:
            worhours=list(WORKINGHOURS.objects.values())
            if len(worhours)>0:
                datos={"mensaje":worhours}
            else:
                datos={"mensaje":"no hay datos"}
        return JsonResponse(datos)
    
    def post(self,request):
        try:
            dat=json.loads(request.body)
        
            #creación de json para enviar
            
            newemployeepayroll=EMPLOYEEPAYROLL.objects.create(WORH_Code=dat['WORH_Code'],
                                                              WORH_TipeHours=dat['WORH_TipeHours'],
                                                              WORH_Costs=dat['WORH_Costs'])
                                                              
            newemployeepayroll.save()
            datos={'mensaje':'hora registrada'}
        
        except:
            datos={'mensaje':'no se registro'}
        return JsonResponse(datos)
    
    def put(self,request,WORH_code):
        #crear conexion a body
        data=json.loads(request.body)
        #genero la busqueda con el dato
        hours=list(WORKINGHOURS.objects.filter(WORH_Code=WORH_code).values())
        #genero la busqueda si hay valores con el dato de busqueda anterior
        if len(hours)>0:
            hor=hours.objects.get(WORH_Code=WORH_code)
            hor.WORH_TipeHours=data["PAY_EM_User"]
            hor.WORH_Costs=data["PAY_NIT"]                        
            mensaje={"mensaje":"se a actualizado la hora requerida"}
        else:
            mensaje={"mensaje":"no existe la hora requerida"}
        return JsonResponse(mensaje)
    
    def delete(self,request,WORH_code):
        #data=json.loads(request.body)
        hours=list(WORKINGHOURS.objects.filter(WORH_Code=WORH_code).values())
        if len(hours)>0:
            WORKINGHOURS.objects.filter(WORH_Code=WORH_code).delete()
            mensaje={"mensaje":"se a eliminado la hora"}
        else:
            mensaje={"mensaje":"no existe el dato, no se elimino nada"}
        return JsonResponse(mensaje)
        
class LISTBUYView(View):
     #metodos para utilisar json
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    ## consultar lista compras
    def get(self,request,LBUY_Code=""):
        if len(LBUY_Code)>0:
            buy_list=list(LISTBUY.objects.filter(LBUY_CLI_User=LBUY_Code).values())
            if len(buy_list)>0:
                datos={"mensaje":buy_list}
            else:
                datos={"mensaje":"no hay datos"}
        else:
            buy_list=list(LISTBUY.objects.values())
            if len(buy_list)>0:
                datos={"mensaje":buy_list}
            else:
                datos={"mensaje":"no hay datos todo"}
        return JsonResponse(datos)
    ##crear lista compras    

    def post(self,request):
        try:
            dat=json.loads(request.body)
            #llaves foraneas
            procod=PRODUCTS.objects.get(PRO_Code=dat['LBUY_PRO_Code'])
            usuario=CUSTOMERS.objects.get(CLI_User=dat['LBUY_CLI_User'])
            
            
            
            #creación de json para enviar
            
            nwebuy=LISTBUY.objects.create( LBUY_PRO_Code=procod,
                                           LBUY_CLI_User=usuario,
                                           LBUY_Fecha=dat['LBUY_Fecha'],
            )
                                                             
            datos={'mensaje':'compra registrada'}
        
        except PRODUCTS.DoesNotExist:
            datos={'mensaje':'producto no existe'}
        except CUSTOMERS.DoesNotExist:
            datos={'mensaje':'cliente no existe'}
       
        return JsonResponse(datos)
        ## actualizar
    def put(self,request,buy_cod):
        #crear conexion a body
        data=json.loads(request.body)
        #genero la busqueda con el dato
        compras=list(LISTBUY.objects.filter(LBUY_Code=buy_cod).values())
        #genero la busqueda si hay valores con el dato de busqueda anterior
        if len(compras)>0:
            newbuy=compras.objects.get(LBUY_Code=buy_cod)
            newbuy.LBUY_PRO_Code=data["LBUY_PRO_Code"]
            newbuy.LBUY_CLI_User=data["LBUY_CLI_User"]
            newbuy.LBUY_Fecha=data["LBUY_Fecha"]
            newbuy.save()
            
            mensaje={"mensaje":"se a actualizado la compra"}
        else:
            mensaje={"mensaje":"no existe la compra"}
        return JsonResponse(mensaje)
        
    def delete(self,request,LBUY_Code=""):
        
        buy_cod=list(LISTBUY.objects.filter(LBUY_Code=LBUY_Code).values())
        if len(buy_cod)>0:
           
            LISTBUY.objects.filter(LBUY_Code=LBUY_Code).delete()
            mensaje={"mensaje":"se a eliminado la compra"}
        else:
            mensaje={"mensaje":"no existe el dato, no se elimino nada"}
        return JsonResponse(mensaje)

class PRODUCTSView(View):
     #metodos para utilisar json
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    ## consultar
    def get(self,request,code=""):
        if len(code)>0:
            pro_list=list(PRODUCTS.objects.filter(PRO_Code=code).values())
            if len(pro_list)>0:

                datos={"productos":pro_list}

                datos={"productos":pro_list, "Mensaje":"Resultado de la busqueda"}

            else:
                datos={"Error":"No se encontró el producto"}
        else:
            pro_list=list(PRODUCTS.objects.values())
            if len(pro_list)>0:
                datos={"productos":pro_list}
            else:
                datos={"Error":"No hay productos registrados"}
        return JsonResponse(datos)
    ##crear  

    def post(self,request):      
        dat=json.loads(request.body)                        
        #creación de json para enviar            
        newpro=PRODUCTS.objects.create(
            PRO_Name=dat['PRO_Name'],
            PRO_Description=dat['PRO_Description'],
            PRO_Cost=dat['PRO_Cost'],           
            PRO_Stock=dat['PRO_Stock']
            )
        newpro.save()                                                 
        datos={'mensaje':'Producto registrado'}     
        return JsonResponse(datos)

        ## actualizar
    def put(self,request,code):
        #crear conexion a body
        data=json.loads(request.body)
        #genero la busqueda con el dato
        productos=list(PRODUCTS.objects.filter(PRO_Code=code).values())
        #genero la busqueda si hay valores con el dato de busqueda anterior
        if len(productos)>0:
            newpro=PRODUCTS.objects.get(PRO_Code=code)
            newpro.PRO_Name=data["PRO_Name"]
            newpro.PRO_Description=data['PRO_Description']
            newpro.PRO_Cost=data['PRO_Cost']         
            newpro.PRO_Stock=data['PRO_Stock']
            newpro.save()
            
            mensaje={"mensaje":"Se a actualizado el producto"}
        else:
            mensaje={"mensaje":"No existe el producto"}
        return JsonResponse(mensaje)
        
    def delete(self,request,code):    
        buy_cod=list(PRODUCTS.objects.filter(PRO_Code=code).values())
        if len(buy_cod)>0:
            PRODUCTS.objects.filter(PRO_Code=code).delete()
            mensaje={"mensaje":"Se a eliminado el producto"}
        else:
            mensaje={"mensaje":"El producto no existe"}
        return JsonResponse(mensaje)

class INCOMEView(View):
     #metodos para utilisar json
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    ## consultar
    def get(self,request,code=""):
        if len(code)>0:
            ING_list=list(INCOME.objects.filter(ING_Code=int(code)).values())
            if len(ING_list)>0:
                datos={"ingresos":ING_list, "Mensaje":"Resultado de la búsqueda"}
            else:
                datos={"Error":"No se encontraron datos"}
        else:
            ING_list=list(INCOME.objects.values())
            if len(ING_list)>0:
                datos={"ingresos":ING_list}
            else:
                datos={"Error":"No se encontraron datos"}
        return JsonResponse(datos)


    def post(self,request):
        try:
            dat=json.loads(request.body)
            #llaves foraneas
            #empresa=BUSINESS.objects.get(EM_NIT=dat['ING_EM_NIT_id'])
            #empleado=EMPLOYEES.objects.get(EMP_USER=dat['ING_EMP_User_id'])
            #procod=PRODUCTS.objects.get(PRO_Code=dat['ING_PRO_Code_id'])

            empresa=BUSINESS.objects.get(EM_NIT=dat['Empresa'])
            empleado=EMPLOYEES.objects.get(EMP_USER=dat['Empleado'])
            procod=PRODUCTS.objects.get(PRO_Code=dat['Producto'])

            newing=INCOME.objects.create(
                ING_EM_NIT=empresa,
                ING_EMP_User=empleado, 
                ING_PRO_Code=procod,
                ING_Quantity=dat['ING_Quantity'],
                ING_Total=dat['ING_Total']
            )

            # newing=INCOME.objects.create(
            #     ING_EM_NIT_id=7984651,
            #     ING_EMP_User_id="Samuel456", 
            #     ING_PRO_Code_id=1,
            #     ING_Quantity=dat['ING_Quantity'],
            #     ING_Total=dat['ING_Total']
            # )
            newing.save()                                 
            datos={'mensaje':'Ingreso registrado'}
        
        except PRODUCTS.DoesNotExist:
            datos={'mensaje':'Producto no existe'}
        except EMPLOYEES.DoesNotExist:
            datos={'mensaje':'Empleado no existe'}
        except BUSINESS.DoesNotExist:
            datos={'mensaje':'Empresa no existe'}    
        return JsonResponse(datos)
      
        ## actualizar
    def put(self,request,code):
        #crear conexion a body
        data=json.loads(request.body)
        #genero la busqueda con el dato
        ingresos=list(INCOME.objects.filter(ING_Code=code).values())
        #genero la busqueda si hay valores con el dato de busqueda anterior
        if len(ingresos)>0:
            newing=INCOME.objects.get(ING_Code=code)
            newing.ING_Fecha=data['ING_Fecha']
            newing.ING_Quantity=data['ING_Quantity']
            newing.ING_Total=data['ING_Total']

            newing.save()
            
            mensaje={"mensaje":"se a actualizado el ingreso"}
        else:
            mensaje={"mensaje":"no existe el ingreso"}
        return JsonResponse(mensaje)
        
    def delete(self,request,code):      
        ing_cod=list(INCOME.objects.filter(ING_Code=code).values())
        if len(ing_cod)>0:
            INCOME.objects.filter(ING_Code=code).delete()
            mensaje={"mensaje":"Eliminado exitosamente"}
        else:
            mensaje={"mensaje":"No existe el dato"}
        return JsonResponse(mensaje)

class CUSTOMERSView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #Metodo para leer datos
    def get(self,request,user=""):
        #Se verifica si user tiene datos.
        if len(user)>0:   
            clientes= list(CUSTOMERS.objects.filter(CLI_User=user).values())
            if len(clientes)>0:
                #Se muestra el cliente con el user que se ha especificado
                mensaje = {'clientes':clientes, "Mensaje":"Resultado de la busqueda."}
            else:
                mensaje = {'Error': "No se encontró el cliente."}
        else:
            clientes= list(CUSTOMERS.objects.values()) 
            if len(clientes)>0:#se pregunta si hay datos
                #Se muestra todos los clientes existentes en la BD
                mensaje={"clientes":clientes}
            else:
                mensaje={"Error":"No se encontraron clientes."}

        return JsonResponse(mensaje)

    #Metodo para insertar un dato
    def post(self,request):
        dato = json.loads(request.body) 
        try:
            userAdmin=ADMINISTRATOR.objects.get(AD_USER=dato['userAdmin'])
            cliente = CUSTOMERS.objects.create(
                CLI_User=dato['usuario'], 
                CLI_Password=dato['password'],
                CLI_Names=dato['nombre'],
                CLI_LastNames=dato['apellido'], 
                CLI_Email=dato['email'],
                CLI_CellPhone=dato['telefono'],
                CLI_AD_User=userAdmin
                )
            cliente.save()
            mensaje={'mensaje':'Cliente registrado exitosamente'}
        except ADMINISTRATOR.DoesNotExist:
            mensaje={'mensaje':'Código de admin erróneo'}
        return JsonResponse(mensaje)

    #Metodo para actualizar un dato 
    def put(self,request,user):
        data = json.loads(request.body)
        cliente= list(CUSTOMERS.objects.filter(CLI_User=user).values())
        if len(cliente)>0:
            #NOTA:
            #No es necesario actualizar todos los datos, solo los que especifiquemos en este condicional.
            updateData=CUSTOMERS.objects.get(CLI_User=user) #Se trae el objeto que se encontró
            updateData.CLI_Password=data['password']
            updateData.CLI_Names=data['nombre']
            updateData.CLI_LastNames=data['apellido'] 
            updateData.CLI_Email=data['email']
            updateData.CLI_CellPhone=data['telefono']
            updateData.save()
            mensaje={"mensaje":"Cliente actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el cliente."}
            
        return JsonResponse(mensaje)

    #Metodo para borrar un dato
    def delete(self,request,user):
        cliente= list(CUSTOMERS.objects.filter(CLI_User=user).values())
        if len(cliente)>0:
            CUSTOMERS.objects.filter(CLI_User=user).delete()
            mensaje={"mensaje":"Cliente eliminado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontró el Cliente."}
        
        return JsonResponse(mensaje)


class EXPENSESView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,code=""):
        if len(code)>0:   
            egreso= list(EXPENSES.objects.filter(EGR_Code=code).values())
            if len(egreso)>0:
                mensaje = {'egresos':egreso, "Mensaje":"Resultado de la busqueda."}
            else:
                mensaje = {'Error': "No se encontró el egreso indicado."}
        else:
            egreso= list(EXPENSES.objects.values()) 
            if len(egreso)>0:
                mensaje ={"egresos":egreso}
            else:
                mensaje ={"Error":"No hay egresos registrados."}

        return JsonResponse(mensaje)


    def post(self,request):
        data = json.loads(request.body) 
        try:
            NITempresa=BUSINESS.objects.get(EM_NIT=data['NIT_empresa'])          
            egreso = EXPENSES.objects.create(
                EGR_EM_NIT=NITempresa, 
                EGR_Name = data['EGR_Name'],
                EGR_Total = data['EGR_Total']
                )
            egreso.save()
            mensaje={'mensaje':'Egreso registrado exitosamente'}
        except BUSINESS.DoesNotExist:
            mensaje={'mensaje':'NIT empresa erróneo'}
        return JsonResponse(mensaje)

    def put(self,request,code):
        data = json.loads(request.body)
        egreso= list(EXPENSES.objects.filter(EGR_Code=code).values())
        if len(egreso)>0:
            updateData=EXPENSES.objects.get(EGR_Code=code) 
            updateData.EGR_Name = data['EGR_Name']
            updateData.EGR_Fecha = data['EGR_Fecha']
            updateData.EGR_Total = data['EGR_Total']        
            updateData.save()
            mensaje={"mensaje":"Actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontró el egreso indicado."}
            
        return JsonResponse(mensaje)
        
    def delete(self,request,code):
        egreso= list(EXPENSES.objects.filter(EGR_Code=code).values())
        if len(egreso)>0:
            EXPENSES.objects.filter(EGR_Code=code).delete()
            mensaje={"mensaje":"Egreso eliminado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontró el egreso indicado."}         
        return JsonResponse(mensaje)


    
