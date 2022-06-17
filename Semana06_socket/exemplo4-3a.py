#importacao da biblioteca socket   
import socket 
#importacao a biblioteca select
import select 

#definicao do endereco UDP_IP do dispositivo recebedor
UDP_IP = "127.0.0.1"
#definicao da porta de comunicacao e transf de arquivos
IN_PORT = 5005 
#definicao do limite de 3 transferências 
timeout = 3 

#especificacao de qual tipo de endenreco ip_udp o programa ira aceitar para ceonexao;
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#vinculacao do socket de arquivos ao endereço ADDR no servidor
sock.bind((UDP_IP, IN_PORT)) 

while True: 
    #definicao do tamanho do arquvivo recebido
    data, addr = sock.recvfrom(1024) 
    if data:
        #printa na tela nome do arquivo
        print "File name:", data 
        #retira os bytes iniciais e finais do arquivo
        file_name = data.strip() 
    #abertura do arquivo para escrita
    f = open(file_name, 'wb') 

    while True: 
        #recepcao e leitura das 3 transferencias
        ready = select.select([sock], [], [], timeout) 
        if ready[0]:
            #definicao do tamanho do novo arquivo recebido
            data, addr = sock.recvfrom(1024) 
            #escreve os dados no arquivo
            f.write(data) 
        else: 
             #imprime na tela o status de transferencia finalizada
            print "%s Finish!" % file_name 
            #encerras a conexão
            f.close() 
            break 