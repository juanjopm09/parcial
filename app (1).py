#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json 

URL= "http://127.0.0.1:5000/students/"

def metodo_GET():
    datajson = requests.get(URL)
    datapy = json.loads(datajson.text)
    datapy = datapy['students']
    for i in range (len(datapy)):
        print(
            "\t" ,datapy[i]['name'],
            "\n\t" ,datapy[i]['id'],
            "\n\t" , datapy[i]['course']
        )
def metodo_GET_one(ID):
    datajson = requests.get(URL+ID)
    datapy = json.loads(datajson.text)
    datapy = datapy['est']
    print(
        "\t" ,datapy[0]['name'],
        "\n\t" ,datapy[0]['id'],
        "\n\t" , datapy[0]['course']
    )
def metodo_POST(name, course, ID):
    datapy = {
        'id': ID,
        'name': name,
        'course': course        
    }
    requests.post(URL, json = datapy)
def metodo_DELETE(ID):
    requests.delete(ID)


def metodo_PUT(name, course, ID):
    datapy = {
        'name': name,
        'course': course,
    }
    requests.put(URL+ID, json= datapy)

def opc1():
    print("\t\tBienvenido, ¿Que accion deseas tomar?")
    print("\t\t1. Ver Facturas.")
    print("\t\t2. Buscar Facturas.")
    print("\t\t3. Eliminar.")
    print("\t\t4. Agregar Factura de cliente.")
    print("\t\t5. Editar.")
    print("6. Salir.")
while True: 
    opc1()
    try:
        opc = int(input(">"))
        if opc in range(7):
            if opc == 1: 
                metodo_GET()
            if opc == 2: 
                codigo= input("Cedula de Ciudadania: ")
                metodo_GET_one(codigo)
            if opc == 3:
                codigo= input("Cedula de Ciudadania: ")
                metodo_DELETE(codigo)
            if opc == 4: 
                codigo = input("Cedula de Ciudadania: ")
                nombre = input("Nombre y apellido: ")
                curso = input("Fecha, direccion y codigo postal: ")
                metodo_POST(nombre, curso, codigo)
                metodo_GET_one(codigo)
            if opc == 5:
                codigo = input("Cedula de Ciudadania:  ")
                metodo_GET_one(codigo)
                nombre = input("Nombre y apellido: ")
                curso = input("Fecha y direccion: ")
                metodo_PUT(nombre, curso, codigo)
                metodo_GET_one(codigo)
            if opc == 6:
                break
        else:
                print('Opción invalida')
    except ValueError:
        print("Error, ingrese solamente numeros")
                
                
                
                
                
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




