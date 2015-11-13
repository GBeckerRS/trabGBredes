#!/usr/bin/env/python

class Arquivo:
    # Construtor
    def __init__ (self, nome):
        self.nome = nome
        self.estado = ''
        self.arq = None

    def abre (self, modo):
        print 'Abrindo o arquivo'
        if (self.estado != ''):
            return -1 # Arquivo esta aberto

        try:
            if (modo.find ('b') == -1):
                self.arq = open (self.nome, 'r')
            else:
                self.arq = open (self.nome, 'rb')
        except IOError as ex:
            print 'Handling error: ', ex
            raise

        self.estado = 'LEITURA'
        return True

    def le (self):
        print 'le o arquivo'
        if (self.arq is None):
            return -1   # Arquivo nao esta aberto
        if (self.estado != 'LEITURA'):
            return -11  # Arquivo nao esta em modo de leitura

        s = self.arq.read ()

        return s

    def escreve (self):
        print 'Escreve no arquivo'
        if (self.arq is None):
            return -1   # Arquivo nao esta aberto
        if (self.estado != 'ESCRITA'):
            return -20  # Arquivo nao esta em modo de escrita

    def fecha (self):
        print 'fechando o arquivo'
        if (self.arq is not None):
            try:
                self.arq.close ()
            except ValueError as ex:
                print 'Handling error: ', ex
                raise
                
            self.nome = ''
            self.estado = ''
            self.arq = None

