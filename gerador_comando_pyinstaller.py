import os

# Caminho para o diretório do UPX
upx_dir = "C:/Users/jkai/OneDrive/Área de Trabalho/upx-4.2.4-win64"

# Caminho para a pasta a ser excluída da compactação UPX
pasta_a_excluir = "Dependencias/DLLL/clisitef-7.0.117.83.r1-Producao-Win32"

# Caminho para o ícone
icone = "Dependencias/Tefway.ico"

# Arquivo Python principal
script_principal = "tefway_tools.py"

# Listar todos os arquivos na pasta a ser excluída
arquivos_a_excluir = []
for root, dirs, files in os.walk(pasta_a_excluir):
    for file in files:
        arquivos_a_excluir.append(os.path.join(root, file))

# Construir o comando PyInstaller
comando_pyinstaller = (
    f'pyinstaller --clean --onefile --add-data "Dependencias;Dependencias" '
    f'--icon="{icone}" --upx-dir="{upx_dir}" '
)

# Adicionar arquivos a serem excluídos do UPX
for arquivo in arquivos_a_excluir:
    comando_pyinstaller += f'--upx-exclude "{arquivo}" '

# Adicionar o script principal
comando_pyinstaller += f'{script_principal}'

# Imprimir o comando para ser executado no terminal
print(comando_pyinstaller)