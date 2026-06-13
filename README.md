## 📸 Project Screenshots

Here are some screenshots showcasing the application in action:
<img width="959" height="463" alt="image" src="https://github.com/user-attachments/assets/1503cb52-beee-41e3-a895-beda1327de56" />
<img width="947" height="482" alt="image" src="https://github.com/user-attachments/assets/aef2b844-8dbe-40ee-886b-7b1a19d37671" />
<img width="959" height="485" alt="image" src="https://github.com/user-attachments/assets/cb509d4a-a25c-4ea9-96ed-db423d878c2a" />

<img width="883" height="447" alt="image" src="https://github.com/user-attachments/assets/30297ec0-6480-4096-9322-aebf7b639c41" />
<img width="872" height="431" alt="image" src="https://github.com/user-attachments/assets/70779cce-fb27-4812-a9e6-bae8576703fb" />
<img width="857" height="461" alt="image" src="https://github.com/user-attachments/assets/9ca91936-6b90-4e63-996f-9cf5c5654184" />
# IPL Stats & Data Analysis Website 🏏

This is a data analytics and interactive project designed to help cricket fans and analysts extract insights from Indian Premier League (IPL) matches. Users can quickly analyze team performance metrics, view player strike rates, and test their cricket knowledge with an optional quiz.

## 🚀 Key Features
- **Top 3 Player Analysis:** Calculates and highlights the strike rates of the top 3 highest-performing players across every franchise.
- **Dynamic Visual Analytics:** Uses Matplotlib/Seaborn to generate bar graphs charting match victory breakdowns.
- **Custom Input Processing:** Generates on-demand data frames based on real-time user parameters.
- **Interactive IPL Trivia Quiz:** Features an integrated, fully optional quiz module to test your comprehensive IPL history knowledge.

## 📁 Project Structure
The repository contains the following core files:
*   `iplpyfinalcode.py` — The primary Python backend script handling the logic, data processing, and user interaction.
*   `matches_rows.csv` — The core dataset containing granular match-by-match metrics and seasonal data.
*   `finaliplproject.xlsx` — The cleaned, processed structural database spreadsheet compiling all analytical data.
*   `IPL-Stats ppt.pptx` - The pptx cleaned and neat stuctered explaination of our project except thee graphs.

## 🛠️ Setup & Installation
To run this application locally on your computer, ensure you have Python installed, then follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/ARUNTHAMIZHAN18AURA/IPL-_STATS_AND_DATA..git
   ```
2. Navigate into the project folder:
   ```bash
   cd IPL-_STATS_AND_DATA.
   ```
3. Install required libraries:
   ```bash
   pip install pandas matplotlib openpyxl
   ```
4. Run the program:
   ```bash
   python iplpyfinalcode.py
   ```
   ---

## 📝 Notes & Troubleshooting

Before running the application, please keep the following important points in mind:

### 🛠 Prerequisites
* **Python 3.x:** Ensure you have Python 3 installed on your local machine. You can verify this by running `python --version` in your terminal.
* **Required Libraries:** If you encounter a `ModuleNotFoundError`, make sure you have successfully executed the installation command:
```bash
  pip install pandas matplotlib openpyxl
---

## ⚙️ Customization & Usage Guide

This project features a built-in **Strike Rate Calculator**. You can customize its inputs or logic inside `iplpyfinalcode.py` to analyze different match situations or player performances.

### 🏏 1. Calculate a Custom Player Strike Rate
To calculate the strike rate for a specific player scenario manually within the script, update the input variables:
```python
# Locate these variables to change the calculation inputs
runs_scored = 45  # Change to the number of runs
balls_faced = 25  # Change to the number of balls faced

# Formula used: (Runs / Balls) * 100
strike_rate = (runs_scored / balls_faced) * 100
