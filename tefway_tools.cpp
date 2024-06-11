#include <iostream>
#include <string>
#include <filesystem>
#include <stdexcept>
#include <cstdlib>

#if defined(_WIN32) || defined(_WIN64)
#include <windows.h>
#endif

using namespace std;
namespace fs = filesystem;

class Cliente {
    string nome, cnpj, tipo;
public:
    Cliente(const string& nome, const string& cnpj, const string& tipo) : nome(nome), cnpj(cnpj), tipo(tipo) {}
    string getNome() const { return nome; }
    string getCnpj() const { return cnpj; }
    string getTipo() const { return tipo; }
};

class Installer {
public:
    static void run_installer(const string& executable_path) {
        if (!fs::exists(executable_path)) {
            throw runtime_error("Arquivo não encontrado: " + executable_path);
        }

        string command = "\"" + executable_path + "\"";
        int result = system(command.c_str());

        if (result != 0) {
            throw runtime_error("Erro no instalador: " + to_string(result));
        }
    }

    static void run_installer_in_path(const string& relative_path) {
        string current_dir = fs::current_path().string();
        string executable_path = current_dir + "/" + relative_path;
        run_installer(executable_path);
    }
};

class TLS {
public:
    static void instalar() {
        Installer::run_installer_in_path("Dependencias/tls/tlscliwl.exe");
    }

    static void testar(const string& command) {
        int result = system(command.c_str());
        if (result != 0) {
            cout << "Falha no teste com o comando " << command << endl;
        }
    }
};

class Gertec {
public:
    static void instalar() {
        Installer::run_installer_in_path("Dependencias/Gertec/Gertec-Full-Installer_2.2.2.0.exe");
    }
};

class Ingenico {
public:
    static void instalar() {
        Installer::run_installer_in_path("Dependencias/Ingenico/IngenicoUSBDrivers_3.36_setup_SIGNED.exe");
    }
};

class Vx {
public:
    static void instalar() {
        string base_path = fs::current_path().string() + "/Dependencias/VX_P200";
        string installer_path = base_path + "/" + (sizeof(void*) == 4 ? "32" : "64") + "/silent_install_VerifoneUSBDriverUninstall.bat";
        Installer::run_installer(installer_path);
    }
};

class DLL {
public:
    static void copy_and_move(const string& dest_path) {
        string src = fs::current_path().string() + "/Dependencias/DLLL/clisitef-7.0.117.83.r1-Producao-Win32";

        if (!fs::exists(src)) {
            throw runtime_error("Diretório não encontrado: " + src);
        }

        for (const auto& entry : fs::directory_iterator(src)) {
            fs::copy(entry.path(), dest_path, fs::copy_options::overwrite_existing);
        }
    }
};

class Client {
public:
    static void install() {
        Installer::run_installer_in_path("Dependencias/clientsitef/7.0.3.1P r1/DISK1/Instala.exe");
    }
};

class Nextar {
public:
    static void install() {
        Installer::run_installer_in_path("Dependencias/Nextar/Instalador_Linx_TEF_3.1.3.exe");
    }
};

class Seta {
public:
    static void install() {
        Installer::run_installer_in_path("Dependencias/Seta/Instalador_Linx_TEF_3.1.3.exe");
    }
};

class Simulador {
public:
    static void executar() {
        Installer::run_installer_in_path("Dependencias/Simulador/SiTEF Simulador.exe");
    }
};

class Instalacao {
public:
    static void Sitef() {
        try {
            cout << "Iniciando o instalador TLS:" << endl;
            TLS::instalar();

            if (confirm("Continuar com o teste TLS?")) {
                TLS::testar("netstat -ano | find \"4096\"");
            }

            InstalarDrivers();

            string escolha = prompt("Instalar DLL (D) ou Client (C)? [D/C]: ");
            if (escolha == "d" || escolha == "D") {
                string path = prompt("Copie o caminho até a pasta do sistema: ");
                DLL::copy_and_move(path);
            } else if (escolha == "c" || escolha == "C") {
                Client::install();
            }
        } catch (const exception& err) {
            cout << err.what() << endl;
        }
    }

    static void InstalarDrivers() {
        while (true) {
            int op = promptInt("Instalar qual driver?\n0.Não instalar driver\n1.Gertec\n2.Ingenico\n3.VX\n: ");
            switch (op) {
                case 0: return;
                case 1: Gertec::instalar(); return;
                case 2: Ingenico::instalar(); return;
                case 3: Vx::instalar(); return;
                default: cout << "Opção inválida" << endl;
            }
        }
    }

    static void Dtef() {
        while (true) {
            try {
                int op = promptInt("Escolha a opção:\n1.Nextar\n2.Seta\n: ");
                switch (op) {
                    case 1: Nextar::install(); return;
                    case 2: Seta::install(); return;
                    default: cout << "Opção Invalida" << endl;
                }
            } catch (const exception& err) {
                cout << "Error na instalação do d-tef -> " << err.what() << endl;
            }
        }
    }

private:
    static bool confirm(const string& message) {
        char choice;
        cout << message << " [S/N]: ";
        cin >> choice;
        return tolower(choice) == 's';
    }

    static string prompt(const string& message) {
        string response;
        cout << message;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Clear the input buffer
        getline(cin, response);
        return response;
    }

    static int promptInt(const string& message) {
        int response;
        cout << message;
        cin >> response;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Clear the input buffer
        return response;
    }
};

class Run {
public:
    static void instalacao() {
        while (true) {
            try {
                int op = promptInt("Escolha a opção:\n1.Sitef\n2.D-TEF\n: ");
                if (op == 1) {
                    Instalacao::Sitef();
                    break;
                } else if (op == 2) {
                    Instalacao::Dtef();
                    break;
                } else {
                    cout << "Opção Invalida!" << endl;
                }
            } catch (const exception& err) {
                cout << "Error no processo de instalação -> " << err.what() << endl;
            }
        }
    }

    static void other_pipeline() {
        try {
            int op = promptInt("Escolha a opção desejada:\n1.Testar VPN\n2.Atualizar DLL\n3.Abrir o simulador Sitef\n4.Instalar driver pin-pad\n: ");
            switch (op) {
                case 1: TLS::testar("netstat -ano | find \"4096\""); break;
                case 2: {
                    string path = prompt("Copie o caminho até a pasta do sistema: ");
                    DLL::copy_and_move(path);
                    break;
                }
                case 3: Simulador::executar(); break;
                case 4: Instalacao::InstalarDrivers(); break;
                default: cout << "Opção inválida!" << endl;
            }
        } catch (const exception& err) {
            cout << "Erro: " << err.what() << endl;
        }
    }

    static void init() {
        try {
            int op = promptInt("Escolha a opção:\n1.Instalação\n2.Teste, configurações ou atualizações\n: ");
            if (op == 1) {
                instalacao();
            } else if (op == 2) {
                other_pipeline();
            } else {
                cout << "Opção inválida!" << endl;
            }
        } catch (const exception& err) {
            cout << "Erro: " << err.what() << endl;
        }
    }

private:
    static string prompt(const string& message) {
        string response;
        cout << message;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Clear the input buffer
        getline(cin, response);
        return response;
    }

    static int promptInt(const string& message) {
        int response;
        cout << message;
        cin >> response;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Clear the input buffer
        return response;
    }
};

int main() {
    Run::init();
    return 0;
}
