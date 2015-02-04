#!/usr/bin/python
import sys
import socket
import string

HOST = "irc.freenode.net"
PORT = 6667
NICK = "pynorcio"
IDENT = "pynorcio"
REALNAME = "Python IRC Bot"
CHANNELS = ["#Neo31", "#pynorcio"]
readbuffer = ""

s = socket.socket()
s.connect((HOST, PORT))

s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

for channel in CHANNELS:
    s.send("JOIN " + channel + " :Hello \r\n")

while 1:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop( )
    for line in temp:
        line = string.rstrip(line)
        line = string.split(line)
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        elif (line[1] == "PRIVMSG"):
            sndr = line[0]
            rcvr = line[2]
            msg = line[3]
            print "sender is : ", sndr
            print  "receiver is : ", rcvr
            print  "message is : ", msg
            if (line[3]==":PING"):
                s.send("PRIVMSG "+line[2]+" :PONG\r\n")
            elif (line[3]==":whois"):
                s.send("PRIVMSG "+line[2]+" :My name is "+REALNAME+", and I am a python IRC bot.\r\n")

