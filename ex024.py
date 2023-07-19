city = str(input('Digite o nome da sua cidade: ').strip().upper())
result = 'SANTO' in city.split()[0].upper()
print(f'A cidade {city} começa com a palavra SANTO? {result}')