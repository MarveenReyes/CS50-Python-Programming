from datetime import date
import inflect


p = inflect.engine()

bday = input("Date of Birth: ")
splitted = bday.split('-')
splitted = [int(n) for n in splitted]

bdayconv = date(splitted[0],splitted[1],splitted[2])
now = date.today()
age = now - bdayconv
time = age * 24 * 60
time = str(time)
x = time.split()
z = x[0]


h = p.number_to_words(z).capitalize()
print(h,'minutes')
