#!/usr/bin/env/python

import sys

from terminal import *
from socket_servidor import *
from arquivo import *

class Servidor:
    def __init__ (self, interfaceGrafica, tamanhoBuffer):
        self.interfaceGrafica = interfaceGrafica
        self.porta = 0
        self.nomeArquivo = ""
        self.term = None
        self.arquivo = None
        self.buffer = ''
        self.tamanhoBuffer = tamanhoBuffer

    def executa (self):
        # Inicializa atributos do cliente
        self.inicializa ()

        # Inicializa socket do servidor
        s = Socket_servidor ('127.0.0.1', self.porta, self.tamanhoBuffer)

        # Inicializa o sevidor
        s.inicializaServidor ()

        # Looping de recebimento de dados
        while 1:
            self.buffer = s.processaCliente ()
            # Realiza gravacao em arquivo dos dados recebidos
            self.arquivo = Arquivo (self.nomeArquivo)
            self.arquivo.abre ('a')
            self.arquivo.escreve (self.buffer)
            self.arquivo.fecha ()

        # Finaliza o servidor
        s.fechaConexao ()

    def inicializa (self):
        if (self.interfaceGrafica == 'N'):
            # Inicializa a interface em modo texto
            self.term = Terminal ()
        else:
            # Inicializa a interface grafica (nao implementada)
            self.term = Terminal ()

        # Requisita a porta do servidor
        self.porta = self.term.lePorta ()

        # Requisita o caminho do arquivo
        self.nomeArquivo = self.term.leCaminhoArquivo ('Digite o nome (caminho completo) do arquivo a escrever')

