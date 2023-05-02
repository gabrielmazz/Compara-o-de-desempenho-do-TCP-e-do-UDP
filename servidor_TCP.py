import socket
import os
import time
import sys
import math

NOME_NOVO_ARQUIVO = 'arquivo_recebido_tcp.txt'

# Verifica se o arquivo esta criado
if os.path.exists(NOME_NOVO_ARQUIVO):
    # Se o arquivo existir, deleta o arquivo
    os.remove(NOME_NOVO_ARQUIVO)
else:
    pass

# definir o tamanho máximo dos pacotes a serem recebidos
tamanho_pacote = 1024

# Definir o endereço IP e porta do servidor
endereco_servidor = '127.0.0.1'
porta_servidor = 5000

# Cria o socket TCP
servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

os.system('clear')

# Verifica se a conexão foi efetivada com sucesso
try:
    print("Aguardando conexão com o cliente...")
    
    # Associa o socket com o endereço e porta do servidor
    servidor_tcp.bind((endereco_servidor, porta_servidor))

    # Ouvi as conexões
    servidor_tcp.listen()

    # Aceitar conexão do cliente
    conexao, endereco_cliente = servidor_tcp.accept()
    
    os.system('clear')
    
    print(f"Conexão com o cliente {endereco_cliente} estabelecida com sucesso!")       
except Exception as erro:
    # Gera uma mensagem de erro se algo acontecer e não for possivel estabelecer a conexão
    print(f"Erro ao estabelcer a conexão: {erro}")
    sys.exit()

# Começa a contagem de tempo para receber o arquivo
start_time = time.time()

# Recebe o nome do arquivo que esta sendo mandado
nome_arquivo = conexao.recv(tamanho_pacote).decode("utf-8")

# Abrir arquivo para escrita
with open(NOME_NOVO_ARQUIVO, 'wb') as arquivo:
    while True:
        
        # Receber pacote
        dados = conexao.recv(tamanho_pacote)
        if not dados:
            break
        
        # Escreva os dados no arquivo
        arquivo.write(dados)

# Termina a contagem de tempo
end_time = time.time()

# Mostra o tempo decorrido para enviar o arquivo
time_final = end_time - start_time

os.system('clear')

print("Arquivo recebido com sucesso via TCP!\n")
print(f"Arquivo recebido pelo servidor: {nome_arquivo}")
print(f"Novo arquivo: {NOME_NOVO_ARQUIVO}")
print(f'IP do remetente: {endereco_cliente}')
print(f"Tamanho do arquivo {NOME_NOVO_ARQUIVO}: {round(os.path.getsize(NOME_NOVO_ARQUIVO)/pow(1024, 2))} MB")
print(f"Tempo decorrido para receber o arquivo: {time_final:.2f} segundos")

# Fecha a conexão com o socket
conexao.close()
servidor_tcp.close()
