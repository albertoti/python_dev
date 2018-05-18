import ctypes
import socket

ip_host	=	socket.gethostbyname(socket.gethostname())
message	=	"IP: "	+	ip_host
try:
	 print ctypes.windll.user32.MessageBoxA(0,message,"Titulo",0x40)
	
except:
	print "Error"