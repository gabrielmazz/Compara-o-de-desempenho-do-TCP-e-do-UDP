## Comparação de desempenho do TCP e UDP

#### Trabalho de Sistemas Operacionais

> Colaboradores: *Gabriel Mazzuco* ([Github Profile](https://github.com/gabrielmazz)), *Rodrigo Rocha* ([Github Profile](https://github.com/Rodrigo2603))

- 3ª ano de Ciências da Computação

## Introdução

Este repositório contém a implementação de clientes e servidores TCP e UDP para a transferência de arquivos de 100 MB entre dois computadores usando pacotes de tamanhos variados. A comparação de desempenho é feita com e sem garantia de entrega.

O objetivo deste projeto é avaliar o desempenho do TCP e UDP para transferência de arquivos em redes de computadores. O protocolo TCP é confiável e garante a entrega de pacotes, enquanto o UDP não possui essa garantia. Para garantir a entrega de pacotes no UDP, foi utilizado um protocolo com confirmação do tipo pare-e-espere.

<img src="https://www.cyberghostvpn.com/privacyhub/wp-content/uploads/2022/04/1tcpvsudp7.gif" style="width:350px; float: right; margin: 90px 10px 10px 10px;">

## O que é TCP e o UDP

UDP significa User Datagram Protocol, e é um protocolo de comunicação da camada de transporte. É um protocolo mais simples do que o TCP, e não fornece as mesmas garantias de entrega de dados e de controle de fluxo. No entanto, o UDP é mais rápido e eficiente do que o TCP, e é frequentemente usado em aplicações que precisam de baixa latência, como jogos online e transmissão de vídeo.


Por outro lado, o TCP, ou Transmission Control Protocol, é um protocolo de comunicação da camada de transporte que fornece confiabilidade na entrega de dados. Ele estabelece uma conexão entre o remetente e o destinatário antes de enviar dados, e verifica se todos os dados foram entregues corretamente. Se os dados não forem entregues, o TCP retransmite os dados perdidos.

## Execução

Primeiro deve ter instalado o Python 3 instalado no computador, caso não esteja baixado, basta executar o comando no terminal do Linux

```
sudo apt-get update
sudo apt-get install python3
```

### TCP

Para a execução do servidor, primeiro execute o servidor TCP com o comando abaixo:

```
python3 servidor_tcp.py
```

Em seguida podemos executar o cliente do TCP

```
python3 cliente_tcp.py
```

### UDP

Para a execução do servidor, primeiro execute o servidor UDP com o comando abaixo:

```
python3 servidor_udp.py
```

Em seguida, execute o cliente UDP com o comando abaixo:

```
python3 cliente_udp.py 
```

## Pacotes de tamanho variado

O tamanho dos pacotes pode ser selecionado durante a execução do cliente TCP e UDP. Para cada teste, os pacotes têm 100 bytes, 500 bytes e 1.000 bytes.

## Resultados

Os resultados dos testes são exibidos na tela após a conclusão da transferência de arquivos. Para cada teste, é exibido o tempo decorrido para enviar o arquivo, o tamanho de cada pacote e o tamanho do arquivo enviado.

## Conclusão
<img src="https://pbs.twimg.com/media/E3thRQzVEAQ6yTy.jpg:large" style="width:350px; float: left; margin: 25px 10px 10px 10px;">

Com base nos resultados obtidos, é possível concluir que o TCP é mais confiável e eficiente na transferência de arquivos em comparação com o UDP, que pode perder pacotes e, portanto, requer confirmações adicionais para garantir a entrega dos pacotes. Além disso, o tamanho dos pacotes pode afetar significativamente o desempenho da transferência de arquivos. Em geral, pacotes maiores resultam em uma transferência mais rápida, desde que o tamanho do pacote não exceda o MTU (Maximum Transmission Unit) da rede.
