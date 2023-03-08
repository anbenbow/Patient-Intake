import zulu
import random


male_intake= "EVMY"
female_intake= "EVFX"
re_eval= "REEV"
blood_work='BWRK'
x_ray='XRAY'
mri='0MRI'
doppler='DPLR'
ultrasound='ULSD'
suture='SUTR'
observation='OBSV'

treatments=['Blood Work','X-Ray','MRI','Doppler','Ultrasound','Suture','Observation']

start= zulu.parse('2023-03-07T23:33:25.656261+00:00')
initial_eval= start.shift(minutes=15)

#print(start)
# print(initial_eval-start)

random_treatment= (random.choice(treatments))
random_treatment_two= (random.choice(treatments))
random_treatment_three= (random.choice(treatments))


print(random_treatment)
print(random_treatment_two)
print(random_treatment_three)

if random_treatment=='MRI':
    print(mri)
if random_treatment=='X-Ray':
    print(x_ray)
if random_treatment=='Blood Work':
    print(blood_work)
if random_treatment=='Doppler':
    print(doppler)
if random_treatment=='Ultrasound':
    print(ultrasound)
if random_treatment=='Suture':
    print(suture)
if random_treatment=='Observation':
    print(observation)

if random_treatment_two=='MRI':
    print(mri)
if random_treatment_two=='X-Ray':
    print(x_ray)
if random_treatment_two=='Blood Work':
    print(blood_work)
if random_treatment_two=='Doppler':
    print(doppler)
if random_treatment_two=='Ultrasound':
    print(ultrasound)
if random_treatment_two=='Suture':
    print(suture)
if random_treatment_two=='Observation':
    print(observation)

if random_treatment_three=='MRI':
    print(mri)
if random_treatment_three=='X-Ray':
    print(x_ray)
if random_treatment_three=='Blood Work':
    print(blood_work)
if random_treatment_three=='Doppler':
    print(doppler)
if random_treatment_three=='Ultrasound':
    print(ultrasound)
if random_treatment_three=='Suture':
    print(suture)
if random_treatment_three=='Observation':
    print(observation)


# if random_treatment=='MRI':
#     start.shift(hour=1)
# if random_treatment=='X-Ray':
#     start.shift(minute=45)
# if random_treatment=='Blood Work':
#     start.shift(minute=15)
# if random_treatment=='Doppler':
#     start.shift(minute=45)
# if random_treatment=='Ultrasound':
#     start.shift(hour=1)
# if random_treatment=='Suture':
#     start.shift(minute=30)
# if random_treatment=='Observation':
#     start.shift(hour=24)






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


#discharge_time= -start

# total_time= end-start
# print(total_time)
# print(end)