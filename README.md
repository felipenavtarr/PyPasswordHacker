# PyPasswordHacker
JetBrains Academy project from the Python Core track

## Stage 1/5: Establishing a connection
### Description
Imagine some admin who runs a website on the Internet. The site is becoming very popular, and a lot of people register. Filling in their profiles, they leave some information there that is not meant to be public, for example, information about their credit cards.

The admin completely forgot about the security of the site, so now you can log in with admin privileges without even having a login and password!

The first task of this project is to go to the admin's site; it will immediately give out all the secret information. Remember, as soon as you enter the site as an admin, you will automatically obtain all the private data of the site. It will get harder: the tasks of all other stages of the project will be to crack the admin password. Good luck!

Your program should connect to the server using an IP address and a port from the command line arguments. You can use socket module to create this program.

### Objectives
**Your program will receive command line arguments in this order:**
IP address
port
message for sending

**The algorithm is the following:**
1. Create a new socket.
2. Connect to a host and a port using the socket.
3. Send a message from the third command line argument to the host using the socket.
4. Receive the server’s response.
5. Print the server’s response.
6. Close the socket.

### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:
```
> python hack.py localhost 9090 password
Wrong password!
```
Example 2:
```
> python hack.py 127.0.0.1 9090 qwerty
Connection Success!
```
