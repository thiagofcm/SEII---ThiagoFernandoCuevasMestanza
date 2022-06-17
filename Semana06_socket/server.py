#importacao da biblioteca socket   
import socket    
#importacao da biblioteca threading
import threading

#definicao do numero de bytes a serem recebidos do cliente para o servidor
HEADER = 64
#definicao da porta de comunicacao
PORT = 5050 
#atribuicao do endereco ip local da maquina a variavel SERVER
SERVER = socket.gethostbyname(socket.gethostname()) 
#criacao de uma variavel que associa o servidor à porta de comunicacao
ADDR = (SERVER, PORT)
#definicao do formato de codificação binária do comprimento UTF-8
FORMAT = 'utf-8' 
#atrivuicao de uma mensagem de desconexao à uma variavel string
DISCONNECT_MESSAGE = "!DISCONNECT" 
#especificacao de qual tipo de endenreco ip o programa ira aceitar para ceonexao; indica que os dados estao sendo streamdos
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#vinculacao do socket ao endereço ADDR
server.bind(ADDR) 

#Funcao que administra configuracoes de conexao entre servidor e cliente
def handle_client(conn, addr):
    #impressao na tela de uma mensagem de conexao 
    print(f"[NEW CONNECTION] {addr} connected.")
    #variavel que valida a conexao
    connected = True
    while connected: 
        #definicao do numero de bytes usados na mensagem
        msg_length = conn.recv(HEADER).decode(FORMAT) 
        if msg_length:
            #conversao do numero de bytes da mensagem para uma variavel int
            msg_length = int(msg_length) 
            #atribuicao da mensagem à variavel msg
            msg = conn.recv(msg_length).decode(FORMAT) 
            #verificacao da mensagem recebida, se for igual a mensagem de desconexao, a conexao eh finalizada
            if msg == DISCONNECT_MESSAGE: 
                connected = False
            #impressao na tela do endereco do cliente e a mensagem transmitida
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    #Finaliza a conexão       
    conn.close() 
        
#f unção que permite o servidor administrar as conexoes
def start():
    #escuta possiveis conexoes
    server.listen() 
    #impressao do status do servidor
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        #conexoes admitidas pelo servidor
        conn, addr = server.accept() 
        #thread que envia as novas conexões para o handle_cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr)) 
        #inicia a thread
        thread.start() 
        #imprime na tela as conexoes ativas
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") 

#mensagem que indica a inicializacao do servidor 
print("[STARTING] server is starting...") 
start() 