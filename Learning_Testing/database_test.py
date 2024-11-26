# import mysql.connector  # or pymysql if you're using that
#
# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="25062000",
#         database="mydbcf"
#     )
#     mycursor = mydb.cursor()
#     mycursor.execute("select * from login_table")
#     result = mycursor.fetchone()
#     print(result)
#     print("Connection successful")
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
import requests

# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
# import sys
# import MySQLdb as mdb
#
#
# class Window(QDialog):
#     def __init__(self):
#         super().__init__()
#
#         # Window properties
#         self.title = "Codeloop.org - PyQt5 Database"
#         self.top = 200
#         self.left = 500
#         self.width = 400
#         self.height = 300
#
#         # Initialize window
#         self.InitWindow()
#
#
#     def InitWindow(self):
#         # Create a button for database connection
#         self.button = QPushButton('DB Connection', self)
#         self.button.setGeometry(100, 100, 200, 50)
#         self.button.clicked.connect(self.DBConnection)
#
#         # Set window icon and properties
#         self.setWindowIcon(QtGui.QIcon("codeloop.png"))
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.show()
#
#
#     def DBConnection(self):
#         try:
#             # Attempt to connect to the database
#             db = mdb.connect(host="localhost", user="root", password = "25062000", db="mydbcf")
#             cursor = db.cursor()
#             query = "SELECT * FROM login_table"
#             cursor.execute("SELECT VERSION()")
#             data = cursor.fetchone()
#             print("Database version : %s " % data)
#             # Display success message
#             QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
#
#         except mdb.Error as e:
#             # Display error message if connection fails
#             QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
#             # Exit the application with error code
#             sys.exit(1)
#
#
# # Create the application instance
# App = QApplication(sys.argv)
# # Create the main window instance
# window = Window()
# # Start the application event loop
# sys.exit(App.exec())



# # Save this as a Python script (e.g., test_connection.py) and run it outside of PyCharm
# import mysql.connector
# import MySQLdb as mdb
#
# try:
#     connection = mdb.connect(
#         host='192.168.0.1',
#         user='if0_37687278',
#         password='Santosh2506',
#         database='if0_37687278_mydbcf',
#         port=3306
#     )
#     if connection.is_connected():
#         print("Connected successfully from outside PyCharm")
#
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
#
# finally:
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    # Launch the browser in headless mode
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to the URL
    page.goto('http://smmydomain.infinityfreeapp.com/database_api.php?operation=read&table=login_table')

    # Get the raw response content
    content = page.content()

    # Extract the JSON part from the content
    start = content.find('[')
    end = content.rfind(']') + 1

    if start != -1 and end != -1:
        json_data = content[start:end]
        try:
            parsed_data = json.loads(json_data)  # Parse the JSON string into Python data
            print(parsed_data)  # Print or use the parsed data
        except json.JSONDecodeError:
            print("Failed to parse JSON data")
    else:
        print("JSON data not found in the response")

    # Close the browser
    browser.close()
