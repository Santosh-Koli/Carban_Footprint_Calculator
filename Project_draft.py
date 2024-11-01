import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QTabWidget, \
    QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QStyledItemDelegate, QTableWidget, QTableWidgetItem, QRadioButton, \
    QMessageBox
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class IconDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(IconDelegate, self).__init__(parent)
        # Load tick and cross icons
        self.tick_icon = QIcon("tick.png")  # Path to tick icon image
        self.cross_icon = QIcon("cross.png")  # Path to cross icon image

    def paint(self, painter, option, index):
        # Get the value from the second column for comparison
        table = index.model().parent()  # Get the QTableWidget
        value = table.item(index.row(), 1).text()  # Second column value

        # Choose the icon based on the condition
        icon = self.cross_icon if value == "Warning" else self.tick_icon

        # Draw the icon in the third column
        icon.paint(painter, option.rect)


class CarbonFootprintCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carbon Footprint Calculator")
        self.setGeometry(100, 100, 600, 600)
        self.setFixedWidth(800)
        self.initUI()
        self.carbonCalculator = {}
        self.carbonCalculator.setdefault("Details", {})
        self.carbonCalculator.setdefault("Energy", {})
        self.carbonCalculator.setdefault("Waste", {})
        self.carbonCalculator.setdefault("Travel", {})
        self.carbonCalculator.setdefault("Results", {})

    def initUI(self):
        stylesheet = """
            QMainWindow {
                background-image: url("D:/_Qt/img/cat.jpg"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        validator = QtGui.QDoubleValidator()  # Create validator.
        validator.setRange(0, 9999.0, 1)

        # self.setStyleSheet()
        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.my_font = QtGui.QFont()
        self.my_font.setBold(True)

        # Create the tab widget and add tabs
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.addTab(self.tab1, "Welcome")
        self.tabs.addTab(self.tab2, "Energy")
        self.tabs.addTab(self.tab3, "Waste")
        self.tabs.addTab(self.tab4, "Travel/Transport")
        self.tabs.addTab(self.tab5, "Results")
        self.tabs.addTab(self.tab6, "Visualization")

        # Add widgets to the first tab
        self.tab1_layout = QGridLayout(self.tab1)
        background = QLabel()
        # Load the image using QPixmap
        pixmap = QPixmap('cfc_2.jpg')
        scaled_pixmap = pixmap.scaled(800, 600)

        # Set the pixmap to the label
        background.setPixmap(scaled_pixmap)
        background.setScaledContents(True)
        background.setToolTip(
            "Welcome to the Carbon Footprint Calculator!\n\nThis tool helps you understand and reduce your carbon footprint. "
            "Every small action counts toward a healthier planet.\nCalculate your emissions, get insights, and track your impact with tables & charts  for a sustainable future. ")

        # self.tab1_title = QLabel("Carbon Footprint Calculator")
        # self.tab1_title.setFont(QFont("Arial", 38, QFont.Bold))
        self.individual_rbtn = QRadioButton("Individual")
        self.individual_rbtn.setFont(QFont("Arial", 11, QFont.Bold))
        self.individual_rbtn.setChecked(True)
        self.sbusiness_rbtn = QRadioButton("Small Business Firm")
        self.sbusiness_rbtn.setFont(QFont("Arial", 11, QFont.Bold))
        self.bbusiness_rbtn = QRadioButton("Big Business Firm")
        self.bbusiness_rbtn.setFont(QFont("Arial", 11, QFont.Bold))
        self.tab1_name_label = QLabel("Name:")
        self.tab1_name_input = QLineEdit()
        self.tab1_name_input.setPlaceholderText("Enter your name")
        self.tab1_year_label = QLabel("Year:")
        self.tab1_year_input = QComboBox()
        self.tab1_year_input.addItems(["2021", "2022", "2023", "2024", "2025"])
        self.tab1_year_input.setCurrentIndex(3)
        self.tab1_next_button = QPushButton("Next")
        self.tab1_next_button.clicked.connect(lambda: self.switchTab(1))
        # self.tab1_layout.addWidget(self.tab1_title, 0, 0, 1, 8)
        self.tab1_layout.addWidget(background, 0, 0, 1, 8)
        self.tab1_layout.addWidget(self.individual_rbtn, 1, 0, 1, 2)
        self.tab1_layout.addWidget(self.sbusiness_rbtn, 1, 3, 1, 2)
        self.tab1_layout.addWidget(self.bbusiness_rbtn, 1, 6, 1, 2)
        self.tab1_layout.addWidget(self.tab1_name_label, 2, 0, 1, 1)
        self.tab1_layout.addWidget(self.tab1_name_input, 2, 1, 1, 7)
        self.tab1_layout.addWidget(self.tab1_year_label, 3, 0, 1, 1)
        self.tab1_layout.addWidget(self.tab1_year_input, 3, 1, 1, 7)
        self.tab1_layout.addWidget(self.tab1_next_button, 4, 7, 1, 1)
        self.tab1_name_input.editingFinished.connect(lambda: self.carbonCalculator_func("Details"))
        self.tab1_year_input.currentIndexChanged.connect(lambda: self.carbonCalculator_func("Details"))
        # self.tab1_layout.setAlignment(Qt.AlignAbsolute)

        # Add widgets to the second tab
        self.tab2_layout = QGridLayout(self.tab2)
        self.tab2_layout.setAlignment(Qt.AlignCenter)

        self.tab2_input_layout = QGridLayout()
        self.tab2_input_layout.addWidget(QLabel("What is your average monthly electricity bill in euros?"), 0, 0)
        self.tab2_input_layout.addWidget(QLabel("What is your average monthly natural gas bill in euros?"), 1, 0)
        self.tab2_input_layout.addWidget(QLabel("What is your average monthly fuel bill for transportation in euros?"),
                                         2, 0)
        self.tab2_electricity_input = QLineEdit()
        self.tab2_gas_input = QLineEdit()
        self.tab2_fuel_input = QLineEdit()
        self.tab2_electricity_input.setValidator(validator)
        self.tab2_gas_input.setValidator(validator)
        self.tab2_fuel_input.setValidator(validator)
        self.tab2_input_layout.addWidget(self.tab2_electricity_input, 0, 1)
        self.tab2_input_layout.addWidget(self.tab2_gas_input, 1, 1)
        self.tab2_input_layout.addWidget(self.tab2_fuel_input, 2, 1)
        self.tab2_layout.addLayout(self.tab2_input_layout, 0, 0, 1, 4)
        self.tab2_electricity_input.editingFinished.connect(lambda: self.carbonCalculator_func("Energy"))
        self.tab2_gas_input.editingFinished.connect(lambda: self.carbonCalculator_func("Energy"))
        self.tab2_fuel_input.editingFinished.connect(lambda: self.carbonCalculator_func("Energy"))

        self.tab2_previous_button = QPushButton("Previous")
        self.tab2_previous_button.clicked.connect(lambda: self.switchTab(0))
        self.tab2_next_button = QPushButton("Next")
        self.tab2_next_button.clicked.connect(lambda: self.switchTab(2))
        self.tab2_layout.addWidget(self.tab2_previous_button, 5, 0)
        self.tab2_layout.addWidget(self.tab2_next_button, 5, 3)

        # Add widgets to the third tab
        self.tab3_layout = QGridLayout(self.tab3)
        self.tab3_layout.setAlignment(Qt.AlignCenter)

        self.tab3_input_layout = QGridLayout()
        self.tab3_input_layout.addWidget(QLabel("How much waste do you generate per month in kilograms?"), 0, 0)
        self.tab3_input_layout.addWidget(QLabel("How much of that waste is recycled or composted(in %)?"), 1, 0)
        self.tab3_waste_generated = QLineEdit()
        self.tab3_waste_recycle = QLineEdit()
        self.tab3_waste_generated.setValidator(validator)
        self.tab3_waste_recycle.setValidator(validator)
        self.tab3_input_layout.addWidget(self.tab3_waste_generated, 0, 1)
        self.tab3_input_layout.addWidget(self.tab3_waste_recycle, 1, 1)
        self.tab3_layout.addLayout(self.tab3_input_layout, 0, 0, 1, 4)
        self.tab3_waste_generated.editingFinished.connect(lambda: self.carbonCalculator_func("Waste"))
        self.tab3_waste_recycle.editingFinished.connect(lambda: self.carbonCalculator_func("Waste"))

        self.tab3_previous_button = QPushButton("Previous")
        self.tab3_previous_button.clicked.connect(lambda: self.switchTab(1))
        self.tab3_next_button = QPushButton("Next")
        self.tab3_next_button.clicked.connect(lambda: self.switchTab(3))
        self.tab3_layout.addWidget(self.tab3_previous_button, 4, 0)
        self.tab3_layout.addWidget(self.tab3_next_button, 4, 3)

        # Add widgets to the fourth tab
        self.tab4_layout = QGridLayout(self.tab4)
        self.tab4_layout.setAlignment(Qt.AlignCenter)

        self.tab4_input_layout = QGridLayout()
        self.tab4_input_layout.addWidget(
            QLabel("How many kilometers do your employees travel per year for business purposes?"), 0, 0)
        self.tab4_input_layout.addWidget(
            QLabel("What is the average fuel efficiency of the vehicles used for business travel in litres/100kms?"), 1,
            0)
        self.tab4_distance = QLineEdit()
        self.tab4_fuel_efficiency = QLineEdit()
        self.tab4_distance.setValidator(validator)
        self.tab4_fuel_efficiency.setValidator(validator)
        self.tab4_input_layout.addWidget(self.tab4_distance, 0, 1)
        self.tab4_input_layout.addWidget(self.tab4_fuel_efficiency, 1, 1)
        self.tab4_layout.addLayout(self.tab4_input_layout, 0, 0, 1, 4)
        self.tab4_distance.editingFinished.connect(lambda: self.carbonCalculator_func("Travel"))
        self.tab4_fuel_efficiency.editingFinished.connect(lambda: self.carbonCalculator_func("Travel"))

        self.tab4_previous_button = QPushButton("Previous")
        self.tab4_previous_button.clicked.connect(lambda: self.switchTab(2))
        self.tab4_next_button = QPushButton("Next")
        self.tab4_next_button.clicked.connect(lambda: self.switchTab(4))
        self.tab4_layout.addWidget(self.tab4_previous_button, 4, 0)
        self.tab4_layout.addWidget(self.tab4_next_button, 4, 3)

        # Add widgets to the fifth tab
        self.tab5gb = QGroupBox()
        self.tab5layout = QGridLayout()
        self.tab5gb.setLayout(self.tab5layout)

        self.tab5_layout = QGridLayout(self.tab5)
        # self.tab5_layout.setAlignment(Qt.AlignCenter)

        self.table = QTableWidget(3, 3)  # Set up a table with 3 columns
        self.table.verticalHeader().setVisible(False)
        # Set column headers
        self.table.setHorizontalHeaderLabels(["Operators", "Carbon Footprint", "Status"])
        self.table.horizontalHeader().setFont(self.my_font)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Populate the table with sample data
        self.table.setItem(0, 0, QTableWidgetItem("Energy"))
        self.table.setItem(1, 0, QTableWidgetItem("Waste"))
        self.table.setItem(2, 0, QTableWidgetItem("Business Travel"))

        for col in range(self.table.rowCount()):
            self.table.item(col, 0).setFlags(Qt.ItemIsEnabled)
            self.table.setItem(col, 1, QtWidgets.QTableWidgetItem())
            # self.table.item(col, 1).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.table.item(col, 1).setFlags(Qt.ItemIsEnabled)
            self.table.setItem(col, 2, QtWidgets.QTableWidgetItem())
            # self.table.item(col, 1).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.table.item(col, 2).setFlags(Qt.ItemIsEnabled)

        # Set custom delegate to the third column for displaying icons
        # delegate = IconDelegate(self.table)
        # self.table.setItemDelegateForColumn(2, delegate)
        self.tab5layout.addWidget(self.table, 0, 0)

        self.tab5_previous_button = QPushButton("Previous")
        self.tab5_previous_button.clicked.connect(lambda: self.switchTab(3))
        self.tab5_next_button = QPushButton("Next")
        self.tab5_next_button.clicked.connect(lambda: self.switchTab(5))
        self.tab5_calculate_button = QPushButton("Calculate")
        self.tab5_calculate_button.setFixedHeight(50)
        self.tab5_calculate_button.setFont(self.my_font)
        self.tab5_calculate_button.setStyleSheet('QPushButton {background-color: rgba(42, 161, 131); color: rgba(232, 237, 235); font-size: 16px}')
        self.tab5_layout.addWidget(self.tab5gb, 0, 0, 1, 3)
        self.tab5_layout.addWidget(self.tab5_previous_button, 1, 0)
        self.tab5_layout.addWidget(self.tab5_calculate_button, 1, 1)
        self.tab5_layout.addWidget(self.tab5_next_button, 1, 2)
        self.tab5_calculate_button.clicked.connect(self.calculate)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
        canvas = FigureCanvas(fig)
        canvas.setParent(self.tab6)

        # Add widgets to the sixth tab
        self.tab6_layout = QVBoxLayout()
        self.tab6_layout.addWidget(canvas)
        self.tab6.setLayout(self.tab6_layout)

        self.tab6_previous_button = QPushButton("Previous")
        self.tab6_previous_button.clicked.connect(lambda: self.switchTab(4))
        self.tab6_layout.addWidget(self.tab6_previous_button)

        # Add the tab widget to the main layout
        self.layout.addWidget(self.tabs)

    def carbonCalculator_func(self, module: str):
        if module == "Details":
            mod = str
            if self.individual_rbtn.isChecked():
                mod = "Individual"
            elif self.sbusiness_rbtn.isChecked():
                mod = "Small Business Firm"
            elif self.bbusiness_rbtn.isChecked():
                mod = "Big Business Firm"
            self.carbonCalculator["Details"].update(
                {"Module": mod, "Name": self.tab1_name_input.text(), "Year": self.tab1_year_input.currentText()})
        elif module == "Energy":
            self.carbonCalculator["Energy"].update(
                {"Electricity": self.tab2_electricity_input.text(), "NaturalGas": self.tab2_gas_input.text(),
                 "Fuel": self.tab2_fuel_input.text()})
        elif module == "Waste":
            self.carbonCalculator["Waste"].update(
                {"Waste_generated": self.tab3_waste_generated.text(), "Waste_recycle": self.tab3_waste_recycle.text()})
        elif module == "Travel":
            self.carbonCalculator["Travel"].update(
                {"Distance": self.tab4_distance.text(), "Fuel_Efficiency": self.tab4_fuel_efficiency.text()})
        # elif module == "Result":
        #     self.calculate()
            # energy_result = (float(self.carbonCalculator["Energy"]["Electricity"]) * 12 * 0.0005) + (float(self.carbonCalculator["Energy"]["NaturalGas"]) * 12 * 0.0053) + (float(self.carbonCalculator["Energy"]["Fuel"]) * 12 * 2.32)
            # waste_result = (float(self.carbonCalculator["Waste"]["Waste_generated"] * 12 * (0.57 - (float(self.carbonCalculator["Waste"]["Waste_generated"]/100)))))
            # travel_result = float(self.carbonCalculator["Travel"]["Distance"]) * (1/float(self.carbonCalculator["Travel"]["Fuel_Efficiency"] * 2.31))
            # self.table.setItem(0, 1, QTableWidgetItem(str(energy_result)))
            # self.table.setItem(1, 1, QTableWidgetItem(str(waste_result)))
            # self.table.setItem(2, 1, QTableWidgetItem(str(travel_result)))

            # self.carbonCalculator["Result"].update(
            #     {"Energy_CF": energy_result, "Waste_CF": waste_result, "Travel_CF": travel_result})

            # print(self.carbonCalculator)

    def calculate(self):
        energy_result = (float(self.carbonCalculator["Energy"]["Electricity"]) * 12 * 0.0005) + (
                    float(self.carbonCalculator["Energy"]["NaturalGas"]) * 12 * 0.0053) + (
                                    float(self.carbonCalculator["Energy"]["Fuel"]) * 12 * 2.32)
        waste_result = float(self.carbonCalculator["Waste"]["Waste_generated"]) * 12 * (
                    0.57 - (float(self.carbonCalculator["Waste"]["Waste_recycle"]) / 100))
        travel_result = float(self.carbonCalculator["Travel"]["Distance"]) * (
                    1 / float(self.carbonCalculator["Travel"]["Fuel_Efficiency"]) * 2.31)
        self.table.setItem(0, 1, QTableWidgetItem("%.2f" % energy_result))
        self.table.setItem(1, 1, QTableWidgetItem("%.2f" % waste_result))
        self.table.setItem(2, 1, QTableWidgetItem("%.2f" % travel_result))

        # table = QTableWidget(0, 2)

        # Create an icon and set it to a QTableWidgetItem
        icon1 = QIcon("positive-vote.png")
        icon2 = QIcon("negative-vote.png")
        item1 = QTableWidgetItem()
        item2 = QTableWidgetItem()
        item3 = QTableWidgetItem()
        # item1.setIcon(icon1)

        # Add the QTableWidgetItem to the table
        item1.setIcon(icon1)
        self.table.setItem(0, 2, item1)
        item2.setIcon(icon2)
        self.table.setItem(1, 2, item2)
        item3.setIcon(icon1)
        self.table.setItem(2, 2, item3)
        self.table.item(0, 1).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.table.item(1, 1).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.table.item(2, 1).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.table.item(0, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.item(1, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.item(2, 2).setTextAlignment(QtCore.Qt.AlignCenter)
        # msg_box = QMessageBox()
        # msg_box.setIcon(QMessageBox.Information)
        # msg_box.setWindowTitle("Information")
        # msg_box.setText("Under Development")
        # msg_box.exec_()

    def switchTab(self, index):
        self.tabs.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarbonFootprintCalculator()
    window.show()
    sys.exit(app.exec_())

