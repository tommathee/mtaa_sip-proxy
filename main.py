import logging
import socketserver
import socket
import time
import sys
import sipfullproxy


if __name__ == "__main__":    
    #vypis do logov
    #logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
    #logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))

    sipfullproxy.hostname = socket.gethostname()
    logging.info(sipfullproxy.hostname)
    sipfullproxy.ipaddress = socket.gethostbyname(sipfullproxy.hostname)

    logging.info(sipfullproxy.ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.ipaddress,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy.ipaddress,sipfullproxy.PORT)
    print(f"Proxy server starting at {sipfullproxy.ipaddress}:{sipfullproxy.PORT}" )
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()
