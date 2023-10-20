print()
print('** UNIT CONVERTER **')
print

unit_conversion = [('1', 'mi', 'km'),('2', 'km', 'mi')]

print('unit conversion:')
print()

for unit_converter, from_unit, to_unit in unit_conversion:
	print(f'{unit_converter}) {from_unit} -> {to_unit}')

print()
conversion = input('Enter conversion type to use -->')
conversion_index = int(conversion) - 1

unit_converter, from_unit, to_unit = unit_conversion[conversion_index]
print()
from_value = float(input(f'Enter {from_unit} --> '))
print()

if unit_converter == '1':
	to_value = from_value * 1.61
	print(f'{from_value} {from_unit} -> {to_value} {to_unit}')