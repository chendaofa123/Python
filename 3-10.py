countries=['China','America','England','France']
countries.append('Russia')
print(countries)
countries.insert(2,'Germany')
print(countries)
del countries[3]
print(countries)
print(sorted(countries))
countries.sort(reverse=True)
print(countries)
print(len(countries))
