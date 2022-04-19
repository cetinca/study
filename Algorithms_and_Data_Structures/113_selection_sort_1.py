# This code here at the top is the same as we saw in the Bogosort
# example. It just loads a Python list of numbers from a file.

numbers = [1, 789, 5, 75, 524, 132]
def selection_sort(values):
  sorted_list = []
  for i in range(0, len(values)):
    index_to_move = index_of_min(values)
    sorted_list.append(values.pop(index_to_move))
  return sorted_list

def index_of_min(values):
  min_index = 0
  for i in range(1, len(values)):
    if values[i] < values[min_index]:
      min_index = i
  return min_index

print(selection_sort(numbers))