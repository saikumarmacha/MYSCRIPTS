#!/bin/bash

for thisHOST in $(cat host.txt); do 
#Should change create a text file **host.txt** which contain all the Hosts to which the directory has to be copied
#should have to give *password* as argument....
sshpass  -p $1 scp -o StrictHostKeyChecking=no -r /your/path/ USER@$thisHOST:/destination/path/
done