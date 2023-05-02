import socket
import os
import time
import sys

# Define o nome do arquivo que sera recebido
NOME_NOVO_ARQUIVO = 'arquivo_recebido_udp.txt'

# Verifica se o arquivo esta criado
if os.path.exists(NOME_NOVO_ARQUIVO):
    # Se o arquivo existir, deleta o arquivo
    os.remove(NOME_NOVO_ARQUIVO)
else:
    pass

# Defini o tamanho máximo dos pacotes a serem recebidos
tamanho_pacote = 1024

# Definir o endereço IP e porta do servidor
endereco_servidor = '127.0.0.1'
porta_servidor = 5000

# Cria o socket UDP
servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system('clear')

# Associa o socket com o endereço e porta do servidor
servidor_udp.bind((endereco_servidor, porta_servidor))

# Aguarda o recebimento do arquivo
try:
    print("Aguardando recebimento do arquivo...")
    
    dados, endereco_cliente = servidor_udp.recvfrom(tamanho_pacote)
    
    os.system('clear')
    
    print(f"Conexão com o cliente {endereco_cliente} estabelecida com sucesso!") 

except Exception as erro:
    # Gera uma mensagem de erro se algo acontecer e não for possivel estabelecer a conexão
    print(f"Erro ao estabelcer a conexão: {erro}")
    
    sys.exit()

# Começa a contagem de tempo para receber o arquivo
start_time = time.time()

# Recebe o nome do arquivo que esta sendo mandado
nome_arquivo, endereco_cliente = servidor_udp.recvfrom(tamanho_pacote)
nome_arquivo = dados.decode('latin1')

# Recebe os dados do arquivo em pacotes e escreve no novo arquivo
with open(NOME_NOVO_ARQUIVO, 'wb') as arquivo:
    while True:
        # Define um timeout de 5 segundos para a recepção dos pacotes
        servidor_udp.settimeout(5)
        
        try:
            # Recebe o próximo pacote de dados
            dados, endereco_cliente = servidor_udp.recvfrom(tamanho_pacote)
            
            # Escreva os dados no arquivo
            arquivo.write(dados)
            
            servidor_udp.sendto(b"ACK", endereco_cliente)
            
        except socket.timeout:
            # Se o timeout expirou, assume que o arquivo foi enviado completamente
            break


#Termina a contagem de tempo
end_time = time.time()

# Mostra o tempo decorrido para enviar o arquivo
time_final = end_time - start_time

os.system('clear')

print("Arquivo recebido com sucesso via UDP!\n")
print(f"Arquivo recebido pelo servidor: {nome_arquivo}")
print(f"Novo arquivo: {NOME_NOVO_ARQUIVO}")
print(f'IP do remetente: {endereco_cliente}')
print(f"Tamanho do arquivo {NOME_NOVO_ARQUIVO}: {round(os.path.getsize(NOME_NOVO_ARQUIVO)/pow(1024, 2))} MB")
print(f"Tempo decorrido para receber o arquivo: {time_final:.2f} segundos")

# Fecha o socket
servidor_udp.close()
