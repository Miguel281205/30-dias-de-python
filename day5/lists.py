lista=list()
print(lista)

lista2=["uno","dos","tres","cuatro","cinco"]

print(len(lista2))

print(lista2[0],lista2[2],lista2[4])

mixed_data_types= ["Miguel","16","1.80","No casado","Jerez de la Frontera"]
print(mixed_data_types)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[3], it_companies[6])

it_companies[3]="SpaceX"
print(it_companies)

it_companies.append("Tesla")
print(it_companies)


it_companies.insert(3, "AMD")
print(it_companies)


#el .upper no me funciona

print("SpaceX" in it_companies)

it_companiess = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companiess.sort()

print(it_companies.reverse())

it_companies in it_companies[2:]



it_companies = it_companies[:4]


it_companies = it_companies[:3]



it_companies.pop(0)


it_companies.pop(1)


it_companies.pop(-1)



it_companies.clear() 



del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_end = front_end.append(back_end)