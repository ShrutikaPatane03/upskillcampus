import sqlite3

conn = sqlite3.connect("quiz.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
score INTEGER,
percentage REAL
)
""")

conn.commit()
conn.close()

print("Database Created")
[
{
"question":"What is the capital of India?",
"options":["Mumbai","Delhi","Pune","Chennai"],
"answer":"Delhi"
},
{
"question":"Which language is used for AI?",
"options":["Python","HTML","CSS","PHP"],
"answer":"Python"
},
{
"question":"2 + 5 = ?",
"options":["6","7","8","9"],
"answer":"7"
},
{
"question":"Which planet is known as the Red Planet?",
"options":["Earth","Mars","Jupiter","Venus"],
"answer":"Mars"
},
{
"question":"CPU stands for?",
"options":[
"Central Processing Unit",
"Computer Power Unit",
"Control Program Unit",
"Central Program Unit"
],
"answer":"Central Processing Unit"
}
]
tk
sqlite3
