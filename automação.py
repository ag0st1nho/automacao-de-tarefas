import pyautogui
import pandas as pd
import time

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.PAUSE = 0.9 
time.sleep(1.0)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.press("tab")

pyautogui.write("email.123@gmail.com")
pyautogui.press("tab")

pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")


tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]    
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]    
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = tabela.loc[linha, "categoria"]    
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco_unitario = tabela.loc[linha, "preco_unitario"]    
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]    
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.click(x=1983, y=284)
