from twisted.internet import protocol, reactor

class Hello(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write('Hello, ' + data)

class Bonjour(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write('Bonjour, ' + data)

helloFactory = protocol.Factory()
helloFactory.protocol = Hello
reactor.listenTCP(1234, helloFactory)

bonjourFactory = protocol.Factory()
bonjourFactory.protocol = Bonjour
reactor.listenTCP(1235, bonjourFactory)

reactor.run()
