#AI-Suggested Version (Using sorted() with lambda):
def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Eve', 'age': 35}]
sorted_data = sort_dicts_by_key(data, 'age')
print(sorted_data)

#Usage:
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Eve', 'age': 35}]
sorted_data = sort_dicts_by_key(data, 'age')
print(sorted_data)

#Manual Implementation (Using Bubble Sort):
def sort_dicts_by_key_manual(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

