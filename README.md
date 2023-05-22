# Robotic-Process-Automation-Backup-Google-Drive

Este script em Python utiliza a biblioteca `pyautogui` para automatizar o processo de upload de um arquivo de backup no Google Drive. 

## Funcionamento

1. Exibe um alerta informando que o código começará e que o usuário não deve utilizar o computador durante a execução.
2. Define um intervalo de pausa de 0,2 segundos entre as ações do `pyautogui`.
3. Abre o Google Chrome e navega até o Google Drive.
4. Minimiza todas as janelas para acessar a Área de Trabalho.
5. Seleciona o arquivo de backup na Área de Trabalho (coordenadas específicas devem ser ajustadas de acordo com a localização do arquivo).
6. Anexa o arquivo no Google Drive alternando entre as janelas.
7. Exibe um alerta informando que o código terminou de executar e que o usuário pode voltar a utilizar o computador.

## Dependências

- [pyautogui](https://pypi.org/project/PyAutoGUI/)

# Como Contribuir
- Faça um fork do repositório.
- Crie uma branch com as suas alterações.
- Faça um pull request para a branch principal.
- Agradeço a sua contribuição para este projeto!