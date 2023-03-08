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
print("Patient Name: "+Patient_0001['Name'])

intake_time= zulu.parse('2023-03-07T23:33:25.656261+00:00')
print("Action: Intake")
print(intake_time)
start= intake_time.shift(hours=0,minutes=15)
print("Action: Evaluation")

if Patient_0001['Gender']=='F':
    print(female_intake)
if Patient_0001['Gender']=='M':
    print(male_intake)    

print(start)


random_treatment= (random.choice(treatments))
random_treatment_two= (random.choice(treatments))
random_treatment_three= (random.choice(treatments))

print("Action: Treatment")

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


if random_treatment=='MRI':
    time_after_first_treatment= start.shift(hours=1)
if random_treatment=='X-Ray':
    time_after_first_treatment= start.shift(minutes=45)
if random_treatment=='Blood Work':
    time_after_first_treatment= start.shift(minutes=15)
if random_treatment=='Doppler':
    time_after_first_treatment= start.shift(minutes=45)
if random_treatment=='Ultrasound':
    time_after_first_treatment= start.shift(hours=1)
if random_treatment=='Suture':
    time_after_first_treatment= start.shift(minutes=30)
if random_treatment=='Observation':
    time_after_first_treatment= start.shift(hours=24)

print(time_after_first_treatment)

print("Action: Treatment")

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


if random_treatment_two=='MRI':
    time_after_second_treatment=time_after_first_treatment.shift(hours=1)
if random_treatment_two=='X-Ray':
    time_after_second_treatment= time_after_first_treatment.shift(minutes=45)
if random_treatment_two=='Blood Work':
    time_after_second_treatment= time_after_first_treatment.shift(minutes=15)
if random_treatment_two=='Doppler':
    time_after_second_treatment= time_after_first_treatment.shift(minutes=45)
if random_treatment_two=='Ultrasound':
    time_after_second_treatment= time_after_first_treatment.shift(hours=1)
if random_treatment_two=='Suture':
    time_after_second_treatment= time_after_first_treatment.shift(minutes=30)
if random_treatment_two=='Observation':
    time_after_second_treatment= time_after_first_treatment.shift(hours=24)


print(time_after_second_treatment)  

print("Action: Treatment")

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


if random_treatment_three=='MRI':
    time_after_third_treatment= time_after_second_treatment.shift(hours=1)
if random_treatment_three=='X-Ray':
    time_after_third_treatment= time_after_second_treatment.shift(minutes=45)
if random_treatment_three=='Blood Work':
    time_after_third_treatment= time_after_second_treatment.shift(minutes=15)
if random_treatment_three=='Doppler':
    time_after_third_treatment= time_after_second_treatment.shift(minutes=45)
if random_treatment_three=='Ultrasound':
    time_after_third_treatment= time_after_second_treatment.shift(hours=1)
if random_treatment_three=='Suture':
    time_after_third_treatment= time_after_second_treatment.shift(minutes=30)
if random_treatment_three=='Observation':
    time_after_third_treatment= time_after_second_treatment.shift(hours=24)

print(time_after_third_treatment)

discharge=time_after_third_treatment.shift(hours=2)

print("Action: Discharge")
print(discharge)

total_time=discharge-intake_time
txt='Patient {} stayed for {} and received 3 treatments.'
print(txt.format(Patient_0001['Name'],total_time))

print("")
print("")
print("")





#discharge_time= -start

# total_time= end-start
# print(total_time)
# print(end)