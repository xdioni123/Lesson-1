x = 5 #int
y = 6.5 #float/double
emri = "Medina" #string

# typecasting
x = str(x)

print(type(x))
print(type(y))
print(type(emri))

#print(x+y)

age = 30

print("Besarti eshte age", age , "vjec")

first_name = "Jon"
last_name = "Behra"

full_name = first_name + "" + last_name

print(full_name)

# ---------------------------------------------
# Lists

cars = ["Audi", "Bmw", "Mercedes", "Mazda"]

print(cars[1])

diff_elem = ["Klima", "Markeri", 2, 30, 4.5]

# elementi i fundit i listes
print(diff_elem[-1])

diff_elem.append("Futboll")

print(diff_elem)

diff_elem[0] = "Klime"

print(diff_elem)

diff_elem.insert(1, "Kompjuteri")

print(diff_elem)

diff_elem.remove("Markeri")

print(diff_elem)

# reversed list
print(diff_elem[::-1])

# tupless

words = ("shkolla", "klasa", "python", "sql")

print(words)

print(words[-1])

print(words[-3])#klasa

#slicing
print(words[0:2])

#words[2] = "Java"

print(words[1].count("a"))

# Dictionaries
# key value pairs, mutable

countries = {
            "Kosova" : "Prishtina",
            "Shqiperia" : "Tirana",
            "Germany" : "Berlin",
            "Canada" : "Otawa",
            "Australia" : "Canberra",
            "Egypt" : "Cairo"
            }

print(countries)

ks = countries["Kosova"]

print(ks)

# values
kryeqytet = countries.values()

print(kryeqytet)

shtetet = countries.keys()
print(shtetet)

del kryeqytet["Egypt"]