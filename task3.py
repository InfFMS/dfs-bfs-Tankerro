# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D

graph = {"A" : ["B", "C"],
        "B" : ["C"],
        "C" : [],
        "D" : []}

# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена

from collections import deque


def alg_Kan(graph):
        in_degree = {node: 0 for node in graph}
        for node in graph:
                for neighbor in graph[node]:
                        in_degree[neighbor] += 1

        queue = deque([node for node in graph if in_degree[node] == 0])
        top_order = []

        while queue:
                current = queue.popleft()
                top_order.append(current)

                for neighbor in graph[current]:
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                                queue.append(neighbor)

        if len(top_order) != len(graph):
                return None  # В графе есть цикл

        return top_order


graph = {
        "A": ["B", "D"],
        "B": ["C"],
        "C": [],
        "D": []
}

result = alg_Kan(graph)
print("Топологический порядок:", result)