''''
    Store the following information in a dictionary:
    Course code: course Name,faculty,Number of registerations
    Perform the following operations using functions
    a.Find Course Name that has highest number of registration
    b.Given the Ciurse Code, Display the associated details
    Display details of all courses.
'''

def find_highest(detail):
    li=[[detail[a][2], detail[a][0]] for a in detail]
    val=li[0]
    for a in li[1:]:
        if val[0]<a[0]:
            val=a
    return val[1]

def find_course(details,course):
    val=details.get(course,0)
    if val==0:
        return "NO such course Found"
    return val

course_details={"MAT134":["Math","Jayesh",13],"DSA132":["DSA","Thapa",15],"PYT34":["Python","Abhishek",30],"SED32":["SED","Maggie",86]}

print("Available courses are: ",course_details)
print("Highest registered courese is: ",find_highest(course_details))
course=input("enter course code: ")
print(find_course(course_details,course))


