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


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys
import MySQLdb as mdb


class Window(QDialog):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title = "Codeloop.org - PyQt5 Database"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        # Initialize window
        self.InitWindow()


    def InitWindow(self):
        # Create a button for database connection
        self.button = QPushButton('DB Connection', self)
        self.button.setGeometry(100, 100, 200, 50)
        self.button.clicked.connect(self.DBConnection)

        # Set window icon and properties
        self.setWindowIcon(QtGui.QIcon("codeloop.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


    def DBConnection(self):
        try:
            # Attempt to connect to the database
            db = mdb.connect(host="localhost", user="root", password = "25062000", db="mydbcf")
            cursor = db.cursor()
            query = "SELECT * FROM login_table"
            cursor.execute("SELECT VERSION()")
            data = cursor.fetchone()
            print("Database version : %s " % data)
            # Display success message
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')

        except mdb.Error as e:
            # Display error message if connection fails
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            # Exit the application with error code
            sys.exit(1)


# Create the application instance
App = QApplication(sys.argv)
# Create the main window instance
window = Window()
# Start the application event loop
sys.exit(App.exec())