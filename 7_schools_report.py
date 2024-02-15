"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the AAC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""


import json

infile = open('school_data.json', 'r')

list_of_schools = json.load(infile)

#print(type(list_of_schools))

aac = []
big_12 = []
big_10 = []
sec = []
interested_schools = []
list_of_conferences = [372, 108, 107, 130]

'''
#Alternate Code to create and print conference specific lists

for i in list_of_schools:
    conference = i["NCAA"]["NAIA conference number football (IC2020)"]

    if conference == 372:
        aac.append(i["instnm"])
        interested_schools.append(i)
    elif conference == 108:
        big_12.append(i["instnm"])
        interested_schools.append(i)
    elif conference == 107:
        big_10.append(i["instnm"])
        interested_schools.append(i)
    elif conference == 130:
        sec.append(i["instnm"])
        interested_schools.append(i)
    else:
        next

print("Schools in AAC:")
for n in aac:
    print(n)
print(f'\n')

print("Schools in Big 12:")
for n in big_12:
    print(n)
print(f'\n')

print("Schools in Big 10:")
for n in big_10:
    print(n)
print(f'\n')

print("Schools in SEC:")
for n in sec:
    print(n)
print(f'\n')

'''

for i in list_of_schools:
    conference = i["NCAA"]["NAIA conference number football (IC2020)"]

    if conference in list_of_conferences:
        interested_schools.append(i)
    else:
        next

for i in interested_schools:
    women_grad_rate = i["Graduation rate  women (DRVGR2020)"]
    if women_grad_rate >= 75:
        print(f'University: {i["instnm"]}')
        print(f'Graduation Rate for Women: {women_grad_rate}%')
        print(f'\n')

for i in interested_schools:
    cost_of_attendance = i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
    if cost_of_attendance == None:
        next
    elif cost_of_attendance >= 50000:
        print(f'University: {i["instnm"]}')
        print(f'Total Price for In-State Students Living Off Campus: ${cost_of_attendance:,.2f}')
        print(f'\n')