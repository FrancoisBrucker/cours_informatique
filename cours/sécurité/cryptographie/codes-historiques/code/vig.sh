#!/bin/sh

a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

[ $1 ] && [ "$1" != "-d" ] && echo "Usage: $0 [-d]" && exit 1

m=${1:+-}

printf "string: ";read t
printf "keyphrase: ";read -s k
printf "\n"
for ((i=0;i<${#t};i++)); do
  p1=${a%%${t:$i:1}*}
  p2=${a%%${k:$((i%${#k})):1}*}
  d="${d}${a:$(((${#p1}${m:-+}${#p2})%${#a})):1}"
done
echo "$d"
