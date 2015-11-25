#!/usr/bin/env/python

import socket
import sys

from meuSocket import *

class Socket_servidor (Socket):
    def __init__ (self, ip, porta, tamamnhoBuffer):
        self.ip = ip
        self.porta = porta
        self.tamBuffer = 1024

    def processaCliente (self):
        host = self.getIp ()
        porta = int (self.getPorta ())
        dados = ''

        # Inicializa o socket
        try:
            s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error, msg:
            print 'Falhou ao criar o socket. Codigo de erro: ' + str(msg [0]) + 'Mensagem ' + msg[1]
            sys.exit ()

        # Vincula o socket criado a aplicacao
        try:
            s.bind ((host, porta))
        except socket.error, msg:
            print 'Falhou ao vincular o socket. Codigo de erro: ' + str(msg [0]) + 'Mensagem ' + msg[1]
            sys.exit ()

        print 'Para sair utilize CTRL+C\n'

        # Laco de processamento das requisicoes
        sair = False
        while not sair:
            # Recebe os dados do cliente
            try:
                msg, cliente = s.recvfrom (self.tamBuffer)
            except KeyboardInterrupt:
                print 'Encerrando o aplicativo...'
                sair = True

            # Recebeu dados do cliente
            if not sair:
                print 'Ip do cliente: ' + cliente[0] + ', Porta do cliente: ' + str (cliente [1])
                dados = msg
                sair = True

        s.close ()

        return dados

