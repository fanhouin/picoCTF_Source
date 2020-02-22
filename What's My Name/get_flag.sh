#/!bin/bash

strings myname.pcap | grep -oE "picoCTF{.*}"
