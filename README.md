# client_server_interface
Instruction on how to navigate databases outside of a database GUI. This will focus on connections to a MySQL database via python

Database Client - Server interface
Alternatives to navigating a database outside of the IDE, including the MySQL shell, the operating systems’ command line, and programming languages, such as Python. 

Use Visual Studio Code and Python as tools for programatically connecting to the database. Ensure these programs are installed.

# Background
## What Is a Server? What Is a Client?
Within a network, a computer machine that shares resources, such as memory, hard drives, and printers, with other computers is called a server. Servers also provide access to data or particular services, such as large-scale computations. Within the same networks, any other computer that is not a server is called a client. Clients are generally capable of receiving information or using a particular service from the server.
Therefore, servers are usually more powerful and expensive machines because they share their resources with other computers in the network. Clients are less powerful machines, and you can think of them as personal computers that users operate to connect to a server. The clients’ machines don’t need to be extremely powerful because, generally, they don’t need to share resources with other computers.
## What Is a Client-Server Interface?
As you know, a user can perform data analysis on a database using SQL locally. This means that the database is stored on the user machine and all the operations happen on the user’s computer. However, SQL works particularly well on a client-server system. In this case, users on different clients’ machines can access a database that is stored on a server machine via wired communications (i.e., LAN) or online channels.
In this specific case, the computer you are using to manipulate a database and where you have installed MySQL Workbench is the client and, so far, you have only performed operations locally.
In the last video, you learned how to extend the applications of SQL by using a different type of client by using a Python driver that acts on the database.
## What Is a Driver?
Let’s try to understand what a driver is with an example.
You have probably heard of the word driver when installing a printer on your machine. Imagine you are working in an office where multiple printers are connected to a network and you want to print a certain document from a specific printer.
It would be convenient to simply say "print this document" but, of course, because each printer is unique, the signal cannot be exactly the same for all the printers in your office. In fact, as you probably know, if you don’t specify which printer you want to connect to, you won’t be able to print anything.
Here’s where drivers become useful. Rather than having to send a different signal to each type of printer (and hoping that one works for you), it is more convenient to locally install a driver for a particular printer that translates the "print this document" command into something more specific that the desired printer hardware needs to understand.
In other words, a driver is a piece of software related to hardware that contains a mapping/translation so that an operating system can communicate with hardware. It's a piece of code that sits between a program and hardware.
In conclusion, both servers and clients can use drivers for communication whenever it is necessary.
# Connect to MySQL via Terminal
MySQL can be navigated through the terminal on a Mac. This can be accomplished as follows: 
- After installing MySQL, open up a terminal
- Navigate to MySQL location on the local machine, `cd / usr/local/mysql/bin; ls`
- Connect to the MySQL database, `./mysql -u root -p`. Then, enter the password when prompted
From here, you’ll know you’re connected to the database by observing the ‘mysql>’ header at each line. From here, queries can be executed just as they would within the MySQL Workbench. 
# Connect to MySQL via Python
## Install the Driver on Mac
There are several drivers that will connect with MySQL. The driver of choice for this exercise is the mysql-connector-python. It can be downloaded via the following command: 
`pip install mysql-connector-python`
Note: this is a different driver than the “mysql-connector” driver. 
## Connect Programmatically to database from VS Code and read data
A connection to a database from a python file will have the following format: 
- Add the MySQL and yaml drivers
- Add the connection string. This will be different depending on whether the YAML file is used to authenticate vs. the authentication is included within he python file
- Add a connection string
- Create a cursor class, which includes the SQL query
- Create a loop to display all rows of the query
- Close the cursor and connection
These steps are illustrated in [this SQL file](mysql_connect.py)

## Write data via Python
Writing data from a python file is executed in a similar fashion: 
- Add drivers (MySQL and YAML)
- Add connection string
- Include input parameters
- Create Cursor, including insert query
- Read content from entry
- Print all rows
- Close the cursor and connection
These steps are illustrated in [this SQL file](create.py)

## YAML files for authentication security

YAML: acronym for ‘yet another markup language,’ is used as a format for configuration files, but its main objective is data serialization. In this case, it’s a convenient format for removing the password from the connection string. See [this YAML file for an example](db.yaml)

