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
*   `ipl_2024_wins_barchart.png` — An exported data visualization chart detailing the win distributions for the 2024 season.

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
