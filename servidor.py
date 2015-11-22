#!/usr/bin/env/python

import sys

from terminal import *
from socket_servidor import *
from arquivo import *

class Servidor:
    def __init__ (self, interfaceGrafica):
        self.interfaceGrafica = interfaceGrafica
        self.porta = 0
        self.nomeArquivo = ""
        self.term = None
        self.arquivo = None
        self.buffer = ''

    def executa (self):
        # Le a partir do teclado a porta que aguarda a conexao
        # le o caminho do arquivo para gravar os dados
        print 'Metodo executa'

        # Inicializa atributos do cliente
        self.inicializa ()

        # Inicializa socket do servidor
        soc = Socket_servidor ('127.0.0.1', '9999')

        # Looping de recebimento de dados
        while 1:
            self.buffer = soc.processaCliente ()

            if (self.buffer == ''):
                print 'Nada foi recebido de clientes, encerrando a aplicacao'
                sys.exit ()

            # Realiza gravacao em arquivo dos dados recebidos
            self.arquivo = Arquivo (self.nomeArquivo)
            self.arquivo.abre ('w')
            self.arquivo.escreve (self.dados)
            self.arquivo.fecha ()

    def inicializa (self):
        if (self.interfaceGrafica == 'N'):
            # Interface grafica desabilitada
            self.term = Terminal ()
        else:
            # Interface grafica habilitada (recurso indisponivel)
            self.term = Terminal ()

        # Requisita a porta do servidor
        self.porta = self.term.lePorta ()

        # Requisita o caminho do arquivo
        self.nomeArquivo = self.term.leCaminhoArquivo ()

