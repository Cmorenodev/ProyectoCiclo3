from django.urls import path
from Supermercado.views import *
from Supermercado.viewsFrontend import *
from Supermercado.viewsLogin import *
urlpatterns = [

    #URLS PARA EL BACKEND
    path('ADMINISTRATOR/',ADMINISTRATORView.as_view(),name='ListarAdministrador'),
    path('ADMINISTRATOR/<str:AD_USER>',ADMINISTRATORView.as_view(),name='ListarAdministradorPorUsuario'),
    path('BUSINESS/',BUSINESSView.as_view(),name='ListarBusiness'),
    path('BUSINESS/<int:EM_nit>',BUSINESSView.as_view(),name='ListarBusiness'),
    path('EMPLOYEES/',EMPLOYEESView.as_view(),name='Listarempleados'),
    path('EMPLOYEES/<str:EMP_User>',EMPLOYEESView.as_view(),name='Listarempleadosporusuario'),
    path('Employeepayroll/',EMPLOYEEPAYROLLView.as_view(),name='Listarnomina'),
    path('Employeepayroll/<int:PAY_id>',EMPLOYEEPAYROLLView.as_view(),name='ListarID'),
    path('WORKINGHOURS/',EMPLOYEEPAYROLLView.as_view(),name='Listarhours'),
    path('WORKINGHOURS/<str:WORH_code>',EMPLOYEEPAYROLLView.as_view(),name='ListarHo'),
    path('CUSTOMERS/',CUSTOMERSView.as_view(),name='ListarCliente'),
    path('CUSTOMERS/<str:user>',CUSTOMERSView.as_view(),name='ListarClientePorUsuario'),
    path('LISTBUY/',LISTBUYView.as_view(),name='ListarListCompra'),
    path('LISTBUY/<str:LBUY_Code>',LISTBUYView.as_view(),name='ListarPorCodigo'),
 
    path('EXPENSES/',EXPENSESView.as_view(),name='ListarEgresos'),
    path('EXPENSES/<str:code>',EXPENSESView.as_view(),name='BuscarEgresos'),
    path('INCOME/',INCOMEView.as_view(),name='ListarIngresos'),
    path('INCOME/<str:code>',INCOMEView.as_view(),name='BuscarIngresos'),
    path('PRODUCTS/',PRODUCTSView.as_view(),name='ListarProductos'),
    path('PRODUCTS/<str:code>',PRODUCTSView.as_view(),name='BuscarProductos'),    


    #URLS PARA EL FRONTEND

    path('catalogo/',Catalogo,name="catalogo"),
    path('',index,name="index"),
    path('login/',login2,name="login"),
    
    path('ins_listCompra/',ins_listCompra,name="ins_listCompra"),
    path('listaCompra/<str:usuario>',listCompra,name="listCompra"),
    path('listaCompra_eli/<str:usuario>',listCompra_eli,name="eliLis"),
    path('ingresar/', iniciarsesion, name="ingresar"),
    path('cerrar/', cerrarsesion, name="cerrar"),

    path('comprar/<str:usuario>',comprar,name="comprar"),

    path('MenuAdmin/', menuAdmin, name="MenuAdmin"),
    path('MenuEmpleado/', menuEmpleado, name="MenuEmpleado"),

     #URLs PARA LA TABLA CLIENTES
    path('ListaClientes/', listaClientes, name='ListaClientes'),
    path('BuscarCliente/', buscarCliente, name='BuscarCliente'),
    path('FormCliente/', formRegistroCliente, name='FormCliente'),
    path('RegistrarCliente/',registrarCliente, name='RegistrarCliente'),
    path('FormEditarCliente/<str:usuario>', formEditarCliente, name='FormEditarCliente'),
    path('ActualizarCliente/',editarCliente, name='ActualizarCliente'),
    path('EliminarCliente/<str:usuario>',eliminarCliente, name='EliminarCliente'),

    path('ListaClientesEMP/', listaClientesEMP, name='ListaClientesEMP'),
    path('BuscarClienteEMP/', buscarClienteEMP, name='BuscarClienteEMP'),
    
    #URLs PARA LA TABLA INGRESOS
    path('ListaIngresos/', listaIngresos, name='ListaIngresos'),
    path('BuscarIngreso/', buscarIngreso, name='BuscarIngreso'),
    path('FormIngreso/', formRegistroIngreso, name='FormIngreso'),
    path('RegistrarIngreso/',registrarIngreso, name='RegistrarIngreso'),
    path('FormEditarIngreso/<str:codigo>', formEditarIngreso, name='FormEditarIngreso'),
    path('ActualizarIngreso/',editarIngreso, name='ActualizarIngreso'),

    path('EliminarIngreso/<str:codigo>',eliminarIngreso, name='EliminarIngreso'),

    # #URLs PARA LA TABLA EGRESOS
    path('ListaEgresos/', listaEgresos, name='ListaEgresos'),
    path('BuscarEgreso/', buscarEgreso, name='BuscarEgreso'),
    path('FormEgreso/', formRegistroEgreso, name='FormEgreso'),
    path('RegistrarEgreso/',registrarEgreso, name='RegistrarEgreso'),
    path('FormEditarEgreso/<str:codigo>', formEditarEgreso, name='FormEditarEgreso'),
    path('ActualizarEgreso/',editarEgreso, name='ActualizarEgreso'),
    path('EliminarEgreso/<str:codigo>', eliminarEgreso, name='EliminarEgreso'),

    # #URLs PARA LA TABLA PRODUCTOS
    path('ListaProductos/', listaProductos, name='ListaProductos'),
    path('BuscarProducto/', buscarProducto, name='BuscarProducto'),
    path('FormProducto/', formRegistroProducto, name='FormProducto'),
    path('RegistrarProducto/',registrarProducto, name='RegistrarProducto'),
    path('FormEditarProducto/<str:codigo>', formEditarProducto, name='FormEditarProducto'),
    path('ActualizarProducto/',editarProducto, name='ActualizarProducto'),
    path('EliminarProducto/<str:codigo>', eliminarProducto, name='EliminarProducto'),


    # #URLs PARA LA TABLA EMPRESAS
    path('ListaEmpresas/', listaEmpresas, name='ListaEmpresas'),
    path('BuscarEmpresa/', buscarEmpresa, name='BuscarEmpresa'),
    path('FormEmpresa/', formRegistroEmpresa, name='FormEmpresa'),
    path('RegistrarEmpresa/',registrarEmpresa, name='RegistrarEmpresa'),
    path('FormEditarEmpresa/<str:EM_NIT>', formEditarEmpresa, name='FormEditarEmpresa'),
    path('ActualizarEmpresa/',editarEmpresa, name='ActualizarEmpresa'),
    path('EliminarEmpresa/<str:EM_NIT>', eliminarEmpresa, name='EliminarEmpresa'),
    
    
    
    ###empleados
    path('ListaDeEmpleados/',ListarEmpleados, name="ListarEmpleados"),
    path('BuscarEmpleados/',ListaDeEmpleadosuser, name="BuscarEmpleados"),
    path('eliminar/<str:EMP_User>',EliminarEmpleados,name="eliminar"),
    path('FormularioAgregarEmpleado/',CrearEmpleado,name="CrearEmpleado"),
    path('GuardarEmpleado/',GuardarEmpleado,name="GuardarEmpleado"),
    path('Cargarform/<str:EMP_User>',CrearFormulario,name="Carfor"),
    path('EditarFormularioEmpleado/',EditarEmpleado,name="Editar"),


]