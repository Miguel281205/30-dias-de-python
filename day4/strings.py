
print("thirty","days","of","python")


print("Coding","for","all")

company=("Coding for all")


print(company)


len(company)

cosa=len(company)

print(cosa)

print(str.upper("hola"))
print(str.lower("ADIOS"))

print(str.capitalize("coding for all"))
print(str.title("coding for all"))


print(str.swapcase("coding for all "))

sliced=slice(1)
print(company[sliced])

company_2=[i.replace("Coding","Python") for i in company ]
print(company_2)

python=("Python","for","Everyone")
python_2=[i.replace("Everyone","All") for i in python]
print(python_2)

print("Coding for All".split())

redes="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(redes.split(","))

print(company[0])

print(company[13])

print(company[10])

palabra = "Python For Everyone".split()
print(palabra[0][0] + palabra[1][0] + palabra[2][0])

palabra2 = 'Coding For All'.split()
print(palabra2[0][0] + palabra2[1][0] + palabra2[2][0])

print(company.index("C"))

print(company.index("f"))

company3 = "Coding for all people"
print(company3.rfind("l"))

frase = "You cannot end a sentence with because because because is a conjunction"
print(frase.index("because"))

cosa2 = "You cannot end a sentence with because because because is a conjunction"
print(cosa2.rindex("because"))

print(frase.replace("because because because", "   "))

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

