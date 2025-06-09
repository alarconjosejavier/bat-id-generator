print('Please enter the following information: \n')

first_name = input('First Name: ')
last_name = input('Last Name: ')
email = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ' )
hair_color = input('Hair: ')
eye_color = input('Eyes: ')
month = input('Month that you started: ')
training = input('Did you complete advanced training: ')

print(' \n')

output= f'The ID Card is: \n --------------------------------------- \n {last_name.upper()}, {first_name} \n {job_title.title()} \n ID: {id_number} \n\n {email.lower()} \n {phone_number} \n'
 
print(output)
print()

#print('Hair: {:<15}'.format(hair_color) + 'Eyes: ' + eye_color)
#print('Month: {:<14}'.format(month) + 'Training: ' + training )
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {month:14} Training: {training}')
print('----------------------------------------')

