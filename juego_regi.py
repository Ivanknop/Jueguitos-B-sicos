import PySimpleGUI as sg 
import random, time
from playsound import playsound
#listas de letras y de colores disponibles
letras = ['a','e','i','o','u','r','l','m','n','g','p','s','t']
colores = ['green','yellow','blue','red',]
l_claves = ['0','1','2','3']
CANT_BOTONES = 4
botones = [] #lista de botones 
BIEN = "sonidos\Cut_bien.mp3"

class boton_colores():
    def __init__ (self,clave,color:str):  
        self.name = ''
        self.clave = clave
        self.color = color
        self.disabled = False
        self.key = clave
        self.font = ('Impact',40)
        self.button_color = ('black',color)    
        self.button = sg.Button(self.name,size=(10,2),
                        disabled=self.disabled,font = self.font,key=self.key,
                        button_color= self.button_color,
                        focus=True,
                        pad=(1,1))

    def get_L (self):
        return self.name

    def get_key(self): #lo uso para acceder al boton pero creo es innecesario
        return self.key
    
    def get_color (self): #esto hay que estudiarlo
        return self.button_color[1]
    
    def set_L (self,letra:str):
        self.name = letra.upper()
        self.button.update(self.name)
    
    def set_color (self,color:str):
        self.button.update(button_color=('white',color))

def ver_correcto(l_boton:str,l_paño):
    if l_boton.lower() == l_paño:
        return True
    else:
        return False

def actualizar_letra(lista):
    random.shuffle(lista)
    ventana['_letra'].update(value='{}'.format(lista[0]).upper())

def mezclar_letras(botones):
    random.shuffle(letras)
    rango_letras =[]
    for i in range(len(botones)):
        botones[i].set_L(letras[i])
        rango_letras.append(letras[i])
    actualizar_letra(rango_letras)
    return rango_letras

def inicializar(botones,ok): #solo mezcla los colores la primera vez que se abre el juego
    if ok == False:
        random.shuffle(colores)
        for i in range(len(botones)):            
            botones[i].set_color(colores[i])
    l_e = mezclar_letras(botones)
    return l_e[0]

#creo los botones
for i in range(CANT_BOTONES): 
    a = boton_colores(l_claves[i],'black')
    botones.append(a)

#Diseño de la interfaz
col1 = [
    [botones[0].button],[botones[1].button],
    [sg.Button ('Empezar',size = (10,2),key = 'Empezar')]
]
col3 = [
    [botones[2].button],[botones[3].button]
        ]
col2 = [
    [sg.Text('',size = (50,15),font = ('Impact', 150),text_color=('black'),key='_letra')]
    ]
ven = [
    [sg.Column(col1),sg.Column(col3),sg.Column(col2)],
        ]
listo = False
ventana = sg.Window ('Juego Regi',layout = ven,size=(800,400),return_keyboard_events=True)
dimensiones = ventana.GetScreenDimensions()
while True:    
    event, values = ventana.read()
    if event == None:
        break
    elif event == 'Empezar':
        l = inicializar(botones,listo)
        listo= True
    elif event in letras:
        ok = ver_correcto(event,l)
        if ok == True:  
            playsound (BIEN)
            l = inicializar(botones,ok)
    elif (event== botones[0].get_key()):
        print (event== botones[0].get_key())
        ok = ver_correcto(botones[0].get_L(),l)
        if ok == True:            
            l = inicializar(botones,ok)
            playsound (BIEN)
    elif (event== botones[1].get_key()):   
        
        print (event== botones[1].get_key()) 
        ok = ver_correcto(botones[1].get_L(),l)
        if ok == True:  
            playsound (BIEN)            
            l = inicializar(botones,ok)
    elif (event== botones[2].get_key()):  
        
        print (event== botones[2].get_key())  
        ok = ver_correcto(botones[2].get_L(),l)
        if ok == True:              
            l = inicializar(botones,ok)
            playsound (BIEN)
    elif (event== botones[3].get_key()): 
        
        print (event== botones[3].get_key())   
        ok = ver_correcto(botones[3].get_L(),l)
        if ok == True:            
            l = inicializar(botones,ok)
            playsound (BIEN)

ventana.close()

