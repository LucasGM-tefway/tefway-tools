"""
Nome do arquivo: tef_installer
Autor: Lucas Guimaraes Moreira & qualquer um que quiser contribuir
Versão: 1.0.4
Data de criação: 19 de abril de 2024
Descrição: Este arquivo é a automação de uma instalação tef, Exemplo: instalar tls, instalar driver, copiar as dll's
Referencias:
  -  https://docs.python.org/3/library/subprocess.html
  -  https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw
  -  https://docs.python.org/3/library/shutil.html
  -  https://docs.python.org/3/library/os.html
  -  https://docs.python.org/3/library/sys.html
  -  https://wiki.winehq.org/Developers
"""
import shutil
import subprocess
import os
import sys
import platform


class utils:
    def ajustar_path(tipo,executavel):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, 'Dependencias', tipo, executavel)

class executable:
    def run_exe(executable_path):
        
        if not os.path.exists(executable_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {executable_path}")

        process = subprocess.Popen([executable_path], stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise Exception(f"Erro no instalador: {stderr}")
        return stdout


class test:
    def test_tls(command):
        try:
            result = subprocess.run(command, capture_output=True, 
                                    text=True, shell=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f'Falha no teste com o comando {command}')
        except subprocess.CalledProcessError as e:
            print(e.stderr)


class dependecy:
    def tls():executable.run_exe(utils.ajustar_path('tls','tlscliwl.exe'))


    def gertec():executable.run_exe(utils.ajustar_path('Gertec', 'Gertec-Full-Installer_2.2.2.0.exe'))


    def ingenico():executable.run_exe(utils.ajustar_path('Ingenico', 'IngenicoUSBDrivers_3.36_setup_SIGNED.exe'))


    def vx():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(current_dir, 'Dependencias', 'VX_P200')

        if sys.platform == 'win32':
            base_path = base_path.replace('/', '\\')

        os_platform = platform.architecture()[0]
        executable_path = os.path.join(base_path, '32' if os_platform == '32bit' else '64', 'silent_install_VerifoneUSBDriverUninstall.bat')
        executable.run_exe(executable_path=executable_path)


    def dll(dest_path):
        """Copia e move as DLLs para o caminho especificado."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src = os.path.join(current_dir, 'Dependencias', 'DLLL', 'clisitef-7.0.117.83.r1-Producao-Win32')

        if sys.platform == 'win32':
            src = src.replace('/', '\\')

        if not os.path.exists(src):
            raise FileNotFoundError(f"Diretório não encontrado: {src}")

        for file in os.listdir(src):
            shutil.copy2(os.path.join(src, file), os.path.join(dest_path, file))

    def client():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'clientsitef', '7.0.3.1P r1', 'DISK1', 'Instala.exe')
        executable.run_exe(executable_path=executable_path)


    def simulator():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Simulador', 'SiTEF Simulador.exe')
        executable.run_exe(executable_path=executable_path)


    def seta():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Seta', 'Instalador_Linx_TEF_3.1.3.exe')
        executable.run_exe(executable_path=executable_path)

    
    def nextar():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Nextar', 'Instalador_Linx_TEF_3.1.3.exe')
        executable.run_exe(executable_path=executable_path)



class pipelines:
    def install_sitef():
        try:
            dependecy.tls()
            op = int(input("Testar tls\n1.Sim\n2.Não\n:"))
            match op:
                case 1:test.test_tls('netstat -ano | find "4096"')
                case 2:pass
                case _:print("Opção Invalida!")
            while(True):
                op = int(input("Digite a opção do driver\n1.Gertec\n2.Ingenico\n3.VX\n0.nenhum\n:"))
                match op:
                    case 0:
                        break
                    case 1:
                        dependecy.gertec()
                        break
                    case 2:
                        dependecy.ingenico()
                        break
                    case 3:
                        dependecy.vx()
                        break
                    case _:
                        print("Opção invalida!")
            op = input("Instalar DLL (D) ou Client (C)? [D/C]\n:").strip().lower()
            if op == 'd':
                path = input("Copie o caminho até a pasta do sistema\n:")
                dependecy.dll(path)
            elif op == 'c':
                dependecy.client()         
        except Exception as err:
            print("Error no pipeline sitef:",err)        

    def install_dtef():
        try:
            while(True):
                op = int(input("Digite a opção:\n1.Seta\n2.Nextar\n:"))
                match op:
                    case 1:
                        dependecy.seta()
                    case 2:
                        dependecy.nextar()
                    case _:
                        print("Opção invalida")
        except Exception as err:
            print("Error no pipeline d-tef:", err)       

    def updateDll():
        path = input("Copie o caminho até a pasta do sistema\n:")
        dependecy.dll(path)   

    def configClient():
        dependecy.simulator()
                   

class install:
    def run():
        try:
            while(True):
                op = int(input("Digite a opção:\n0.Finalizar\n1.Instalar sitef\n2.instalar d-tef\n3.atualizar dll\n4.configurar cliente\n5.testar tls\n:"))
                match op:
                    case 1:
                        pipelines.install_sitef()
                    case 2:
                        pipelines.install_dtef()
                    case 3:
                        pipelines.updateDll()
                    case 4:
                        pipelines.configClient()
                    case 5:
                        test.test_tls('netstat -ano | find "4096"')   
                    case _:
                        print("Opção invalida")
        except Exception as err:
            print("Error no pipeline d-tef:", err) 


if __name__ == '__main__':
    install.run()