# Passo a passo para desenvolver um código que faça o cadastro de vários podutos de
# uma determinada base de dados:
# Passo 1 - Entrar no sistema
# Passo 2 - Fazer login 
# Passi 3 - Importar base de dados
# Passo 4 - Cadastrar um produto 
# Passo 5 - Repetir o cadastro até que acabem todos os produtos

import pyautogui
import time

#utilizado para dar uma pausa a cada comando realizado
pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no sistema
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# Entrar no link do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2 - Fazer login 
# Selecionar o campo do e-mail e apagar qualquer texto caso haja algum
pyautogui.click(x=625, y=451)
pyautogui.hotkey("ctrl", "a")

# Escrever o e-mail, senha e logar
pyautogui.write("eduardateste@gmail.com")
pyautogui.press("tab")
pyautogui.write("T@ylor")
pyautogui.press("tab")
pyautogui.press("enter")

# Passi 3 - Importar base de dados
import pandas as pd 
tabela = pd.read_csv("produtos.csv")

#exibir a tabela (base de dados) importada
print(tabela)

# Passo 4 - Cadastrar um produto        
for linha in tabela.index:
    # Selecionar o campo de código
    pyautogui.click(x=780, y=368)
    
    # Pegar na tabela o valor do campo que será preenchido
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
   
   # Marca
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
            pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Dar scroll para o início da página
    pyautogui.scroll(4000)

# Passo 5 - Repetir o cadastro até que acabem todos os produtos (todas as linhas da tabela)
# Rodando o for(looping)
