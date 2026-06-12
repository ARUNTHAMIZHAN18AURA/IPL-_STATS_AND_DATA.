import pandas as pd
import numpy as np
import pandas as pd




name = input("Enter your name or nickname: ")

# Valid IPL teams list
valid_teams = ["RCB", "CSK", "MI", "GT", "PBKS", "SRH", "KKR", "LSG", "RR", "DC"]

# Loop until correct team name is entered
while True:
    fav_ipl_team = input("Enter your favorite IPL team (use CAPS only, no numbers): ")

    if fav_ipl_team in valid_teams:
        print(f"Congrats {name}! Your favorite team {fav_ipl_team} is one of the proud IPL franchises.")
        break  # Exit loop once correct team is entered
    else:
        print("Invalid team name. Choose only from RCB, CSK, MI, GT, PBKS, SRH, KKR, LSG, RR, DC.")
  # Exit loop once correct team is entered
# Checking condition
#for rcb fans and overview of rcb in this season
if fav_ipl_team == "RCB":
    print(f"🏆Congrats Royal Challengers Bengaluru🏆 , {name}'s favorite team of ipl {fav_ipl_team} achieved their long awaited glory in IPL 2026 with a season that captured the imagination of fans everywhere. Virat Kohli led with unmatched determination while Mohammed Siraj delivered fiery spells that broke opposition batting lineups. Every match reflected the spirit of Play Bold as RCB fought through challenges with resilience and unity. Their triumph in Chennai was more than a victory on the scoreboard, it was the fulfillment of a dream carried by millions of loyal supporters. RCB proved that belief and persistence can turn hope into history, and their championship run will forever shine as one of the greatest stories in the league.")

#for csk fans and overview of csk in this season 
if fav_ipl_team == "CSK" :
    print(f"🦁Chennai Super Kings🦁, {name}'s favorite team of IPL {fav_ipl_team}, continued their legacy of excellence with calm leadership and golden consistency. Guided by the wisdom of MS Dhoni, CSK blended experience and youth to dominate crucial moments. Their trademark “Whistle Podu” spirit echoed across stadiums as they turned pressure into opportunity. Every player contributed to the yellow brigade’s unstoppable rhythm, proving once again that CSK’s success is built on trust, teamwork, and timeless class.")
#for PBKS fans and overview of PBKS in this season
if fav_ipl_team == "PBKS" :
    print(f"🔥Punjab Kings🔥, {name}'s favorite team of IPL {fav_ipl_team}, played with heart and aggression that electrified fans. Shikhar Dhawan’s leadership brought calm to their fiery batting lineup, while their bowlers struck with precision. PBKS showed that passion and perseverance can turn every game into a spectacle. Their red spirit burned bright, inspiring fans to believe that Punjab’s roar will soon echo across the IPL podium.")
#for MI fans and overview of MI in this season 
if fav_ipl_team == "MI" :
    print(f"💙Mumbai Indians💙, {name}'s favorite team of IPL {fav_ipl_team}, showcased their champion DNA with fearless batting and tactical brilliance. Rohit Sharma’s leadership brought clarity and confidence, while their all‑rounders delivered match‑winning performances under pressure. MI’s blue wave swept through the season with precision and power, reminding everyone why they are one of the most decorated franchises in IPL history — a team that thrives when the stakes are highest.")
#for GT fans and overview of GT in this season 
if fav_ipl_team == "GT" :
    print(f"⚡Gujarat Titans⚡, {name}'s favorite team of IPL {fav_ipl_team}, embodied youthful energy and fearless cricket. Shubman Gill’s elegant stroke play and Rashid Khan’s magical spin made GT a team of flair and fight. Their journey was marked by bold decisions and thrilling finishes, proving that new teams can rise to greatness through belief and innovation. GT’s rise has redefined modern IPL cricket with style and substance.")
#for DC fans and overview of DC in this season
if fav_ipl_team == "DC" :
    print(f"🏛Delhi Capitals🏛️, {name}'s favorite team of IPL {fav_ipl_team}, showcased youthful energy and tactical sharpness. Rishabh Pant’s fearless captaincy and their dynamic lineup made DC a thrilling side to watch. Their blue flame burned bright with ambition, proving that Delhi’s rise is built on passion, preparation, and the hunger to conquer.")
#for RR fans and overview of RR in this season
if fav_ipl_team == "RR" :
    print(f"🏹Rajasthan Royals🏹, {name}'s favorite team of IPL {fav_ipl_team}, played with elegance and innovation. Sanju Samson’s leadership and Yashasvi Jaiswal’s fearless batting brought flair to every contest. RR’s pink pride stood for creativity and courage, reminding fans that cricket is as much art as competition. Their journey reflected the royal spirit of resilience and grace.")
#for LSG fans and overview of LSG in this season
if fav_ipl_team == "LSG" :
    print(f"💪Lucknow Super Giants💪, {name}'s favorite team of IPL {fav_ipl_team}, impressed with tactical brilliance and explosive talent. KL Rahul’s calm captaincy and their balanced squad made LSG a team that thrives under pressure. Their blue‑green energy symbolized fresh ambition and fearless cricket, marking them as one of the most promising forces in the league.")  
#for KKR fans and overview of KKR in this season
elif fav_ipl_team == "KKR" :
    print(f"🌀Kolkata Knight Riders🌀, {name}'s favorite team of IPL {fav_ipl_team}, brought flair and strategy together in perfect harmony. Under sharp leadership, KKR’s mix of youth and experience delivered thrilling performances. Their purple pride and “Korbo Lorbo Jeetbo” spirit made every match a spectacle of passion and belief. KKR’s journey reflected the power of unity and fearless ambition")
#for SRH fans and overview of SRH in this season
elif fav_ipl_team == "SRH":
    print(f"🌅Sunrisers Hyderabad🌅, {name}'s favorite team of IPL {fav_ipl_team}, combined explosive batting with disciplined bowling to light up the season. Travis Head’s fearless stroke play and Bhuvneshwar Kumar’s swing mastery made SRH a balanced powerhouse. Their orange army stood tall through every challenge, proving that consistency and courage define true contenders.")
# for the names except ipl teams or mistype and it runs like loop till they enter a proper franchise name (ipl team)
else:
    print(f" {name}Please Choose only from (RCB, CSK, MI, GT, PBKS, SRH, KKR, LSG, RR, DC)")
  
# Load tab-separated file
df = pd.read_csv("matches_rows.csv", sep="\t")

# Drop unwanted empty column
df = df.drop(columns=["Unnamed: 9"], errors="ignore")

# Force pandas to show everything in IDLE
pd.set_option("display.max_columns", None)   # show all columns
pd.set_option("display.max_rows", None)      # show all rows
pd.set_option("display.width", None)         # prevent wrapping
pd.set_option("display.max_colwidth", None)  # show full cell content

print(df)
print("If the data shows like no data or you find similar terms pls wait until our server loads the data, or you can share these missing data contact us on arunthamizhan18gmail.com")


# Column names aur unke exact data types define kiye hain (Tabular Layout)
# U10 = String (max 10 characters), f4 = Float number
dt = np.dtype([
    ('Team', 'U10'),
    ('Player_1', 'U25'), ('SR_1', 'f4'),
    ('Player_2', 'U25'), ('SR_2', 'f4'),
    ('Player_3', 'U25'), ('SR_3', 'f4')
])

print(f"{name}, the top 3 players strike rate of each team are showcased here; if u have interested for other players get the input for no. of balls played by them and runs in the total balls faced IF YOU WANT TO STOP PLS ENTER 1 IN THE INPUT")
records = [
    ("CSK", "Urvil Patel", 201.56, "Shivam Dube", 168.40, "Ruturaj Gaikwad", 154.20),
    ("RCB", "Rajat Patidar", 192.69, "Tim David", 188.27, "Virat Kohli", 144.71),
    ("MI", "Suryakumar Yadav", 167.91, "Ryan Rickelton", 150.97, "Rohit Sharma", 149.28),
    ("GT", "Jos Buttler", 163.03, "Sai Sudharsan", 156.17, "Shubman Gill", 155.87),
    ("PBKS", "Priyansh Arya", 211.62, "Shreyas Iyer", 175.07, "Prabhsimran Singh", 160.52),
    ("SRH", "Abhishek Sharma", 204.72, "Ishan Kishan", 182.42, "Heinrich Klaasen", 172.69),
    ("KKR", "Finn Allen", 214.11, "Sunil Narine", 174.50, "Ajinkya Rahane", 147.72),
    ("LSG", "Nicholas Pooran", 196.25, "Mitchell Marsh", 163.70, "Aiden Markram", 148.82),
    ("RR", "Vaibhav Sooryavanshi", 237.30, "Riyan Parag", 166.52, "Yashasvi Jaiswal", 159.71),
    ("DC", "K L Rahul", 149.72, "Abishek Porel", 142.40, "Tristan Stubbs", 138.98)
]

# NumPy Structured Tabular Array Create Karna
ipl_table = np.array(records, dtype=dt)

# Output in clean tabular format 
print(f"{'Team':<6} | {'Player 1':<20} {'SR 1':<6} | {'Player 2':<20} {'SR 2':<6} | {'Player 3':<20} {'SR 3':<6}")
print("-" * 95)
for row in ipl_table:
    print(f"{row['Team']:<6} | {row['Player_1']:<20} {row['SR_1']:<6.2f} | {row['Player_2']:<20} {row['SR_2']:<6.2f} | {row['Player_3']:<20} {row['SR_3']:<6.2f}")


ASD = input("if you want to know a specific players strike rate get the data and give it in the input after this or use this if you want for your customized. If you want to skip type 3, if you want to proceed press any other key: ")
if ASD != "3":   
    while True:
        # Ask user for runs and balls safely
        try:
            runs = int(input("Enter runs scored: "))
            balls = int(input("Enter balls faced: "))

            if balls <= 0 or runs < 0:
                print("Invalid input. Runs must be >= 0 and balls must be > 0.")
                continue

            # Calculate strike rate
            strike_rate = (runs / balls) * 100
            print(f"Strike Rate = {strike_rate:.2f}")
            print("🔥 That's a power-hitter's strike rate! You'd be opening in the IPL!")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Exit condition
        choice = input("Type 1 to stop, or press Enter to continue: ")
        if choice == "1":
            print("Program stopped.")
            break



import matplotlib.pyplot as plt

# IPL 2026 League Stage Data (Accurate)
teams = ["RCB","GT","SRH","RR","KKR","CSK","DC","LSG","PBKS","MI"]
wins = [9,9,9,8,7,7,7,7,5,4]
runs = [675,732,624,776,488,430,402,460,354,417]
wickets = [28,29,17,25,21,21,16,14,24,20]

# --- Wins Chart ---
plt.figure(figsize=(10,6), facecolor=(0.95,0.95,0.95))
plt.bar(teams, wins, color="orange", edgecolor="black")
for i, v in enumerate(wins):
    plt.text(i, v+0.2, str(v), ha="center", fontweight="bold")
plt.title("IPL 2026 - Wins per Team", fontsize=14, fontweight="bold")
plt.xlabel("Teams"); plt.ylabel("Wins")
plt.ylim(0, 11); plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# --- Runs Chart ---
plt.figure(figsize=(10,6), facecolor=(0.95,0.95,0.95))
plt.bar(teams, runs, color="blue", edgecolor="black")
for i, v in enumerate(runs):
    plt.text(i, v+10, str(v), ha="center", fontweight="bold")
plt.title("IPL 2026 - Top Run Scorer Runs per Team", fontsize=14, fontweight="bold")
plt.xlabel("Teams"); plt.ylabel("Runs")
plt.grid(axis="y", linestyle="--", alpha=0.5)
teams = ["RCB","GT","SRH","RR","KKR","CSK","DC","LSG","PBKS","MI"]
runs = [675,732,624,776,488,430,402,460,354,417]
strike_rate = [142.3,148.5,156.7,152.8,145.2,138.4,162.1,134.7,141.6,139.5]

plt.figure(figsize=(10,6), facecolor=(0.95,0.95,0.95))
plt.scatter(runs, strike_rate, color="blue", s=100, edgecolor="black")

# Annotate each point with team name
for i, team in enumerate(teams):
    plt.text(runs[i]+5, strike_rate[i], team, fontsize=9, fontweight="bold")

plt.title("IPL 2026 - Runs vs Strike Rate (Top Players)", fontsize=14, fontweight="bold")
plt.xlabel("Runs Scored")
plt.ylabel("Strike Rate")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

        
      

import random
import time

scores = []


# IPL Trivia Questions
questions = [
    ("Which team won IPL 2026?",
     ["CSK","RCB","GT","KKR","SRH"],
     1),  # RCB

    ("Who won the Orange Cap in IPL 2026?",
     ["Virat Kohli","Vaibhav Sooryavanshi","Shubman Gill","Heinrich Klaasen"],
     1),  # Vaibhav Sooryavanshi

    ("Who won the Purple Cap in IPL 2026?",
     ["Harshal Patel","Pat Cummins","Kagiso Rabada","Mohammed Siraj"],
     2),  # Kagiso Rabada

    ("Which team had the most wins in the league stage?",
     ["RCB","GT","SRH","RR","KKR"],
     0),  # RCB (9 wins, tied with GT & SRH but RCB champion)

    ("Which player scored 675 runs for RCB?",
     ["Virat Kohli","Faf du Plessis","Rajat Patidar","Glenn Maxwell"],
     0),  # Virat Kohli

    ("Which Rajasthan Royals player scored 776 runs?",
     ["Sanju Samson","Yashasvi Jaiswal","Vaibhav Sooryavanshi","Riyan Parag"],
     2),  # Vaibhav Sooryavanshi

    ("Which Gujarat Titans bowler took 29 wickets?",
     ["Mohammed Shami","Rashid Khan","Kagiso Rabada","Alzarri Joseph"],
     2),  # Kagiso Rabada

    ("Which Delhi Capitals batter had a strike rate of 162.1?",
     ["Rishabh Pant","Jake Fraser-McGurk","David Warner","Tristan Stubbs"],
     1),  # Jake Fraser-McGurk

    ("Which Punjab Kings bowler took 24 wickets?",
     ["Arshdeep Singh","Harshal Patel","Sam Curran","Kagiso Rabada"],
     1),  # Harshal Patel

    ("Which Mumbai Indians bowler took 20 wickets?",
     ["Jasprit Bumrah","Piyush Chawla","Hardik Pandya","Jason Behrendorff"],
     0)   # Jasprit Bumrah
]

def display_ques(no, ques, option):
    print(f"\nQ{no}. {ques}")
    for i, o in enumerate(option, 1):
        print(f"{i}. {o}")

def validate(no):
    while True:
        a = input("Answer: ").strip()
        if a.isdigit() and 1 <= int(a) <= no:
            return int(a) - 1
        print(f"Invalid Input. Please enter a number between 1 and {no}.")

def result(sc, tot, wrong):
    pct = round((sc/tot)*100)
    if pct >= 80:
        g = "Excellent/ Outstanding"
    elif pct >= 60:
        g = "Good"
    else:
        g = "Keep Trying"

    print(f"\n--- Final Result ---")
    print(f"{sc}/{tot} ({pct}%) - {g}")

    if wrong:
        print("Questions to Review:")
        for q in wrong:
            print(f"- {q}")
    return pct

def run_quiz():
    score = 0
    wr = []
    print(f"\n{'IPL 2026 Trivia Quiz':^50}")
    random.shuffle(questions)
    for i, (ques, option, ans) in enumerate(questions, 1):
        display_ques(i, ques, option)
        a = validate(len(option))
        if a == ans:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {option[ans]}")
            wr.append(ques)

    pct = result(score, len(questions), wr)
    scores.append((name, pct))
    print(f"{'Thank you for playing!':^50}")

play = input("Excited to play? y/n: ")
while play.lower() == "y":
    start = time.time()
    run_quiz()
    print(f"\nTotal time taken: {time.time() - start:.1f}s")

    sorted_scores = sorted(scores, key=lambda x: -x[1])
    print("\nLeaderboard:", sorted_scores)

    play = input("\nPlay again? y/n: ")
