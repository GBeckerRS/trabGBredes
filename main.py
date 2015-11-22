#!/usr/bin/env/python 

import gtk, gtk.glade

from terminal import *
from servidor import *
from cliente import *

def main ():
    term = Terminal ()  # Interface de texto
    interface = ""
    servidor = None
    cliente = None

    # Mensagem de abertura do programa
    msgBoasVindas ()

    # 
    s = term.leTeclado ('Iniciar a interface grafica (s = sim)?', False)
    if (s == "s" or s == "S"):
        # Inicia a interface grafica...
        print 'Recurso de interface esta desabilitado...'
        interface = "N"
    else :
        # Inicia a interface de texto...
        print 'Inicia a interface de texto...'
        interface = "N"

    #
    s = int (term.leTeclado ('1 - Servidor, 2 - Cliente', True))
    if (s == 1):
        # Inicia o app com servidor
        servidor = Servidor (interface)
        servidor.executa ()
    else:
        cliente = Cliente (interface)
        cliente.executa ()

def msgBoasVindas ():
    print 10 * '='
    print 'TAREFA: envio de dados via protocolo UDP'
    print 10 * '='

if __name__ == '__main__':
    main ()

