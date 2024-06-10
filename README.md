# Tef_Instaler
## Projeto para fazer a junção de varios instaladores(1.0.9 - Completo).
- instalar o tls com inserção da senha manualmente
- instalação do driver do pin-pad com escolha do usuario.
- Fazer a instalação da dll ou client.
## versão 2.0.1:
- Modelar o fluxo para que possa ser usado para mais do que somente instalação, atualizações, configurações de cliente, etc ...(Feito).
- Gerar um Log da instalação ou reinstalação(Em Progresso).
- gerar fluxo de reinstalação(Aguardando a finalização da etapa anterior).
- gerar um fluxo para migração(Aguardando a finalização da etapa anterior).
- Utilizar o upx para diminuir o tamanho do executavel(Aguardando a finalização da etapa anterior).
## comando de build:
- Windows:
  - pyinstaller --clean --onefile --add-data "Dependencias;Dependencias" --icon="Dependencias\Tefway.ico" --upx-dir="C:/Users/jkai/OneDrive/Área de Trabalho/upx-4.2.4-win64" Tefway_Instaler.py
## proximos passos:
1. Otimizar e revisar o codigo(Importante).
2. Deixar mais amigavel a execução(+-).
3. Implementar uma interface grafica(Opcional).
