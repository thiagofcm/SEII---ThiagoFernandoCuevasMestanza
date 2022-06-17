#importacao da biblioetca socket
import socket 

#definicao do endereco IP do dispositivo usado
TCP_IP = "127.0.0.1" 
#definicao da porta de comunicacao e transf de arquivos
FILE_PORT = 5005    
#definicao da porta de comunicacao e transf de dados 
DATA_PORT = 5006  
#tamanho do buffer  
buf = 1024          

#especificacao de qual tipo de endenreco ip o programa ira aceitar para ceonexao; indica que os dados estao sendo streamdos
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#vinculacao do socket ao endereço ADDR
sock_f.bind((TCP_IP, FILE_PORT)) 
#escutar e receber possiveis conexoes
sock_f.listen(1) 

#especificacao de qual tipo de endenreco ip o programa ira aceitar para ceonexao; indica que os dados estao sendo streamdos
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#vinculacao do socket ao endereço ADDR
sock_d.bind((TCP_IP, DATA_PORT)) 
#escutar e receber possiveis conexoes
sock_d.listen(1) 

while True: 
    #conexoes admitidas pelo servidor
    conn, addr = sock_f.accept() 
    #define tamanho da mensagem
    data = conn.recv(buf) 
    if data:
        #printa na tela nome do arquivo
        print "File name:", data 
        #retira os bytes iniciais e finais do arquivo
        file_name = data.strip() 

    #abertura do arquivo para escrita
    f = open(file_name, 'wb') 

    #conexoes admitidas pelo servidor
    conn, addr = sock_d.accept()
    
    while True:
        #Definicao do tamanho dos dados recebidos
        data = conn.recv(buf) 
        if not data: 
            break    
        #Escreve os dados no arquivo
        f.write(data) 
    #imprime na tela o status de transferencia finalizada
    print "%s Finish!" % file_name
    #encerras a conexão
    f.close() 