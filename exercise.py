import heapq


def min_cost_to_combine_cables(lengths):
    # Створення мінімальної кучі з довжин кабелів
    heapq.heapify(lengths)
    total_cost = 0

    # Об'єднуємо кабелі, поки в кучі більше одного елемента
    while len(lengths) > 1:
        # Виймаємо два найменших кабелі
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # Обчислюємо витрати на об'єднання і додаємо до загальних витрат
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель з об'єднаною довжиною до кучі
        heapq.heappush(lengths, cost)

    return total_cost


# Приклад використання функції
cable_lengths = [5, 4, 2, 8]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_combine_cables(cable_lengths))