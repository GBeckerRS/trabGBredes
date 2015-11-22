#!/usr/bin/env/python

class Socket:
    def __init__ (self, ip, porta):
        self.host = (ip, porta)
        self.ip = ip
        self.porta = porta

    def getHost (self):
        return self.host

    def getIp (self):
        return self.ip

    def getPorta (self):
        return self.porta

    def setHost (self, ip, porta):
        self.host = (ip, porta)
        self.ip = ip
        self.porta = porta

    def setIp (self, ip):
        self.host = (ip, self.porta)
        self.ip = ip

    def setPorta (self, porta):
        self.host = (ip, self.porta)
        self.porta = porta

