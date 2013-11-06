from twisted.internet import reactor

counter = 5

def hello(name):
    global counter
    if counter:
        print 'hello', name
        counter -= 1
        reactor.callLater(1, hello, 'world')
    else:
        reactor.stop()

reactor.callLater(1, hello, 'world')
reactor.run()

