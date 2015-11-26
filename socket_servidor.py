#!/usr/bin/env/python

import socket
import sys

from meuSocket import *

class Socket_servidor (Socket):
    def __init__ (self, ip, porta, tamamnhoBuffer):
        self.ip = ip
        self.porta = porta
        self.tamBuffer = 1024
        self.soc = None

    def processaCliente (self):
        dados = ''

        print 'Para sair utilize CTRL+C\n'

        # Laco de processamento das requisicoes
        sair = False
        # Recebe os dados do cliente
        try:
            msg, cliente = self.soc.recvfrom (self.tamBuffer)
        except KeyboardInterrupt:
            print 'Encerrando o aplicativo...'
            sys.exit ()
        print 'SS Dados: ' + msg
        '''
        while not sair:
            # Recebe os dados do cliente
            try:
                msg, cliente = self.soc.recvfrom (self.tamBuffer)
            except KeyboardInterrupt:
                print 'Encerrando o aplicativo...'
                sair = True

            # Recebeu dados do cliente
            if not sair:
                print 'Ip do cliente: ' + cliente[0] + ', Porta do cliente: ' + str (cliente [1])
                dados = msg
                sair = True
        '''
        return msg

    def inicializaServidor (self):
        host = self.getIp ()
        porta = int (self.getPorta ())

        # Inicializa o socket
        try:
            self.soc = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error, msg:
            print 'Falhou ao criar o socket. Codigo de erro: ' + \
                   str(msg [0]) + \
                  'Mensagem ' + \
                   msg[1]
            sys.exit ()

        # Vincula o socket criado a aplicacao
        try:
            self.soc.bind ((host, porta))
        except socket.error, msg:
            print 'Falhou ao vincular o socket. Codigo de erro: ' + \
                   str(msg [0]) + \
                  'Mensagem ' + \
                   msg[1]
            sys.exit ()

    def fechaConexao (self):
        s.close ()

