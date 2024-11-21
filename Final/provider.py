from Handler import myHandler
import string
import datetime
import pytz

class Provider():
    def __init__(self,ip_addr,udp_port) -> None:
        self.handler = myHandler(ip_addr,udp_port=udp_port)

        self.handler.thread_init()

    def registerService(self,ip_serv_mark):
        pass

    def provideService(self,opt,data):
        if opt == '1':
            reply = self.getHour(data)
        elif opt == '2':
            reply = self.resolveDomainName(data)
        elif opt == '3':
            reply = self.cesarEncrypt(data)
        else:
            reply = 'None'

    def getHour(self,data):
        col_tz = pytz.timezone('America/Bogota')
        de_tz = pytz.timezone('Europe/Berlin')
        it_tz = pytz.timezone('Europe/Rome')
        if data == "CO":
            hora = datetime.datetime.now(col_tz)
            hora = hora.strftime("%H:%M:%S")
            reply = "Hora Colombia: " + hora
        elif data == "DE":
            hora = datetime.datetime.now(de_tz)
            hora = hora.strftime("%H:%M:%S")
            reply = "Hora Alemania: " + hora
        elif data == "IT":
            hora = datetime.datetime.now(it_tz)
            hora = hora.strftime("%H:%M:%S")
            reply = "Hora Italia: " + hora
        else:
            hora = datetime.datetime.now(it_tz)
            hora = hora.strftime("%H:%M:%S")
            reply = "Hora Italia: " + hora
        return reply

    def resolveDomainName(self,data):
        pass

    def cesarEncrypt(self,text,n=3):
        # alphabet "abcdefghijklmnopqrstuvwxyz"
        intab = string.ascii_lowercase
        # alphabet shifted by n positions
        outtab = intab[n % 26:] + intab[:n % 26]
        # translation made b/w patterns
        trantab = str.maketrans(intab, outtab)
        # text is shifted to right
        return text.translate(trantab)





    
