from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json
app = Flask(__name__)
DB_conf = { 'user': 'root', 'password': 'root', 'host': 'db',
            'port': '3306', 'database': 'images' }
def test_table():
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   cursor.execute('SELECT * FROM imagelinks')
   results = [c for c in cursor]
   cursor.close()
   connection.close()
   return results

def add_item(title, link, descr):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"INSERT INTO imagelinks (title, link, descr) VALUES ('{title}', '{link}', '{descr}');"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

def delete_item(title):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"DELETE FROM imagelinks WHERE title = '{title}';"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

def style():
    S  = "<style>\n"
    S += "   body {background-color: #F9F5F1;\n"
    S += "         font-family: Helvetica;\n"
    S += "         color: #543B46;"
    S += "         letter-spacing: 1px;}\n"
    S += "   ul.menu {list-style-type: none;"
    S += "            margin: 0;"
    S += "            padding: 0;"
    S += "            overflow: hidden;"
    S += "            background-color: #ABD1B5;}"
    S += "   .imgLi {margin-bottom: 20px;\n"
    S += "           list-style-type: none;}"
    S += "   .menuLi {float: left;} "
    S += "   .menuLi a {display: block; "
    S += "            color: #543B46;"
    S += "            text-align: center;"
    S += "            padding: 14px 16px;"
    S += "            text-decoration: none;"
    S += "            font-weight: bold;}"
    S += "   .menuLi a:hover {background-color: #89BE97;}"
    S += "   .button {background-color: #ED6A5A;"
    S += "            border: none;"
    S += "            padding: 12px;"
    S += "            border-radius: 2px;}"
    S += "   input {padding: 10px;}"
    S += "   img {margin: 15px 0px;}"
    S += "</style>\n"
    return S

def menu():
   S = "  <ul class='menu'>"
   S += "    <li class='menuLi'><a href='/'>Homepage</a></li>\n"
   S += "    <li class='menuLi'><a href='/addform'>Addform</a></li>\n"
   S += "    <li class='menuLi'><a href='/deleteform'>Deleteform</a></li>\n"
   S += "  </ul>"
   return S

@app.route('/add')
def add():
   title = request.args.get("title", "", str)
   link = request.args.get("link", "", str)
   descr = request.args.get("descr", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Added an image</title>\n"
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Added an image</h1>\n"
   if title != "" and link != "" and descr != "":
      S += add_item(title, link, descr)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/delete')
def delete():
   title = request.args.get("title", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Delete an image</title>\n"
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Delete an image</h1>\n"
   if title != "":
      S += delete_item(title)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/addform')
def addform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "   <head>\n"
    S += "      <title>Add a dog breed to the list</title>\n"
    S += style()
    S += "   </head>\n"
    S += "   <body>\n"
    S += menu()
    S += "      <h1>Add a dog breed to the list</h1>\n"
    S += "      <form action='/add'>\n"
    S += "        <input type='text' name='title' value='Title'/>\n"
    S += "        <input type='url' name='link' value='Link to image'/>\n"
    S += "        <input type='text' name='descr' value='Description'/>\n"
    S += "        <input class='button' type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/deleteform')
def deleteform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "   <head>\n"
    S += "      <title>Delete a dog breed from the list</title>\n"
    S += style()
    S += "   </head>\n"
    S += "   <body>\n"
    S += menu()
    S += "      <h1>Delete a dog breed from the list</h1>\n"
    S += "      <form action='/delete'>\n"
    S += "        <input type='text' name='title' value='Title'/>\n"
    S += "        <input class='button' type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S

@app.route('/')
def index():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Images list</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += menu()
   S += "      <ul>\n"
   S += "      <h2>IMAGE LIST:</h2>\n"
   for (title, link, descr) in test_table():
      S += f"         <li class='imgLi'><b>{title}</b><br>{descr}.<br><i>{link}</i><br>\n"
      S += f" <a href='{link}' target='_blank'>\n"
      S += f"<img src='{link}' width='70' height='auto'>\n"
      S += "</a></li>\n"
   S += "      </ul>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

if __name__ == '__main__':
    app.run(host='0.0.0.0')