import subprocess
import os
import shutil

class Dependency:
    @staticmethod
    def tls():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'tls', 'tlscliwl.exe'))
    @staticmethod
    def gertec():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'Gertec', 'Gertec-Full-Installer_2.2.2.0.exe'))
    @staticmethod
    def ingenico():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'Ingenico', 'IngenicoUSBDrivers_3.36_setup_SIGNED.exe'))
    @staticmethod
    def vx():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'VX_P200', '32', 'silent_install_VerifoneUSBDriverUninstall.bat'))
    @staticmethod
    def lane():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'Lane 3000', 'IngenicoUSBDrivers_3.34_setup_SIGNED.exe'))
    @staticmethod
    def simulator():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'Simulador', 'SiTEF Simulador.exe'))
    @staticmethod
    def client():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'clientsitef', '7.0.3.1P r1', 'DISK1', 'Instala.exe'))
    @staticmethod
    def dtef():Utils.run_exe(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'DTEF', 'Instalador_Linx_TEF_3.1.4.exe'))
    @staticmethod
    def dll(dest_path):
        src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'DLLL', 'clisitef-7.0.117.83.r1-Producao-Win32')
        for file in os.listdir(src):
            shutil.copy2(os.path.join(src, file), os.path.join(dest_path, file))

class Utils:
    @staticmethod
    def run_exe(executable_path):
        process = subprocess.Popen([executable_path], stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise Exception(f"Erro na execução do executável: {stderr}")
        return stdout

    @staticmethod
    def restart_service(service_name):
        subprocess.run(f"net stop {service_name}", shell=True)
        subprocess.run(f"net start {service_name}", shell=True)
   

    @staticmethod
    def test_tls():return subprocess.run(r'netstat -ano | find "4096"', capture_output=True,text=True, shell=True)    

    @staticmethod
    def pinpad():
        option = input("Escolha o PinPad\nGertec(G)\nIngenico(I)\nLane3000(L)\nVX_P2000(V)\n:").strip().lower()
        while(True):
            match option:
                case 'g':Dependency.gertec();break
                case 'i':Dependency.ingenico();break
                case 'l':Dependency.lane();break
                case 'v':Dependency.vx();break
                case _:print("Opção Invalide")

    @staticmethod
    def configurate_client():
        print("Abrindo o Simulador.....")
        Dependency.simulator()
        print("Pressione Enter para fechar.....")

    @staticmethod
    def update_dll():
        dest = input("Digite o path até a pasta do sistema:")
        Dependency.dll(dest)

class Pipeline:

    def install_sitef():
        try:
            print("Iniciando a instalação do TLS")
            Dependency.tls()
            input("pressione qualquer Enter para continuar.....")
            print("Testando o tls")
            test = Utils.test_tls()
            if test == 0:
                print(test.stdout)
            else:
                Utils.restart_service("")
            input("pressione qualquer Enter para continuar.....")
            Utils.pinpad()
            input("pressione qualquer Enter para continuar.....")
            option = input("Escolha o metodo de comunicação DLL (D) ou Client (C):").strip().lower()
            while(True):
                if option == 'd':
                    Dependency.dll("")
                    break
                elif option == 'c':
                    Dependency.client()
                else:
                    print("Opção invalida!")
        except Exception as e:
            print("Error na instalação sitef:", e)    

    def install_dtef():
        print("Abrindo o instalador D-TEF")
        Dependency.dtef()
        print("Pressione Enter para fechar.....")

    
    def reinstall_pinpad():
        Utils.pinpad()
    

    def correct_dtef():
        option = "Pressione Enter para continua ....."


if __name__ == "__main__":
    try:
        while(True):
            option = int(input("Escolha a opção:\n0.Sair\n1.Instalação Sitef\n2.Instalação D-TEF\n3.Reinstalar PinPad\n4.Atualizar DLL\n5.Abrir Simulador\n:"))
            match option:
                case 0:break
                case 1:Pipeline.install_sitef()
                case 2:Pipeline.install_dtef()
                case 3:Utils.pinpad()
                case 4:Dependency.dll()
                case 5:Utils.configurate_client()
                case _:print("Opção Invalida!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
