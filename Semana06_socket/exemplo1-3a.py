#importacao da biblioetca socket
import socket
#importacao da biblioteca sys
import sys 
#definicao do endereco IP do dispositivo usado
TCP_IP = "127.0.0.1"
#definicao da porta de comunicacao e transf de arquivos
FILE_PORT = 5005
#definicao da porta de comunicacao e transf de dados
DATA_PORT = 5006
#tamanho do buffer
buf = 1024
file_name = sys.argv[1]


try:
    #especificacao de qual tipo de endenreco ip o programa ira aceitar para ceonexao; indica que os dados estao sendo streamdos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #conexao do cliente ao endereco ADDR do servidor - transf de arquivos
    sock.connect((TCP_IP, FILE_PORT))
    #envio do arquivo
    sock.send(file_name)
    #encerramento da transferencia
    sock.close()
    
    #impressao na tela do status de envio do arquivo
    print "Sending %s ..." % file_name

    f = open(file_name, "rb")
    #definicao do cliente
    #especificacao de qual tipo de endenreco ip o programa ira aceitar para ceonexao; indica que os dados estao sendo streamdos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #conexao do cliente ao endereco ADDR do servidor - transf de dados
    sock.connect((TCP_IP, DATA_PORT))
    #definicao da variavel para leitura de dados
    data = f.read()
    #envio dos dados
    sock.send(data)

finally:
    #encerra a transferencia de arquivos
    sock.close()
    #encerra a transferencia de dados
    f.close()