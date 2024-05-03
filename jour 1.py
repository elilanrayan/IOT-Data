from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pins de sortie et de modulation du signal
import utime # importe dans le code la lib qui permet de gerer le temps
import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json


import time # importe dans le code la lib qui permet de gerer le temps

ledpin=[17,18,19] # declaration d'une variable pinNumber à 17

leds = []

maisons = {"Gryffindor" : [255,0,0] , "Slytherin" : [0,255,0] , "Ravenclaw" : [0,0,255] , "Hufflepuff" : [255,255,0]}

            
#pin_button = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP) # declaration d'une variable de type pin ici la 14 
                                                    #et on prescise que c'est une pine d'entré de courant (IN)


for i in ledpin :
    leds.append(PWM(Pin(i,mode=Pin.OUT)))


"""for i in ledpin :
    leds.append(Pin(i,mode=Pin.OUT))


while True:
    print(pin_button.value()) # on envoie la valeur du bouton
    utime.sleep(.1)            # on attend 0.1 seconde
    for i in leds:
        if pin_button.value()==1 :
                i.on()
                utime.sleep(.5)
                i.off()
lastDataButton =1
while True :
    if pin_button.value() == 0 and lastDataButton ==1 :
        leds[0].toggle()
    lastDataButton = pin_button.value()
    utime.sleep(.1)"""
                
   




"""pwm_led = PWM(Pin(17,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_led.freq(1_000) # dont la frequence est de 1000 (default)
pwm_led.duty_u16(13000) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v
duty = 13000
while True :
    for i in range(200):
        pwm_led.duty_u16(i*100)
        time.sleep(0.1)
    for i in range (200):
        pwm_led.duty_u16(2000-i*100)
        time.sleep(0.1)"""



for i in leds:
    i.freq(1_000)
    i.duty_u16(0)

def off() :
    for i in leds :
        i.duty_u16(0)

def on() :
    for i in leds:
        i.duty_u16(9000)



def setColor(c):
    for led, color_value in zip(leds, c):
        led.duty_u16(color_value*50)
        utime.sleep(0.5)
        led.duty_u16(color_value*10)
        
       
        

    
wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Kskvkdkckf'
password = 'azerty123'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://192.168.214.43:3000/"

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        couleur = r.json()['message']
        setColor(maisons[couleur])
        print(r.json()['message']) # traite sa reponse en Json
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)


setColor(maisons[couleur])