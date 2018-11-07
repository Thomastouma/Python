# ThomasAndKristianProgram
Thomas and Kristians python program for "python fördjupning"


We have created a graphical database program in python with tkinter that allows the user to manage his "bookstore". You are able to delete, update, insert and view the data from your database all by pressing a simple button instead of wrinting sql code. This program is a big releif to people that dont know how to manage their database trough sql code, they can simply use our program that needs no knowledge about sql code.

To use this program you need to change the mysql connector parameters in the back2.py file to your own database information.
conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='toumatest')
You also need to create the table book in your database with this sql syntax.
Create table book(id int not null auto_increment primary key, title varchar(32), author varchar(32))) year int, default character set utf8;
