NETWORKING IN PYTHON
--------------------

There are three requirements to establish a network:
1. Hardware : Includes the computers, cables, modems, routers, hubs, etc.
2. Software : Includes programs to communicate between servers and clients.
3. Protocol : Represents a way to establish connection and helps in sending and receiving data in a standard format.

Protocol : A protocol represents a set of rules to be followed by every computer on the network.
There are two types of protocol models based on which other protocols are developed:
*TCP/IP Protocol
*UDP

TCP/IP Protocol
---------------
Transmission Control Protocol / Internet Protocol is the standard protocol model used on any network, including Internet.

TCP / IP model has got the following five layers:
*Application layer - Topmost layer that directly interacts with an application or data. This layer receives
data from the application and formats the data.
*TCP - Upon receiving the data from the application layer, we will divide it into small segments called 'packets'.
*IP - IP layer inserts the packets into envelopes called 'frames.' Each frame contains a packet, the IP address
of destination computer, the IP address of source computer, some additional bits useful in
error detection and correction. These frames are then sent to Data link layer which dispatches them to
correct destination computer on the network.
*Data Link Layer - Dispatches the frames to correct destination computer on the network.
*Physical Layer - Transmits data on the network using the appropriate hardware.

DNS - Domain Name Service is a service on the internet that maps the IP addresses with corresponding website names.

HTTP Protocol - It is the most widely used protocol on the Internet, which is used to transfer web pages from
one computer to another on Internet.
FTP (File Transfer Protocol) - It is useful to download or upload files from and to the server.
SMTP (Simple Main Transfer Protocol) - It is useful to send mails on network.
POP (Post Office Protocol) - It is useful to receive mails into mail boxes.
NNTP (Network News Transfer Protocol) - It is used to transfer news articles on the Internet.

UDP (User Datagram Protocol) - USP is another protocol that transfers data in a connection less and unreliable manner.
It will not check how many bits are sent or how many bits are actually received at the other side.
UDP is used to send images, audio files, video files.

Sockets - It is possible to establish a logical connecting point between a server and a client so that communication
can be done through that point. The point is called 'socket'. Each socket is given and identification number,
which is called 'port number'. Port number takes 2 bytes and can be from 0 to 65,535.
Establishing communication between a server and a client using sockets is called 'socket programming'.

Port numbers from 0 to 1023 are used by our computer system for various applications and hence we should avoid using these
port numbers in our networking programs.

Port Number - Application or Service
13          - Date and time service
21          - FTP which transfers files
23          - Telnet, which provides remote login
25          - SMTP, which delivers mails
67          - BOOTP, which provides configuration at boot time
80          - HTTP, which transfers web pages
109         - POP2, which is a mailing service
110         - POP3, which is a mailing service
119         - NNTP, which is for transferring news articles