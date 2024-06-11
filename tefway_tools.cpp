#include <iostream>
#include <cstdlib> // Incluído para usar a função system
using namespace std;

int install_sitef()
{
    cout << "SITEF" << endl;
    int vpn = system("Dependencias/tls/tlscliwl.exe");
    if (vpn == 0)
    {
        int status_vpn = system("netstat -ano | find \"4096\"");
        if (status_vpn == 1)
        {
            cout << "Serviço VPN não está em execução." << endl;
            // Iniciar o serviço do monitor
        }
        else
        {
            cout << "Serviço VPN está em execução." << endl;
            // Alguma outra ação, se necessário
        }
    }
    else
    {
        cout << "Erro ao executar tlscliwl.exe." << endl;
    }

    return 0;
}

int install_dtef()
{
    int op;
    cout << "Instalacao D-TEF:" << endl;
    cout << "1. Nextar" << endl;
    cout << "2. Seta" << endl;
    cin >> op;
    if (op == 1)
    {
        cout << "Instalando D-TEF (Nextar)..." << endl;
    }
    else if (op == 2)
    {
        cout << "Instalando D-TEF (Seta)..." << endl;
    }
    else
    {
        cout << "Opcao invalida!" << endl;
    }
    return 0;
}

int configuracoes()
{
    int op;
    cout << "Configuracoes:" << endl;
    cout << "1. Verificar VPN" << endl;
    cout << "2. Atualizar DLL" << endl;
    cout << "3. Abrir simulador" << endl;
    cout << "4. Instalar driver PIN-pad" << endl;
    cin >> op;
    switch (op)
    {
    case 1:
        cout << "Verificando VPN..." << endl;
        break;
    case 2:
        cout << "Atualizando DLL..." << endl;
        break;
    case 3:
        cout << "Abrindo simulador..." << endl;
        break;
    case 4:
        cout << "Instalando driver PIN-pad..." << endl;
        break;
    default:
        cout << "Opcao invalida!" << endl;
        break;
    }
    return 0;
}

void run()
{
    int op;
    bool condition = true;

    while (condition)
    {
        cout << "Digite a opcao:\n0.Sair\n1.Instalacao SITEF\n2.Instalacao D-TEF\n3.Configuracoes\n:";
        cin >> op;

        switch (op)
        {
        case 0:
            condition = false;
            break;
        case 1:
            install_sitef();
            break;
        case 2:
            install_dtef();
            break;
        case 3:
            configuracoes();
            break;
        default:
            cout << "Opcao invalida!" << endl;
            break;
        }
    }
}

int main()
{
    run();
    return 0;
}
