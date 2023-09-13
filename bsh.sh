#!/bin/bash
echo "Enter your username:"
read -p "username: " username
read -sp "password: " password
echo
echo "username: $username - password: $password"

a=10
b=20
if [ $a -gt $b ];
then
echo "a is bigger"
else
echo "b is bigger"
fi

for i in {0..20..2}
do
if [ $i == 10 ];
then
continue
fi
echo "$i"
done
