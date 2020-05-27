import PySimpleGUI as sg 
import time, random
num='000'
lista_num = []
intentos = 10
gano = False #Controla el juego
def instrucciones (): 
    return '¡¿Qué cómo se juega?! ¡¡¡No puede ser!!! \nEs muy sencillo. La computadora pensará un número de 4 (cuatro) dígitos al azar. \nNinguna de estos estará repetido \n Deberás escribir un número de 3 (tres) dígitos. \nLa computadora te dirá cuántos adivinaste CORRECTAMENTE y cuáles están bien pero MAL UBICADOS\nBuena suerte!!'
sg.theme ('Dark Purple6')

contenido = [ 
    [sg.Text ('BIENVENIDE AL JUEGO DE ADIVINAR EL NÚMERO',size=(40,2),justification='center',font=('Impact',20),text_color='gray')],
    [sg.Text(instrucciones(),size = (47,7),justification='center',font=('Arial',15),text_color='white',key='instrucciones')],
    [sg.Text ('Ingrese 3 dígitos:', size = (18,1), justification='left',font=('Arial',10)),sg.InputText(key='_numJugador_',size=(5,1)),sg.Button('Probemos'),sg.Text(key='lista_num',size=(9,5))],
    [sg.Text ('Números Correctos:', size = (19,1),font=('Arial',10)),sg.Text(key='_ok_'),sg.Text ('Números Mal ubicados: ', size = (22,1),font=('Arial',10)),sg.Text(key='_mal_')],
    [sg.Text ('Número secreto:', size = (18,1), justification='left',font=('Arial',10)),sg.Text(size=(4,1),key='_DISPLAY_'),sg.Text(size = (4,1)),sg.Text(size=(4,1),key='_vidas_')],
    [sg.Text ('', size = (10,1)),sg.Text (size = (15,1),justification='center',font=('Arial',30),text_color='white',key='_ganador_')],
    [sg.Button('Nuevo Numero Secreto'),sg.Text ('', size = (40,1)),sg.Button('Salir')] 
    ]
#Imprime numero secreto
def actualizar_pantalla(valor_pantalla:str):
    try:
        ventana['_DISPLAY_'].update(value='{}'.format(valor_pantalla))
    except:
        ventana['_DISPLAY_'].update(value=valor_pantalla)

def actualizar_ok(valor_pantalla:str):
    try:
        ventana['_ok_'].update(value='{}'.format(valor_pantalla))
    except:
        ventana['_ok_'].update(value=valor_pantalla)
#Imprime cantidad de intentos restantes
def actualizar_vidas():
    try:
        ventana['_vidas_'].update(value=str(intentos))
    except:

        
        ventana['_vidas_'].update(value=valor_pantalla)
#Imprime si ganó o perdió
def actualizar_ganador(valor):
    try:
        ventana['_ganador_'].update(value=valor)
    except:
        ventana['_ganador_'].update(value=valor_pantalla)
#Imprime números mal ubicados
def actualizar_mal(valor_pantalla:str):
    try:
        ventana['_mal_'].update(value='{}'.format(valor_pantalla))
    except:
        ventana['_mal_'].update(value=valor_pantalla)

def ver_ganador(ok):    
    global intentos
    global gano
    if (intentos > 0) and (ok == 3): #Si acertó todas, ganó y finaliza flujo
        actualizar_ganador('GANASTE')
        gano = True
    else:            
        intentos = intentos - 1
        actualizar_vidas()
        if intentos == 0: #Imprime perdiste y finaliza el flujo
            actualizar_ganador('PERDISTE')
            actualizar_pantalla(num)
            gano = True
#Imprime números ya utilizados       
def actualizar_lista_numeros(valor_pantalla:str):
    try:
        ventana['lista_num'].update(value=valor_pantalla)
    except:
        ventana['lista_num'].update(value=valor_pantalla)
#Evalúa los números elegidos con el número secreto, dígito a dígito
def validar():
    casi = 0
    ok = 0
    listado='' 
    numJugador = values['_numJugador_']    
    if len(numJugador)==3:
        for i in range(3):
            if numJugador[i] == num[i]:
                ok= ok +1
            elif numJugador[i] in num:
                casi = casi +1  
        lista_num.append(str(numJugador))
        for i in range(len(lista_num)):
            listado = listado + ' | '+ str(lista_num[i])
        actualizar_lista_numeros (listado)
        actualizar_ok(ok)
        actualizar_mal(casi)
        ventana['_numJugador_'].update(value='')        
        ver_ganador(ok)
#Crea número secreto
def num_secreto():
    global num
    global intentos 
    num=''
    numeros=(list(range(10)))
    random.shuffle(numeros)
    for i in range(3):
        num += str(numeros[i])
    return num
#Inicializa la interfaz y las variables
def inicializar(num):
    global intentos
    global lista_num 
    global gano
    gano = False   
    lista_num=[]
    actualizar_lista_numeros ('')
    intentos = 10
    actualizar_pantalla('***')
    actualizar_ganador('')
    actualizar_vidas()

ventana = sg.Window('Adivinando el Número', layout=contenido)

while True:
    event, values = ventana.read()
    if num =='000':
        num_secreto()
    if event in (None, 'Salir'):	# Salir, cierra ventana
        break
    if event == 'Nuevo Numero Secreto':
        num_secreto()
        inicializar(num)
    if gano == False:
        if event == 'Probemos':
            validar ()
    elif (intentos < 0) and (gano == False):
            num_secreto()
            inicializar(num)
ventana.close()