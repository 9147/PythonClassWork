# print("insert into staff")
# print("values(1,'Amit','Belgaum','Testing',5000);")
a='''5000
9000
10000
6000
8000
5000
5000
9000
10000
12000
9000'''
li1=['Amit', 'Dilip', 'Abhishek', 'Rohan', 'Ramesh', 'Prashant', 'Ravi', 'Akshata', 'Raghu', 'Kumar', 'Dimple']
li2=['Belgaum', 'belgaum', 'Nagpur', 'Belgaum', 'Gokak', 'Bagalkot', 'Belgaum', 'Dharwad', 'Hubli', 'Banglore', 'Nippani']
li3=['Testing', 'Design', 'Testing', 'Production', 'Testing', 'Design', 'Production', 'Design', 'Design', 'Production', 'Production']
li4=[5000, 9000, 10000, 6000, 8000, 5000, 5000, 9000, 10000, 12000, 9000]
for i in range(1,len(li1)+1):
    print("insert into staff")
    print(f'values({i},\'{li1[i-1]}\',\'{li2[i-1]}\',\'{li3[i-1]}\',{li4[i-1]});')