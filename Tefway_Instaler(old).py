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

'''
Classe Cliente no qual vão ser armazenados os dados do cliente e enviar junto do log
'''
class Cliente:
    #Instanciando a classe do cliente
    def __init__(self,nome,cnpj,tipo) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.tipo = tipo
    #Getters dos dados do cliente
    def getNome(self):return self.nome
    def getCnpj(self):return self.cnpj
    def getTipo(self):return self.tipo


#Como Fazer?
#Usar api ou não (A Decidir)
class EnviarLog:
    pass


class Installer:
    """Classe genérica para instalação de executáveis."""
    @staticmethod
    def run_installer(executable_path):
        """Executa o instalador especificado."""
        if sys.platform == 'win32':
            executable_path = executable_path.replace('/', '\\')

        if not os.path.exists(executable_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {executable_path}")

        process = subprocess.Popen([executable_path], stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise Exception(f"Erro no instalador: {stderr}")
        return stdout


class TLS:
    """Função responsável por toda a parte do TLS no programa."""
    @staticmethod
    def instalar():
        """Executa o instalador do TLS."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir,
                                       'Dependencias', 'tls', 'tlscliwl.exe')
        Installer.run_installer(executable_path)

    @staticmethod
    def testar(command):
        """Faz testes na VPN para garantir que a conexão está estável."""
        try:
            result = subprocess.run(command, capture_output=True, 
                                    text=True, shell=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f'Falha no teste com o comando {command}')
        except subprocess.CalledProcessError as e:
            print(e.stderr)


class Gertec:
    """Responsável pela instalação do driver da Gertec."""
    @staticmethod
    def instalar():
        """Executa o instalador do driver da Gertec."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Gertec', 'Gertec-Full-Installer_2.2.2.0.exe')
        Installer.run_installer(executable_path)


class Ingenico:
    """Responsável pela instalação do driver da Ingenico."""
    @staticmethod
    def instalar():
        """Executa o instalador do driver da Ingenico."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Ingenico', 'IngenicoUSBDrivers_3.36_setup_SIGNED.exe')
        Installer.run_installer(executable_path)


class Vx:
    """Responsável pela instalação do driver da VX."""
    @staticmethod
    def instalar():
        """Executa o instalador do driver da VX."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(current_dir, 'Dependencias', 'VX_P200')

        if sys.platform == 'win32':
            base_path = base_path.replace('/', '\\')

        os_platform = platform.architecture()[0]
        installer_path = os.path.join(base_path, '32' if os_platform == '32bit' else '64', 'silent_install_VerifoneUSBDriverUninstall.bat')
        Installer.run_installer(installer_path)


class DLL:
    """Classe para manipulação de DLLs."""
    @staticmethod
    def copy_and_move(dest_path):
        """Copia e move as DLLs para o caminho especificado."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src = os.path.join(current_dir, 'Dependencias', 'DLLL', 'clisitef-7.0.117.83.r1-Producao-Win32')

        if sys.platform == 'win32':
            src = src.replace('/', '\\')

        if not os.path.exists(src):
            raise FileNotFoundError(f"Diretório não encontrado: {src}")

        for file in os.listdir(src):
            shutil.copy2(os.path.join(src, file), os.path.join(dest_path, file))


class Client:
    """Classe responsável pela instalação do Client Sitef."""
    @staticmethod
    def install():
        """Executa o instalador do Client Sitef."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'clientsitef', '7.0.3.1P r1', 'DISK1', 'Instala.exe')
        Installer.run_installer(executable_path)

class Nextar:
    @staticmethod
    def install():
        """Executa o instalador do d-tef Nextar."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Nextar', 'Instalador_Linx_TEF_3.1.3.exe')
        Installer.run_installer(executable_path)


class Seta:
    @staticmethod
    def install():
        """Executa o instalador do d-tef Seta."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Seta', 'Instalador_Linx_TEF_3.1.3.exe')
        Installer.run_installer(executable_path)


class Simulador:
    @staticmethod
    def executar():
        """Executa o instalador do d-tef Seta."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        executable_path = os.path.join(current_dir, 'Dependencias', 'Simulador', 'SiTEF Simulador.exe')
        Installer.run_installer(executable_path)


class Instalacao():
    @staticmethod
    def Sitef():
        """Executa um pipeline que chama todas as classes de instalação do Sitef."""
        try:
            print("Iniciando o instalador TLS:")
            TLS.instalar()
            if input("Continuar com o teste TLS? [S/N]\n:").strip().lower() == 's':
                TLS.testar('netstat -ano | find "4096"')

            Instalacao.InstalarDrivers()

            escolha = input("Instalar DLL (D) ou Client (C)? [D/C]\n:").strip().lower()
            if escolha == 'd':
                path = input("Copie o caminho até a pasta do sistema\n:")
                DLL.copy_and_move(path)
            elif escolha == 'c':
                Client.install()
        except Exception as err:
            print(f"{err}")

    @staticmethod
    def InstalarDrivers():
        while True:
                op = int(input("Instalar qual driver?\n0.Não instalar driver\n1.Gertec\n2.Ingenico\n3.VX\n:"))
                if op == 0:
                    break
                elif op == 1:
                    Gertec.instalar()
                    break
                elif op == 2:
                    Ingenico.instalar()
                    break
                elif op == 3:
                    Vx.instalar()
                    break
                else:
                    print("Opção inválida")        

    @staticmethod
    def Dtef():
            while(True):
                try:
                    op = int(input("Escolha a opção:\n1.Nextar\n2.Seta\n:"))
                    match op:
                        case 1:
                            Nextar.install()
                        case 2:
                            Seta.install()
                        case _:
                            print("Opção Invalida")
                except Exception as err:
                    print("Error na instalação do d-tef -> ", err)

class Run:
    """Classe responsável pela execução do tef_installer."""
    @staticmethod
    def instalacao():
        while(True):
            try:
                #nome = input("Digite o nome do cliente:")
                #cnpj = input("Digite o Cnpj:")
                op = int(input("Escolha a opção:\n1.Sitef\n2.D-TEF\n:"))
                match op:
                    case 1:
                        tipo = "Sitef"
                        Instalacao.Sitef()
                        break
                    case 2:
                        tipo = "D-TEF"
                        Instalacao.Dtef()
                        break
                    case _:
                        print("Opção Invalida!")
                #cliente = Cliente(nome=nome,cnpj=cnpj,tipo=tipo)        
            except Exception as err:
                print("Error no processo de instalação -> ", err) 

    @staticmethod
    def other_pipeline():
        """Executa outras opções de teste e configuração."""
        try:
            op = int(input("Escolha a opção desejada:\n1.Testar VPN\n2.Atualizar DLL\n3.Abrir o simulador Sitef\n4.Instalar driver pin-pad\n:"))
            match op:
                case 1:
                    TLS.testar('netstat -ano | find "4096"')    
                case 2:
                    path = input("Copie o caminho até a pasta do sistema\n:").strip()
                    DLL.copy_and_move(path)
                case 3:
                    Simulador.executar()
                case 4:
                    Instalacao.InstalarDrivers()
        except Exception as err:
            print("Erro:", err)

    @staticmethod
    def init():
        """Ponto de entrada principal para o instalador."""
        try:
            op = int(input("Escolha a opção:\n1.Instalação\n2.Teste, configurações ou atualizações\n:"))
            if op == 1:
                Run.instalacao()
            elif op == 2:
                Run.other_pipeline()
            else:
                print("Opção inválida!")
        except Exception as err:
            print("Erro:", err)


if __name__ == '__main__':
    Run.init()