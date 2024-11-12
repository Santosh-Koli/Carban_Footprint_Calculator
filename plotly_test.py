import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class PlotlySubplotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.setWindowTitle("Plotly Bar Plots in PyQt5")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a 1x2 grid of subplots
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Bar Plot 1", "Bar Plot 2"))

        # Print the grid layout to confirm valid indices
        fig.print_grid()

        # Add bar plots to the subplots
        fig.add_trace(
            go.Bar(x=['A', 'B', 'C', 'D'], y=[10, 15, 13, 17], name='Bar Plot 1'),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=['E', 'F', 'G', 'H'], y=[5, 10, 15, 20], name='Bar Plot 2'),
            row=1, col=2
        )

        # Update the layout for better visualization
        fig.update_layout(title_text="Two Bar Plots Example", showlegend=True)

        # Render the plot as HTML
        plot_html = fig.to_html(full_html=False)

        # Create a QWebEngineView widget and set the HTML content
        web_view = QWebEngineView()
        web_view.setHtml(plot_html)

        # Add the web view to the layout
        self.layout.addWidget(web_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PlotlySubplotApp()
    main_window.show()
    sys.exit(app.exec_())
