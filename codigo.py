import pyautogui
import time

def clicar_imagem(img, nome, espera=1, posicao_alternativa=None, tentativas=3, intervalo=1):
    """
    Clica em uma imagem na tela usando PyAutoGUI.
    Tenta localizar a imagem várias vezes antes de recorrer à posição alternativa.
    
    :param img: Caminho da imagem a ser encontrada
    :param nome: Nome da ação (para log)
    :param espera: Tempo para esperar após o clique
    :param posicao_alternativa: Tupla (x, y) para clique alternativo
    :param tentativas: Quantas vezes tentar localizar a imagem antes de usar a alternativa
    :param intervalo: Tempo entre tentativas
    """
    posicao = None
    for i in range(tentativas):
        try:
            posicao = pyautogui.locateOnScreen(img, confidence=0.7)
            if posicao:
                pyautogui.click(posicao)
                print(f"[OK] Clique realizado em: {nome} (imagem encontrada na tentativa {i+1})")
                time.sleep(espera)
                return
        except pyautogui.ImageNotFoundException:
            pass  # ignora erro e continua tentando

        time.sleep(intervalo)

    # Se não encontrou após várias tentativas, usa a posição alternativa
    if posicao_alternativa:
        pyautogui.click(posicao_alternativa)
        print(f"[Alerta] {nome} não encontrado após {tentativas} tentativas. Clique realizado na posição alternativa {posicao_alternativa}.")
    else:
        print(f"[Erro] {nome} não encontrado e nenhuma posição alternativa definida.")

    time.sleep(espera)

# Exemplo de uso:

# Abrir Chrome
pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)

clicar_imagem("chrome_aberto.png", "Chrome aberto", espera=2, posicao_alternativa=(788, 401))

# Acessar site
pyautogui.write('https://sso.dimsport.com/login')
pyautogui.press('enter')
time.sleep(3)

# Botão login
clicar_imagem("img1.png", "Botão login", espera=2, posicao_alternativa=(637, 510))

# Menu Race
clicar_imagem("img2.png", "Menu Race", espera=2, posicao_alternativa=(550, 369))

# Tickets
clicar_imagem("img3.png", "Tickets", espera=2, posicao_alternativa=(77, 364))

# Finalizar ação
clicar_imagem("img4.png", "Finalizar", espera=2, posicao_alternativa=(610, 750))



