
import sys
from scapy.all import *

zero_mac="00:00:00:00:00:00"
input_filename=""

def zerolize_mac(in_filename,out_filename):
    pkts=rdpcap(in_filename)
    for pkt in pkts:
        pkt[Ether].src=zero_mac
        pkt[Ether].dst=zero_mac
        wrpcap(out_filename,pkt)
        

if __name__ =='__main__':
    print('Pcap Zerolization')
    args=sys.argv
    
    if len(args)<2:
        print('Usage '+ args[0] + ' input filename output filename')
        exit()
    input_filename=args[1]
    if len(args)==2:
        output_filename=input_filename+"_output"
    else:
        output_filename = args[2]
    zerolize_mac(args[1],output_filename)
    print('Complete outputfile is ' + output_filename)