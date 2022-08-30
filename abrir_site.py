import os
import webbrowser
import time
from tkinter import *


def Hora_Fim_Semana():
    return str(time.strftime('%w, %H, %M, %S'))

def Hora_Semana():
    return str(time.strftime('%H, %M, %S'))


url_cabeca_de_rede = 'https://mega94.com.br/'
url_ebc = 'https://radios.ebc.com.br/aovivo?emissora=radio-nacional-fm-brasilia'

Hora = Hora_Semana
Hora_FS = Hora_Fim_Semana

Dia_util_6h00 = '05, 59, 30'
Dia_util_6h25 = '06, 25, 30'
Dia_util_6h26 = '06, 26, 00'
Dia_util_6h55 = '06, 55, 30'
Dia_util_11h00 = '10, 59, 30'
Dia_util_11h25 = '11, 25, 00'
Dia_util_11h25_10 = '11, 25, 10'
Dia_util_05h00 = '05, 00, 30'
Dia_FS_06h00 = '6, 59, '

def abrir_fechar_site():
    if Dia_util_6h00 == Hora():
        webbrowser.open_new(url_cabeca_de_rede)
    elif Dia_util_6h25 == Hora():
        os.system('taskkill /im firefox.exe')
    elif Dia_util_6h26 == Hora():    
        webbrowser.open(url_ebc)
    elif Dia_util_6h55 == Hora():
        os.system('taskkill /im firefox.exe')
    elif Dia_util_11h00 == Hora():
        webbrowser.open(url_cabeca_de_rede)
    elif Dia_util_11h25 == Hora():
        os.system('taskkill /im firefox.exe')
    elif Dia_util_11h25_10 == Hora():
        webbrowser.open(url_ebc)
    elif Dia_util_05h00 == Hora():
        os.system('taskkill /im firefox.exe')
    elif Hora() == Hora():
        os.system('cls')
        print('-------Automatic Tassio Time-------')
        print('Hora Local')
        print(Hora())
        print('Rádio Marinha Pantanal 105,9FM')


countTimer = 0
sleepTime = 1.000
while time.time():
    time.sleep(sleepTime)
    countTimer += sleepTime
    abrir_fechar_site()


