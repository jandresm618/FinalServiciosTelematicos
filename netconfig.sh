#!bin/bash

if [ "$#" -ne 4 ]; then
	echo "Usage : $0 [IP] [MASK] [GW] [DNS]"
	exit 1
fi

IP=$1
MASK=$2
GW=$3
DNS=$4

sudo ip addr add $IP/$MASK dev enp0s3

sudo ip route add default via $GW

echo "nameserver $DNS" | sudo tee /etc/resolv.conf > /dev/null


ip link set enp0s3 up
