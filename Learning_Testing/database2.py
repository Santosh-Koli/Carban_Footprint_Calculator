import sys
import faulthandler
import pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
faulthandler.enable()


class LoginApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI components
        self.setWindowTitle("Simple Login App")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password characters
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

        # Connect button click to login function
        self.login_button.clicked.connect(self.check_login)

    def check_login(self):
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="your_password",
                database="mydbcf"
            )
            cursor = connection.cursor()
            print("connection successful")
            query = "SELECT * FROM login_table WHERE User = %s AND Password = %s"
            cursor.execute(query, ("aalvin", "dfsd"))
            result = cursor.fetchone()
            if result:
                self.show_message("Login Successful", "Welcome to the application!")
            else:
                self.show_message("Login Failed", "Incorrect username or password.")
            connection.close()
        except pymysql.MySQLError as e:
            print(f"Database Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
