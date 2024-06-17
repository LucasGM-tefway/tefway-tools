import subprocess
import os
import shutil


class Dependency:
    @staticmethod
    def tls():Utils.run_exe('tls', 'tlscliwl.exe')

    @staticmethod
    def gertec():Utils.run_exe('Gertec', 'Gertec-Full-Installer_2.2.2.0.exe')

    @staticmethod
    def ingenico():Utils.run_exe('Ingenico', 'IngenicoUSBDrivers_3.36_setup_SIGNED.exe')

    @staticmethod
    def vx():Utils.run_exe('VX_P200/32', 'silent_install_VerifoneUSBDriverUninstall.bat')

    @staticmethod
    def lane():Utils.run_exe('Lane 3000', 'IngenicoUSBDrivers_3.34_setup_SIGNED.exe')

    @staticmethod
    def simulator():Utils.run_exe('Simulador', 'SiTEF Simulador.exe')

    @staticmethod
    def client():Utils.run_exe('clientsitef/7.0.3.1P r1/DISK1', 'Instala.exe')

    @staticmethod
    def dtef():Utils.run_exe('DTEF', 'Instalador_Linx_TEF_3.1.4.exe')

    @staticmethod
    def dll(dest_path):
        src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', 'DLLL', 'clisitef-7.0.117.83.r1-Producao-Win32')
        for file in os.listdir(src):
            shutil.copy2(os.path.join(src, file), os.path.join(dest_path, file))


class Utils:
    @staticmethod
    def run_exe(directory, executable):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dependencias', directory, executable)
        process = subprocess.Popen([path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise Exception(f"Erro na execução do executável: {stderr}")
        return stdout

    @staticmethod
    def restart_service(service_name):
        subprocess.run(f"net stop {service_name}", shell=True)
        subprocess.run(f"net start {service_name}", shell=True)

    @staticmethod
    def test_tls():
        return subprocess.run(r'netstat -ano | find "4096"', capture_output=True, text=True, shell=True)

    @staticmethod
    def select_pinpad():
        options = {'g': Dependency.gertec, 'i': Dependency.ingenico, 'l': Dependency.lane, 'v': Dependency.vx}
        while True:
            option = input("Escolha o PinPad\nGertec(G)\nIngenico(I)\nLane3000(L)\nVX_P2000(V)\n:").strip().lower()
            if option in options:
                options[option]()
                break
            print("Opção Inválida")

    @staticmethod
    def configurate_client():
        print("Abrindo o Simulador.....")
        Dependency.simulator()
        input("Pressione Enter para fechar.....")

    @staticmethod
    def update_dll():
        dest = input("Digite o path até a pasta do sistema:")
        Dependency.dll(dest)


    @staticmethod
    def correct_dtef():
        Utils.run_exe('Rotinas Update', '1)DPOS8GPSetup822071922.exe')

    @staticmethod
    def correct_gp():
        pass

    @staticmethod
    def correct_runtime():
        pass    


class Pipeline:
    @staticmethod
    def install_sitef():
        try:
            print("Iniciando a instalação do TLS")
            Dependency.tls()
            input("Pressione Enter para continuar.....")

            print("Testando o TLS")
            test = Utils.test_tls()
            if test.returncode == 0:
                print(test.stdout)
            else:
                Utils.restart_service("NomeDoServico")  # Insira o nome correto do serviço

            input("Pressione Enter para continuar.....")
            Utils.select_pinpad()
            input("Pressione Enter para continuar.....")

            while True:
                option = input("Escolha o método de comunicação DLL (D) ou Client (C):").strip().lower()
                if option in {'d', 'c'}:
                    break
                print("Opção inválida!")

            if option == 'd':
                dest = input("Digite o path até a pasta do sistema:")
                Dependency.dll(dest)
            elif option == 'c':
                Dependency.client()
        except Exception as e:
            print("Erro na instalação Sitef:", e)

    @staticmethod
    def install_dtef():
        print("Abrindo o instalador D-TEF")
        Dependency.dtef()
        input("Pressione Enter para fechar.....")



    @staticmethod
    def correct_dtef():
        input("Pressione Enter para continuar.....")


def main_menu():
    options = {
        1: Pipeline.install_sitef,
        2: Pipeline.install_dtef,
        3: Utils.select_pinpad,
        4: Utils.update_dll,
        5: Utils.configurate_client,
        6: Utils.correct_dtef,
        7: Utils.correct_gp,
        8: Utils.correct_runtime
    }

    while True:
        try:
            option = int(input("Escolha a opção:\n0. Sair\n1. Instalação Sitef\n2. Instalação D-TEF\n3. Reinstalar PinPad\n4. Atualizar DLL\n5. Abrir Simulador\n6. Corrigir o (D-TEF)\n7. Corrigir o GP(D-TEF)\n8. Corrigir runtime (D-TEF)\n:"))
            if option == 0:
                break
            elif option in options:
                options[option]()
            else:
                print("Opção Inválida!")
        except ValueError:
            print("Opção inválida! Por favor, insira um número.")


if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
