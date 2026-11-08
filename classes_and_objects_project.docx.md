# **מיני פרויקט: ספרייה קטנה**

**איזו מערכת בונים:** מערכת קטנה לספרייה. בספרייה יש ספרים, ולכל ספר כמה עותקים. קוראים משאילים עותקים ומחזירים אותם, והמערכת יודעת בכל רגע כמה עותקים פנויים מכל ספר — וכמה ספרים יש בספרייה בסך הכול.

**מה תלמדו מהפרויקט:**

• לבנות Class שלמה מאפס: \_\_init\_\_, מתודות ו-\_\_str\_\_

• לבדוק ערכים כבר ביצירה, ולזרוק שגיאה כשהם לא חוקיים

• להבחין בין Setter שמשנה את המצב לבין Getter שרק מחזיר מידע

• להשתמש ב-Class Attribute כמונה משותף לכל האובייקטים

**מה צריך לבנות — שלב אחרי שלב:**

**שלב 1 — ה-Class והמונה המשותף.** כתבו Class בשם Book, עם Class Attribute בשם total\_books שמתחיל ב-0. הוא יספור כמה ספרים נוצרו.

**שלב 2 — יצירת ספר.** ה-\_\_init\_\_ מקבל שם, סופר ומספר עותקים, ושומר אותם. בהתחלה כל העותקים פנויים — שומרים אותם גם ב-available. כל ספר חדש מגדיל את total\_books ב-1. אם מספר העותקים קטן מ-1 — זורקים ValueError, ולא יוצרים ספר.

**שלב 3 — השאלה והחזרה (Setters).**

• borrow — מורידה עותק פנוי אחד. אם אין עותקים פנויים: ValueError.

• return\_book — מחזירה עותק אחד. אם כל העותקים כבר בספרייה: ValueError.

**שלב 4 — בדיקה (Getter).** is\_available מחזירה True אם יש לפחות עותק פנוי אחד, אחרת False.

**שלב 5 — הצגה.** \_\_str\_\_ מחזירה שם, סופר וכמה עותקים פנויים מתוך כמה, כמו בפלט.

**הודעות השגיאה — בדיוק כך:**

| copies must be at least 1 no copies available all copies are already in |
| :---- |

**קוד לבדיקה:**

| books \= \[     Book("Clean Code", "Martin", 3),     Book("Python Basics", "Cohen", 1), \]   books\[0\].borrow() books\[1\].borrow()   try:     books\[1\].borrow() except ValueError as error:     print("Python Basics \-\>", error)   try:     Book("Empty", "Nobody", 0\) except ValueError as error:     print("Empty \-\>", error)   for book in books:     print(book, "\| available:", book.is\_available())   print("Books in the library:", Book.total\_books) |
| :---- |

**הפלט הרצוי:**

| Python Basics \-\> no copies available Empty \-\> copies must be at least 1 Clean Code by Martin (2/3 available) \| available: True Python Basics by Cohen (0/1 available) \| available: False Books in the library: 2 |
| :---- |

**בסוף הפרויקט תדעו:**

• לתרגם תיאור של "דבר" בעולם — ספר — ל-Class עם נתונים ופעולות

• לשמור על כללים בתוך האובייקט, כך שאי אפשר להגיע למצב לא חוקי

• להבין למה הספר Empty לא נספר במונה: השגיאה נזרקה לפני ההגדלה

**בונוס:** הוסיפו Class בשם Library שמחזיקה רשימת ספרים, עם add\_book שמוסיפה ספר, ו-available\_books שמחזירה רק את הספרים שאפשר להשאיל עכשיו.