from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
import mysql.connector
import MySQLdb as mdb
import pymysql

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt with MySQL")
        self.setGeometry(100, 100, 600, 400)

        label = QLabel("Connecting to Database...", self)
        label.move(50, 50)

        try:
            mydb = pymysql.connect(
                host="sql.freedb.tech",
                user="freedb_saloni",
                password="Xyk$b8T!MNGQh&T",
                database="freedb_mydbcf"
            )
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM login_table")
            data = cursor.fetchall()
            label.setText("Data retrieved successfully")
            print(data)
            mydb.close()
        except mysql.connector.Error as err:
            label.setText(f"Error: {err}")
            print(f"Error: {err}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
