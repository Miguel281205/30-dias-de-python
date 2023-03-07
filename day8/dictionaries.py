dog={}

dog["Name"]="Chuli"
dog["Color"]="Brown"
dog["Breed"]="Mastiff"
dog["Legs"]="4 legs"
dog["Age"]="15"
print(dog)


student_dictionary = {}
student_dictionary["First_name"] = "Miguel"
student_dictionary["Last_name"] = "Luna"
student_dictionary["gender"] = "Male"
student_dictionary["Age"] = "17"
student_dictionary["marital status"] = "Alone"
student_dictionary["skills"] = "Gentle"
student_dictionary["country"] = "Spain"
student_dictionary["city"] = "Jerez de la Frontera"
student_dictionary["address"] = "11407"
print(len(student_dictionary))


print(student_dictionary["skills"])

print(type(student_dictionary["skills"]))



student_dictionary["skills"] = "Playing sports like basketball or padel"

key = student_dictionary.keys()


values = student_dictionary.values
print(values)


print(student_dictionary.items())


student_dictionary.pop("gender")


del student_dictionary