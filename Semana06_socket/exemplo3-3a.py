#importacao da biblioteca socket   
import socket 
#importacao a biblioteca time
import time   
#Importando a biblioteca sys 
import sys      

#definicao do endereco UDP_IP do dispositivo recebedor
UDP_IP = "127.0.0.1" 
#definicao da porta de comunicacao e transf de arquivos
UDP_PORT = 5005
#tamanho do buffer  
buf = 1024           

file_name = sys.argv[1] 

#especificacao de qual tipo de endenreco ip_udp o programa ira aceitar para ceonexao;
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#Utilizacao da função sendto para conecatar cliente ao endereço ADDR do servidor e enviar o arquivo
sock.sendto(file_name, (UDP_IP, UDP_PORT))
#imprime na tela o status de transferencia enviada
print "Sending %s ..." % file_name 

#abertura do arquivo para leitura
f = open(file_name, "r") 
#Definicao do tamanho dos dados do arquivo
data = f.read(buf) 
while(data): 
    #verificacao da variável de leitura e do tamanho do arquivo enviado
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): 
        #Definicao do tamanho dos dados do arquivo
        data = f.read(buf)
        #tempo dado para armazenamento do arquivo
        time.sleep(0.02) 
#encerra a tranferência do arquivo
sock.close() 
#encerrar a tranferência dos dados
f.close() 