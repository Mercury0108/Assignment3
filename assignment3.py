def replace_value(values, index, new_value):
  values[index] = new_value
def find_first(values, target):
  for i in range(len(values)):
    if values[i] == target:
      return i
  return -1
def summarize(values):
  tupple = (min(values), max(values), sum(values))
  return tupple
days = int(input('Enter the number of days: '))
original = []
for i in range(days):
  reading = int(input('Enter reading time in minutes: '))
  original.append(reading)
updated = original[:]
index = int(input('Enter the index to correct: '))
new_value = int(input('Enter the new reading time in minutes: '))
replace_value(updated, index, new_value)
target = int(input('Enter the reading time to search for: '))
find_first(updated, target)
count = updated.count(target)
minimum, maximum, total = summarize(updated)
updated_sorted = sorted(updated)
print(f'Original: {original}')
print(f'Updated: {updated}')
print(f'Sorted: {updated_sorted}')
print(f'Minimum reading time: {minimum} minutes')
print(f'Maximum reading time: {maximum} minutes')
print(f'Total reading time: {total} minutes')
print(f'First matching index: {find_first(updated, target)}' if find_first(updated, target) != -1 else 'Target not found')
print(f'Matching values: {count}')
