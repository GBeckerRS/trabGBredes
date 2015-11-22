#!/usr/bin/env/python

class Arquivo:
    # Construtor
    def __init__ (self, nome):
        self.nome = nome
        self.estado = ''
        self.arq = None
        print 'Criado o objeto Arquivo...'

    def abre (self, modo):
        if (self.estado != ''):
            return -1 # Arquivo esta aberto

        try:
            self.arq = open (self.nome, modo)
        except IOError as ex:
            print 'Handling error: ', ex
            raise
        print 'Abriu o arquivo...'

        if (modo == 'r'):
            self.estado = 'LEITURA'
        else:
            self.estado = 'ESCRITA'

        return 1

    def le (self):
        print 'le o arquivo'
        if (self.arq is None):
            return -1   # Arquivo nao esta aberto
        if (self.estado != 'LEITURA'):
            return -11  # Arquivo nao esta em modo de leitura

        s = self.arq.read ()
        print 'Leu dados do arquivo...'

        return s

    def escreve (self, dados):
        print 'Escreve no arquivo'
        if (self.arq is None):
            return -1   # Arquivo nao esta aberto
        if (self.estado != 'ESCRITA'):
            return -20  # Arquivo nao esta em modo de escrita

        self.arq.write (dados)
        print 'Escreveu dados no arquivo...'

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
            print 'Fechou o arquivo...'

