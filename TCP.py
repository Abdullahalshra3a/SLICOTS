from scapy.all import *
import sys, os


    
#A script to generate packets to destination 10.0.0.9, using the source ip of the sending node using UDP
#you can run this script from any node you want'''


def generatePackets():
      if len(sys.argv) != 4:
        print "Usage: arping2tex <net>\n eg: arping2text 192.168.1.0/24"
        sys.exit(1)
      src= sys.argv[1]
      dst= sys.argv[2]
      x = int(sys.argv[3])
      os.system("iptables -A OUTPUT  -p tcp --sport 2234 --tcp-flags RST RST -j DROP")
    # three way handshake
      ip=IP(src= src, dst=dst)
      SYN=TCP(sport= 2235,dport=5546,flags='S', seq=0)
      pkt = (ip/SYN)
      #pkt.show()
      SYNACK=sr1(pkt)
      seq = SYNACK.seq+1
      #ACK
      ACK=TCP(sport = 2235, dport=5546, flags='A', seq=0, ack =seq)
      pkt = (ip/ACK)
      send(pkt)
      #ACK.show()
      pkt= ip/TCP(sport = 2235, dport=5546 )/ "cat"
      send(pkt, count = x, inter=1./1000 )
      seq+= 1
      ACK=TCP(sport = 2235, dport=5546, flags='F', seq=0, ack =seq)
      pkt = (ip/ACK)
      send(pkt)
      seq+= 1
          
    
    
if __name__ == '__main__':
    generatePackets()

