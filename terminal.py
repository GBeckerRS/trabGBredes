#!/usr/bin/env/python

class Terminal:
    def __init__ (self):
        print ''

    def leIp (self):
        return self.leTeclado ('Digite o IP do host', False) 

    def lePorta (self):
        return self.leTeclado ('Digite o PORTA do host', True) 

    def leCaminhoArquivo (self):
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

