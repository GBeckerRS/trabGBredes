#!/usr/bin/env/python

import sys

from terminal import *
from arquivo import *
from socket_cliente import *

class Cliente:
    def __init__ (self, interfaceGrafica):
        self.interfaceGrafica = interfaceGrafica
        self.ip = ''
        self.porta = 0
        self.nomeArquivo = ""
        self.term = None
        self.arquivo = None
        self.buffer = ''

    def executa (self):
        dados = ''

        # Inicializa atributos do cliente
        self.inicializa ()

        # Le dados do arquivo que sera enviado
        self.arquivo = Arquivo (self.nomeArquivo)
        self.arquivo.abre ('r')
        dados = self.arquivo.le ()
        self.arquivo.fecha ()

        # Envia dados para o servidor
        soc = Socket_cliente (self.ip, self.porta)
        soc.enviaDados (dados)

    def inicializa (self):
        if (self.interfaceGrafica == 'N'):
            # Interface grafica desabilitada
            self.term = Terminal ()
        else:
            # Interface grafica habilitada (recurso indisponivel)
            self.term = Terminal ()

        # Requisita o ip do host
        self.ip = self.term.leIp ()

        # Requisita a porta do cliente
        self.porta = self.term.lePorta ()

        # Requisita o caminho do arquivo
        self.nomeArquivo = self.term.leCaminhoArquivo ()

