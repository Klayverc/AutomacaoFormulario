import os
import pyautogui as pg 
import time

arquivos = ""
NomeDaPasta = r"C:\Users\Aluno\Desktop\Klayver python"


def Abrirchrome():
    os.system("start chrome")
    time.sleep(2)

def AbrirFormulario():
    pg.typewrite("https://forms.gle/i3APS9jk55XSV4nh9")
    time.sleep(1)
    pg.press("enter")
    time.sleep(1)

def PreencherFumulario():
    pg.moveTo(621,484, duration=0.8)
    time.sleep(0.5)
    pg.click()
    pg.write("Klayver", interval=0.1)
    time.sleep(0.5)
    pg.moveTo(619,674, duration=0.5)
    time.sleep(0.5)
    pg.click()
    pg.write("programacao em python", interval=0.1)
    time.sleep(0.5)

def abrir_arquivo_para_envia():
    pg.moveTo(683,884, duration=0.8)
    time.sleep(0.5)
    pg.click()
    pg.moveTo(914,781, duration=0.8)
    time.sleep(2)
    pg.click()
    pg.moveTo(1037,57, duration=0.5)
    time.sleep(0.5)
    pg.click()

def ler_arquivo():

    global arquivos
    global NomeDaPasta
    arquivos = os.listdir(NomeDaPasta)  
    arquivos.remove("ex_17.py")
    arquivos.remove("teste 1.py")
    pg.typewrite(arquivos)
    

def seleciona_arquivo(i):

    pg.typewrite(f"{NomeDaPasta}\{arquivos[i]}")
    time.sleep(1)
    pg.press("Enter")
    time.sleep(7)
    for i in range(2):
        pg.press("Tab")
    pg.press("enter")
    time.sleep(4)
    pg.press("Tab")
    time.sleep(0.8)
    pg.press("Enter")


Abrirchrome()
AbrirFormulario()
PreencherFumulario()
ler_arquivo()
for i in range(len(arquivos)):
    PreencherFumulario()
    abrir_arquivo_para_envia()
    seleciona_arquivo(i)