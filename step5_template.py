"""
Data Science Project - Step 5: Poster & Conclusions
====================================================

POSTER DUE: Wednesday, April 30 (last class) - 20 points
REFLECTION DUE: After your presentation (Finals Week) - 5 points

The poster pulls your entire project together in one visual document.
You'll present it during the poster session on 4/30, get feedback,
then use it for your oral presentation during finals week.
"""


# ============================================================
# PART 1: CONCLUSIONS (10 points)
# ============================================================

# Summarize your entire project. This text will go on your poster.

project_title = """
YOUR TITLE HERE: "123 years of MLB: How Has Winning Percentage changed since 1901?
"""

research_question = """
YOUR RESEARCH QUESTION (from Step 1): "How has the average winning percentage of MLB teams changed over time?"

"""

key_findings = """
YOUR KEY FINDINGS (3-4 bullet points with specific numbers):
"- Notable differences exist
between franchise: the Yankees
averaged 0.570 while the Phillies
averaged 0.467. A gap of 0.10
across 123 seasons.
- Overall average winning
percentage went from 0.526 in
1901 to 0.536 in 2024, a change
of only 0.01 over 123 years.
- Pearson correlation between
Year and winning percentage are
weakly correlated  (r =0.065, p =
0.027)
- Though a pattern of (r =0.947, p
=0.0) confirms a strong
correlation between winning
percentage and run differential"
"""

answer_to_question = """
YOUR ANSWER (2-3 sentences directly answering your research question):
The average winning percentage of MLB teams has not meaningfully changed over 123 years(r = 0.065, p = 0.027). 
Despite major shifts in the sport including professionalization,expansion, the steroid era, and modern analytics, winning percentage has remained close to0.500 across all franchises from 1901 to 2024. 
My hypothesis was not supported: improvement in one franchise comes at another's expense in baseball.
"""

limitations = """
LIMITATIONS OF YOUR ANALYSIS:
Winning percentage alone may not fully capture team improvement such as factors like league competition level, schedule strength, and roster payroll are not accounted for in this analysis.
"""


# ============================================================
# PART 2: CREATE YOUR POSTER (10 points)
# ============================================================

"""
YOUR POSTER SHOULD INCLUDE:

1. TITLE SECTION
   - Project title (large, clear)
   - Your name
   - CSCI 120, Spring 2026

2. INTRODUCTION (2-3 sentences)
   - What question did you explore?
   - Why is it interesting?

3. DATA (brief)
   - Source and size
   - Key variables used

4. KEY VISUALIZATIONS (2-3 of your best charts)
   - Include the PNG files from Step 4
   - Add brief captions

5. FINDINGS (bullet points)
   - Your 3-4 key findings with numbers

6. CONCLUSION (2-3 sentences)
   - Answer to your question
   - Main takeaway

POSTER SPECS:
- Format: PowerPoint, Google Slides, or Canva
- Size: Letter (8.5x11) or tabloid (11x17)
- Save as: poster.pdf
- Bring printed copy to class on 4/30

POSTER TIPS:
- Less text, more visuals
- Font size: Title 36+, headers 24+, body 18+
- Use your chart colors consistently
- Leave white space - don't cram everything in
"""

# Use this to plan your poster layout:
poster_layout = """
+------------------------------------------+
|              PROJECT TITLE               |
|            Your Name | CSCI 120          |
+------------------------------------------+
|                    |                     |
|   INTRODUCTION     |    CHART 1          |
|   (why this        |    (your best       |
|    matters)        |     visualization)  |
|                    |                     |
+--------------------+---------------------+
|                    |                     |
|   CHART 2          |    CHART 3          |
|                    |    (optional)       |
|                    |                     |
+--------------------+---------------------+
|                                          |
|   KEY FINDINGS          CONCLUSION       |
|   - Finding 1           (answer to       |
|   - Finding 2            your question)  |
|   - Finding 3                            |
|                                          |
+------------------------------------------+
"""


# ============================================================
# PART 3: REFLECTION (5 points) - Due same day as presentation
# ============================================================

"""
Complete this RIGHT AFTER your presentation while it's fresh.
Three quick questions - just a few sentences each.
"""

# 1. What went well?
what_went_well = """
The data turned out to be genuinely interesting to work with. I didn't expect that winning percentage would be so stable across 123 years.
"""

# 2. What was tough?
what_was_tough = """
The trickiest part was dealing with missing packages. When matplotlib and scipy weren't installed, I had to figure out how to install them through the terminal with pip.
"""

# 3. What would you tell next semester's students?
advice_for_future = """
Pick a dataset you're actually curious about and don't panic when you get errors.
"""


# ============================================================
# SUBMISSION CHECKLIST
# ============================================================

"""
WEDNESDAY 4/30 (Poster Session):
[ x ] Poster saved as poster.pdf
[ x ] Printed copy brought to class
[ x ] Conclusions section completed above
[ x ] Ready to explain your project in 2-3 minutes

FINALS WEEK (After Presentation):
[ x ] Reflection completed (above or as reflection.md)
[ x ] All project files organized in folder

FINAL SUBMISSION STRUCTURE:
YourName_DataProject/
    step1_question.py
    step2_cleaning.py
    step3_analysis.py
    step4_visualization.py
    step5_conclusions.py  ← this file
    data/
        your_dataset.csv
    outputs/
        cleaned_data.csv
        chart1.png
        chart2.png
        chart3.png
    poster.pdf
    reflection.md
"""
