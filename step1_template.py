"""
Data Science Project - Step 1: Research Question & Dataset
============================================================

Due: Sunday, April 5
Points: 25

In this step, you will:
1. Choose a dataset that interests you
2. Formulate a clear research question
3. Explore your data (no coding required!)
4. Plan your analysis approach

NO PYTHON CODE REQUIRED FOR THIS STEP!
Open your dataset in Excel, Google Sheets, or any spreadsheet app to explore it.
You'll load it with Python in Step 2.

Submit this file with your answers filled in.
"""


# ============================================================
# PART 1: YOUR DATASET (5 points)
# ============================================================

# Answer these questions about your chosen dataset:

# 1. What dataset did you choose?
dataset_name = """
YOUR ANSWER HERE: "MLB Stats 1901 - 2025"
"""

# 2. Where did you get it? (Include URL if online)
dataset_source = """
YOUR ANSWER HERE: "https://www.kaggle.com/datasets/diazk2/mlb-statistics-1901-present"
"""

# 3. Why did you choose this dataset?
why_this_dataset = """
YOUR ANSWER HERE: "I'm interested in baseball statistics and I want to analyze team performance over time."
"""


# ============================================================
# PART 2: EXPLORE YOUR DATA (no code needed!) (5 points)
# ============================================================

# Open your CSV file in Excel, Google Sheets, or any spreadsheet program.
# Answer these questions by looking at the data:

# 4. How many rows (records) are in your dataset?
num_rows = """
YOUR ANSWER HERE: "2690 rows"
"""

# 5. How many columns are there?
num_columns = """
YOUR ANSWER HERE: "16 columns"
"""

# 6. List ALL the column names:
column_names = """
YOUR ANSWER HERE: "
1. team_name
2. year
3. wins
4. losses
5. winning_percentage
6. games_behind
7. wild_card_games_behind
8. record_in_the_last_10_games
9. current_streak
10. runs_scored
11. runs_allowed
12. run_differential
13. expected_win_loss_record
14. record_at_home
15. record_when_away
16. record_against_top_50_percent"

"""

# 7. For each column, what type of data does it contain?
#    - Text (words, names, categories)
#    - Numbers (counts, measurements, scores)
#    - Dates
#    - Yes/No (true/false)
column_types = """
YOUR ANSWER HERE: "
- team_name: Text (name of the baseball team)
- year: Number (season year)
- wins: Number (total wins in the season)
- losses: Number (total losses in the season)
- winning_percentage: Number (wins divided by total games)
- games_behind: Number (how many games behind the leader)
- wild_card_games_behind: Number (how many games behind the wild card spot)
- record_in_the_last_10_games: Text (e.g., '6-4'
- current_streak: Text (e.g., 'W3' for 3 wins in a row)
- runs_scored: Number (total runs scored in the season)
- runs_allowed: Number (total runs allowed in the season)
- run_differential: Number (runs scored minus runs allowed)
- expected_win_loss_record: Text (e.g., '80-82' based on runs)
- record_at_home: Text (e.g., '40-41' wins-losses at home)
- record_when_away: Text (e.g., '40-41' wins-losses away)
- record_against_top_50_percent: Text (e.g., '30-30' wins-losses against top half of teams)"

"""


# ============================================================
# PART 3: YOUR RESEARCH QUESTION (10 points)
# ============================================================

# A good research question is:
#   - Specific (not too broad)
#   - Answerable with your data (the columns you need exist!)
#   - Interesting to you
#
# BAD:  "Is this data interesting?" (too vague)
# BAD:  "What causes restaurant violations?" (can't prove causation)
# GOOD: "Do restaurants in Manhattan receive more violations than other boroughs?"
# GOOD: "Which cuisine types have the highest average inspection scores?"

# 8. What is your research question?
research_question = """
YOUR ANSWER HERE: "How has the average winning percentage of MLB teams changed over time?"

"""

# 9. Why is this question interesting or important?
why_interesting = """
YOUR ANSWER HERE: "I'm curious about trends in baseball performance and whether teams are getting more competitive over time."

"""

# 10. What do you predict the answer will be? (Your hypothesis)
#     It's okay to be wrong! This is just your initial guess.
hypothesis = """
YOUR ANSWER HERE: "I predict that the average winning percentage will have increased over time due to improvements in training, analytics, and player development."

"""


# ============================================================
# PART 4: PLANNING YOUR ANALYSIS (5 points)
# ============================================================

# 11. Which columns will you need to answer your question?
#     List the specific column names from your dataset.
key_columns = """
YOUR ANSWER HERE: "
- year (to track changes over time)
- winning_percentage (to measure team performance)"

"""

# 12. What challenges do you anticipate?
#     Think about: missing data, confusing values, things you'd need to clean up
anticipated_challenges = """
YOUR ANSWER HERE: "MLB Lockouts, Shortened seasons, and Protesting/Strikes may cause some seasons to have fewer games, which could affect winning percentages. I'll need to decide how to handle those seasons in my analysis."

"""

# 13. What type of analysis will you do?
#     Check all that apply:
analysis_plan = """
YOUR ANSWER HERE (check all that apply):

[ X ] Compare averages between groups (e.g., avg score by borough)
[ ] Count/percentage by category (e.g., % of each grade)
[ ] Look for relationships between two numbers (e.g., price vs rating)
[ X ] Track changes over time (e.g., violations by year)
[ ] Other: _______________
"""


# ============================================================
# SUBMISSION CHECKLIST
# ============================================================

"""
Before submitting, verify:

[ X ] I found a dataset with at least 100 rows and 5 columns
[ X ] I can open my dataset in a spreadsheet program
[ X ] I listed all column names and their types
[ X ] My research question is specific and answerable with this data
[ X ] I identified which columns I'll need for my analysis
[ X ] I saved my dataset file (you'll submit it with Step 2)

SUBMIT: Just this file (step1_template.py with your answers)
        Keep your dataset ready for Step 2!
"""
