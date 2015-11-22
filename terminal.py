#!/usr/bin/env/python

class Terminal:
    def __init__ (self):
        print 'Criando o objeto Terminal...'

    def leIp (self):
        print 'Le o IP do host'
        return self.leTeclado ('Digite o IP do host', False) 

    def lePorta (self):
        print 'Le a porta de conexao...'
        return self.leTeclado ('Digite o PORTA do host', True) 

    def leCaminhoArquivo (self):
        print 'Le o caminho completo do arquivo...'
        return self.leTeclado ('Digite o caminho do arquivo a enviar', False) 

    def leTeclado (self, mensagem, ehNumero):
        print mensagem
        tmp = ""
        while tmp == "":
            tmp = raw_input (" --> ")
            if ehNumero == True and not tmp.isdigit () and tmp != "":
                print 'Entrada invalida, use apenas numeros. Voce digitou: {0}'.format (tmp)
                tmp = ""
            if tmp != "":
                r = raw_input ("Voce digitou \'{0}\', esta correto? (s = sim): ".format (tmp))
                if (r == "s" or r == "S"):
                    break
                else:
                    tmp = ""

        return tmp

