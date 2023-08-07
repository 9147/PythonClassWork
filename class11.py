'''
26 july 2023
'''

'''
 Create a table student with attributes USN, Student name, Branch, Semester, Courses code, enter atleast 5 tuples. Then 
 1) Print all the students who have registered for a particular course.
 2)Print the faculity handeling the courses in assending order.
'''

import sqlite3
con = sqlite3.connect("demo.db")
cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT(usn INTEGER PRIMARY KEY, name TEXT, branch TEXT, semester INTEGER, course_code TEXT)''')
con.commit()
con.close()

# Insert Values
conn = sqlite3.connect('demo.db')
c = conn.cursor()
c.execute('''INSERT INTO STUDENT VALUES(2,RAJ,IS,4,21IS43)''',(usn, name, branch, semester, course_code))
'''
CREATE TABLE 
'''



