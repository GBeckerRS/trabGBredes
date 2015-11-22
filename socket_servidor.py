#!/usr/bin/env/python

import socket
import sys

from meuSocket import *

class Socket_servidor (Socket):
    def __init__ (self, ip, porta):
        self.ip = ip
        self.porta = porta
        self.tamBuffer = 1024
        print 'Criado o objeto Socket_servidor...'

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
        print 'Foi criado o socket com sucesso...'

        # Vincula o socket criado a aplicacao
        try:
            s.bind ((host, porta))
        except socket.error, msg:
            print 'Falhou ao vincular o socket. Codigo de erro: ' + str(msg [0]) + 'Mensagem ' + msg[1]
            sys.exit ()
        print 'Socket foi vinculado ao servidor...'

        print 'Para sair utilize CTRL+X\n'

        # Laco de processamento das requisicoes
        sair = False
        while not sair:
            # Recebe os dados do cliente
            try:
                msg, cliente = s.recvfrom (self.tamBuffer)
            except KeyboardInterrupt:
                print 'Encerrando o aplicativo...'
                sair = True
            if (not sair):
                print 'recebeu dados do cliente...'

            # Recebeu dados do cliente
            if not sair:
                print 'Cliente de origem: ' + cliente
                dados = msg
                sair = true

        s.close ()

        return dados

