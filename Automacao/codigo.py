#Abrir sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Fazer login
#Importar base de dados
#Cadastrar produtos

import pyautogui 
import time
import pandas as pd
#tempo para esperar entre comandos

pyautogui.PAUSE = 0.3

dados = pd.read_csv("produtos.csv")

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

pyautogui.press("tab")
pyautogui.write("email@teste.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("enter")
time.sleep(2)

#for i in range(3):
for i in dados.index:
    pyautogui.click(x=695, y=248)
    #codigo
    pyautogui.write(str(dados.loc[i]["codigo"]))
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(dados.loc[i]["marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(dados.loc[i]["tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(dados.loc[i]["categoria"]))
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(dados.loc[i]["preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(dados.loc[i]["custo"]))
    pyautogui.press("tab")
    #obs
    obs = str(dados.loc[i]["obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(+1000)