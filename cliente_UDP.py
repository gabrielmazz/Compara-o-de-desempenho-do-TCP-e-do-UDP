import socket
import os
import sys
import time

# Define o nome do arquivo que sera mandado
NOME_ARQUIVO = 'teste.txt'
TAMANHO_ARQUIVO = os.path.getsize(NOME_ARQUIVO)

# Define o tamanho dos pacotes
pacote_pequeno = 100
pacote_medio = 500
pacote_grande = 1000

os.system('clear')

# Solicitar o tamanho do pacote
while True:
    print("Selecione o tamanho do pacote:\n1 - Pacote pequeno (100 bytes)\n2 - Pacote médio (500 bytes)\n3 - Pacote grande(1000 bytes)\n")
    print("Digite o número da opção desejada:")
    opcao = input()

    # selecionar o tamanho do pacote
    if opcao == '1':
        tamanho_pacote = pacote_pequeno
        os.system('clear')
        break
    elif opcao == '2':
        tamanho_pacote = pacote_medio
        os.system('clear')
        break
    elif opcao == '3':
        tamanho_pacote = pacote_grande
        os.system('clear')
        break
    else:
        print("Opção inválida, tente novamente")
        time.sleep(3)
        os.system('clear')

# Define o tamanho do arquivo a ser enviado
tamanho_arquivo_max = 100 * 1024 * 1024 # 100 MB

# Verifica se o tamanho do arquivo é maior que o limite do algoritmo
try:
    if TAMANHO_ARQUIVO > tamanho_arquivo_max:
        print("Arquivo muito grande, tente novamente")
        sys.exit()
except Exception as erro:
    print(f"Tamanho do arquivo é menor que o limite")


# Define o endereço IP e porta do servidor
endereco_servidor = '127.0.0.1'
porta_servidor = 5000

# Verifica se o arquivo existe
if not os.path.exists(NOME_ARQUIVO):
    print("Arquivo não encontrado")
    sys.exit()

# Cria o socket UDP
cliente_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Faz a verificação se o servidor existe
try:
    # Conecta com o servidor
    cliente_udp.connect((endereco_servidor, porta_servidor))
    print(f"Conexão com o servidor {endereco_servidor} estabelecida com sucesso!")
    
    # Se caso a conexão falhou, gera e mostra o erro
except Exception as erro:
    print(f"Erro ao conectar com o servidor: {erro}")

# Começa a contagem de tempo para mandar o arquivo
start_time = time.time()

# Manda o nome do arquivo para o servidor
cliente_udp.sendto(NOME_ARQUIVO.encode('utf-8'), (endereco_servidor, porta_servidor))

# Abre o arquivo a ser transferido
with open(NOME_ARQUIVO, "rb") as arquivo:
    # Lê o primeiro pacote do arquivo
    while True:  # Enquanto houver dados no arquivo
        # Lê o próximo pacote do arquivo
        dados = arquivo.read(tamanho_pacote)  
        
        if not dados:
            break
        
        # enviar o pacote
        cliente_udp.sendto(dados, (endereco_servidor, porta_servidor))  # Envia o pacote para o servidor
        

# Termina a contagem de tempo
end_time = time.time()

# Mostra o tempo decorrido para enviar o arquivo
time_final = end_time - start_time

os.system('clear')

print("Arquivo enviado com sucesso via UDP!\n")
print(f"Arquivo mandado para o servidor: {NOME_ARQUIVO}")
print(f'IP do destinatario: {endereco_servidor}')
print(f"Tamanho de cada pacote foi definido como {tamanho_pacote} bytes")
print(f'Tamanho do arquivo {NOME_ARQUIVO}: {round(TAMANHO_ARQUIVO/pow(1024, 2))} MB')
print(f"Tempo decorrido para enviar o arquivo: {time_final:.2f} segundos")

# Fecha o socket
cliente_udp.close()
