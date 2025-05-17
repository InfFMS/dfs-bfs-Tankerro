# Даны N городов и M дорог между ними. Дороги двусторонние (граф неориентированный).
# Известно, что города разделены на группы (острова),
# между которыми дорог нет. То есть граф состоит из нескольких компонент связности (островов).
# Необходимо ответить на следующие вопросы:
#
# 1. Есть ли путь между двумя заданными городами (вершинами)?
# 2. Сколько всего островов (компонент связности) в графе?
# 3.Перечислить, какие города принадлежат каждому острову.
#
# Входные данные:
# Первая строка: N (количество городов) и M (количество дорог).
# Следующие M строк: пары чисел u и v, обозначающие дорогу между городами u и v.
# Затем вводится два числа: start и end — номера городов, между которыми нужно проверить наличие пути.
#
# Выходные данные:
# Ответ на вопрос, есть ли путь между start и end ("YES" или "NO").
# Количество островов (компонент связности) в графе.
# Список городов для каждого острова (в порядке возрастания номеров островов).

# Пример 1:
# 5 3
# 1 2
# 2 3
# 4 5
# 1 4
#
# Ожидаемый вывод:
#
# NO
# 2
# 1: [1, 2, 3]
# 2: [4, 5]

# Пример 2:
# 6 4
# 1 2
# 3 4
# 5 6
# 2 3
# 3 5
#
# Ожидаемый вывод:
#
# YES
# 1
# 1: [1, 2, 3, 4, 5, 6]

# Пример 3:
# 7 0
# 1 2
#
# Ожидаемый вывод:
#
# NO
# 7
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]
# 6: [6]
# 7: [7]


N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start, end = map(int, input().split())

visited = set()
stack = [start]
found = False

while stack:
    node = stack.pop()
    if node == end:
        found = True
        break
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

print("YES" if found else "NO")

visited = set()
components = []
component_id = 1

for city in range(1, N + 1):
    if city not in visited:
        stack = [city]
        current_component = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                current_component.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        current_component.sort()
        components.append((component_id, current_component))
        component_id += 1

print(len(components))
for comp_id, cities in components:
    print(f"{comp_id}: {cities}")