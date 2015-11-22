#!/usr/bin/env/python

import socket
import sys

from meuSocket import *

class Socket_cliente (Socket):
    def __init__ (self, ip, porta):
        self.ip = ip
        self.porta = porta
        self.tamBuffer = 1024
        print 'Criado o objeto Socket_cliente...'

    def enviaDados (self, dados):
        ip = self.getIp ()
        porta = int (self.getPorta())

        # Inicializa o socket do cliente
        try:
            s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error, msg:
            print 'Falhou ao criar o socket. Codigo de erro: ' + str (msg [0]) + ' Mensagem ' + msg [1]
            sys.exit ()
        print 'Foi criado o socket com sucesso...'

        # Envia um blodo de dados ao host
        try:
            s.sendto (dados, (ip,porta))
        except socket.error, msg:
            print 'Nao foi possivel comunicar com o host. Codigo de erro: ' + str (msg [0]) + ' Mensagem ' + msg [1]
            sys.exit ()
        print 'Comunicacao foi estabelecida com sucesso...'

        # fecha o socket
        s.close ()

