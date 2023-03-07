import zulu
import random


male_treatment= "EVMY"
female_treatment= "EVFX"
re_eval= "REEV"

treatments=['Blood Work','X-Ray','MRI','Doppler','Ultrasound','Suture']

start= zulu.parse('2023-03-07T23:33:25.656261+00:00')
initial_eval= start.shift(minutes=15)
#print(start)
print(initial_eval-start)

Patient_0001={
'Name': 'Jon Snow',
'Gender': 'M'
}
Patient_0002={
'Name': 'Bran Stark',
'Gender': 'M'
}
Patient_0003={
'Name': 'Daenerys Targaryen',
'Gender': 'F'
}
Patient_0004={
'Name': 'Cersei Lannister',
'Gender': 'F'
}
Patient_0005={
'Name': 'Joffrey Baratheon',
'Gender': 'M'
}
# print(Patient_0001['Name'])
# print(Patient_0001['Gender'])


# end= zulu.now() 

# total_time= end-start
# print(total_time)
# print(end)