#!/usr/bin/env/python

import sys

from terminal import *
from arquivo import *
from socket_cliente import *

class Cliente:
    def __init__ (self, interfaceGrafica, tamanhoBuffer):
        self.interfaceGrafica = interfaceGrafica
        self.ip = ''
        self.porta = 0
        self.nomeArquivo = ""
        self.term = None
        self.arquivo = None
        self.tamanhoBuffer = tamanhoBuffer

    def executa (self):
        dados = ''

        # Inicializa atributos do cliente
        self.inicializa ()

        # Le dados do arquivo que sera enviado
        self.arquivo = Arquivo (self.nomeArquivo)
        self.arquivo.abre ('r')
        dados = self.arquivo.le ()
        self.arquivo.fecha ()

        soc = Socket_cliente (self.ip, self.porta, self.tamanhoBuffer)

        print 'Inciando a transmissao de dados...'

        tamanho = len (dados)
        tamanhoPacote = self.tamanhoBuffer
        if (tamanho < tamanhoPacote):
            tamanhoPacote = tamanho
        inicio = 0
        final = tamanhoPacote
        contadorPacotes = 0
        while inicio < (tamanho -1):
            print 'Enviando o pacote: ' + str (contadorPacotes)
            # Envia dados para o servidor
            soc.enviaDados (dados [inicio:final])
            inicio = final
            final += tamanhoPacote
            contadorPacotes += 1

        print 'Encerrando a transmissao, foram enviados ' + \
               str (contadorPacotes) + \
             ' pacotes para o host...'

    def inicializa (self):
        if (self.interfaceGrafica == 'N'):
            # Inicializa a interface em modo texto
            self.term = Terminal ()
        else:
            # Inicializa a interface grafica (nao implementada)
            self.term = Terminal ()

        # Requisita o ip do host
        self.ip = self.term.leIp ()

        # Requisita a porta do cliente
        self.porta = self.term.lePorta ()

        # Requisita o caminho do arquivo
        self.nomeArquivo = self.term.leCaminhoArquivo ('Digite nome (caminho completo) do arquivo a enviar')

