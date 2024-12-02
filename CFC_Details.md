## Carbon Footprint Calculator 🌍🌱 :-

*A Python-based interactive application to calculate and visualize your carbon footprint. This tool provides insights into energy consumption, waste generation, and travel habits, and compares them with regional and global averages. Users can also download detailed reports in PDF format, view dynamic visualizations, and track their progress over time.*


----------------------------------------------------------------------------------------------------------------------------

## Features 🌟:- 

1. Interactive Dashboard:
   
- *Track energy consumption, waste, and travel habits.*
- *View detailed breakdowns of carbon emissions.*

3. User-Friendly Interface:
   
- *Clean, modern, and intuitive design.*
- *Registration and login system for personalized tracking.*

5. Dynamic Calculations:
   
- *Calculate carbon footprint for individual or enterprise users.*
- *View per capita emissions and compare with European averages.*

7. Data Visualization:
   
- *Dynamic charts for comparing emissions.*
- *Visualize the distribution of emissions from energy, waste, and travel.*

9. Yearly Comparisons:
    
- *Compare carbon footprint data year-over-year.*
- *Track progress and identify trends over time.*

11. PDF Reporting:
    
- *Generate downloadable reports with visual graphs and feedback.*

13. Admin Features:
    
- *Access to all user data and analytics.*
- *Ability to compare emissions across companies and years.*

  

----------------------------------------------------------------------------------------------------------------------------

## File Structure 📁 :- 

```bash

CARBON_FOOTPRINT_CALCULATOR/
├── __pycache__/                                      # Compiled Python bytecode
├── .idea/                                            # IDE project settings (if using PyCharm or similar)
├── carbonFootprint/                                  # Main module for carbon footprint calculations
│   └── carbon_footprint.py                           # Core logic for calculations and backend processes
├── images/                                           # Images and UI assets
│   ├── carbonfootprint_login.png
│   └── carbon_footprint_background.png
├── Learning_Testing/                                 # For test scripts or learning modules
│   └── (test files here)                             # Placeholder for testing resources
├── loginUi/                                          # Login and UI management
│   └── Ui_Form.py                                    # Handles user interface logic for login/registration
├── myvenv/                                           # Virtual environment for project dependencies
├── Carbon Footprint Calculator-Concept-Design.docx   # Documentation or design notes
├── CFC_Details.md                                    # Markdown file for additional project details
├── LICENSE                                           # License file for the project
├── requirements.txt                                  # List of Python dependencies


```


-----------------------------------------------------------------------------------------------------------------------------

## Installation and Setup 🛠️ : -

1. Prerequisites
   
- *Python 3.8 or above*
- *pip (Python package manager)*
- *MySQL database (create your own database, can refer excel sheet to create a table)*
- *ChromeDriver (if enabling Selenium functionalities)*

2. Steps

- *Clone the Repository:-*

```bash

  git clone https://github.com/your-username/Carbon-Footprint-Calculator.git
  cd Carbon-Footprint-Calculator

```

- *Set Up the Environment Create a virtual environment and activate it:-*

```bash

python -m venv venv
source venv/bin/activate  # For Linux/macOS
myvenv\Scripts\activate     # For Windows

```

- *Install Dependencies Use the requirements.txt file to install the necessary libraries:-*

```bash

pip install -r requirements.txt

```

- *Set Up the Database:-*


- *Run the Application:-*

```bash

python ui_form.py

```

- *Admin Access (Optional):-*

```bash

Use admin credentials to access admin tools and analytics. (Currently admin access is restricted to single user_admin) 
```


----------------------------------------------------------------------------------------------------------------------------

## Technologies Used 💻 :-

- *Programming Language: Python 3.8+*
- *Framework: PyQt5 (for the GUI)*
- *Database: MySQL (with pymysql and MySQLdb for connections)*
- *Visualization: Plotly and PyQt WebEngine*
- *PDF Generation: ReportLab*
- *Additional Tools: Selenium (for web data retrieval)*
  

----------------------------------------------------------------------------------------------------------------------------

## Features Breakdown 🚶‍♂️💡 :- 

1. Login & Registration
   
- *Secure login system with password validation.*
- *User role-based access (Admin/User).*

2. Dynamic Tabs

- *Tabs for energy, waste, travel inputs, and results visualization.*
- *Validation for user inputs (e.g., numeric-only fields).*
  
4. Visual Analytics

- *Bar and pie charts for carbon footprint comparison.*
- *Yearly comparisons and energy-waste-travel distributions.*
  
5. Admin Panel

- *Tools to compare companies' emissions.*
- *Filters for years and user types.*

6. Reporting

- *Generate PDF reports with detailed graphs and recommendations.*
  

----------------------------------------------------------------------------------------------------------------------------

## Contributing 🤝 :- 

**We welcome contributions! To get started:**

*Fork the repository.*
*Create a feature branch.*
*Commit your changes.*
*Submit a pull request.*

----------------------------------------------------------------------------------------------------------------------------

## License 📄 :-

*This project is licensed under the MIT License. See the "LICENSE" file for details.*

----------------------------------------------------------------------------------------------------------------------------

*Let's work together to create a sustainable future!* 🌿

----------------------------------------------------------------------------------------------------------------------------

