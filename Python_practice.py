print('Hello World')

counties = ['Arapahoe','Denver','Jefferson']
if counties[1] == 'Denver':
    print(counties[1])

counties = ['Arapahoe','Denver','Jefferson']
if counties[2]!='Jefferson':
    print(counties[2])

counties = ['Arapahoe','Denver','Jefferson']
if 'El Paso' in counties:
    print('El Paso is in the list of counties.')
else:
    print('El Paso is not in the list of counties.')


for county in counties:
    print(county)

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key,value)

for county, voters in counties_dict.items():
    print(county, voters)

if 'Arapahoe' in counties_dict:
    print('Arapahoe county has 422820 registered voters.')
else:
    print('Not in the list.')

if 'Denver' in counties_dict:
    print('Denver county has 463353 registered voteres.')
else:
    print('Not in the list.')

if 'Jefferson' in counties_dict:
    print('Jefferson county has 432438 registered voters.')
else:
    print('Not in the list.')

voting_data=[{'county':'Arapahoe','registered_voters': 422829},{'county':'Denver','registered_voters': 463353},{'county':'Jefferson','registered_voters': 432438}]
for counties_dict in voting_data:
    print(counties_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for counties_dict in voting_data:
    print(counties_dict['county'])

counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
for county, voters in counties_dict.items():
    print(county + 'county has' + str(voters) + 'registered voters.')

counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters.')

counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
    print(f'{county} county has {voters:,} registered voters.')