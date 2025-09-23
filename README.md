# 🤖 Automação com Python (PyAutoGUI + OpenCV)

Este projeto é um exemplo prático de como a automação pode facilitar tarefas repetitivas do dia a dia.  
O script utiliza **PyAutoGUI** para interações com a tela, **OpenCV** para reconhecimento de imagens e **PyInstaller** para gerar um executável simples de rodar.

---

## 🚀 Funcionalidades
- Abre automaticamente o navegador.
- Realiza login no sistema da empresa.
- Navega até menus e botões específicos.
- Acessa o WhatsApp Web.
- Usa reconhecimento de imagens com **OpenCV** para localizar elementos na tela.
- Possui plano B (fallback) com coordenadas fixas caso a imagem não seja encontrada.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **PyAutoGUI** → Automação de teclado e mouse.
- **OpenCV** → Reconhecimento e tratamento de imagens.
- **Pillow** → Suporte para manipulação de imagens.
- **PyInstaller** → Empacotamento em executável (.exe).

---

## 📂 Estrutura do Projeto

📦 automacao-pyautogui
┣ 📜 codigo.py # Script principal da automação
┣ 📂 imagens # Capturas de tela (botões/ícones a localizar)
┣ 📜 requirements.txt # Dependências do projeto
┗ 📜 README.md # Documentação do projeto


---

## ⚙️ Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/automacao-pyautogui.git
   cd automacao-pyautogui

2. Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

3. Execute o script:

python codigo.py
```

📦 Gerar Executável

Para transformar em um executável simples (Windows):
```
pyinstaller --onefile --noconsole codigo.py
```

🎯 Próximos Passos

Melhorar reconhecimento de imagens com técnicas avançadas do OpenCV.

Adicionar logs mais detalhados (ex.: tempo de execução, tentativas de reconhecimento).

Criar interface gráfica (GUI) para configuração sem mexer no código.

Evoluir para automações integrando APIs e Inteligência Artificial.
