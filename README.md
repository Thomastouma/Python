# Graphical interface MYSQL connector written in python

A graphical database program written in python that uses tkinter to create the GUI allows the user to manage his "bookstore". You are able to delete, update, insert and view the data from your database all by pressing a simple button instead of wrinting sql code. This program is a big releif to people that dont know how to manage their database trough sql code, they can simply use our program that needs no knowledge about SQL code.

To use this program you need to change the mysql connector parameters in the back2.py file to your own database information.
conn = mysql.connector.connect(host='localhost', user='root', passwd='root', db='toumatest')
You also need to create the table book in your database with this sql syntax or preferably you can could create whatever table suits you and afterwards change the code in the program to match your database table.


#MYSQL syntax to create database table that matches the programs current data parameters.
Create table book(id int not null auto_increment primary key, title varchar(32), author varchar(32))) year int, default character set utf8;
