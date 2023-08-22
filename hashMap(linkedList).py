from linkedList import Node, LinkedList   

class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [LinkedList() for _ in range(self.size)]  # Создаем экземпляры LinkedList для каждой ячейки массива

    def hash(self, key):
        return sum(key.encode())  # Вычисляем хеш ключа

    def compress(self, hash_code):
        return hash_code % self.size  # Применяем операцию взятия остатка для сжатия хеш-кода в диапазон размера массива

    def assign(self, key, value):
        payload = [key, value]  # Создаем пару ключ-значение для вставки
        array_index = self.compress(self.hash(key))  # Получаем индекс ячейки массива для вставки
        list_at_array = self.array[array_index]  # Получаем экземпляр LinkedList для данной ячейки массива
        node = list_at_array.find_node(key)  # Ищем ноду с заданным ключом в списке
        if node:
            node.value[1] = value  # Если нода найдена, обновляем значение
        else:
            list_at_array.insert_end(payload)  # Если нода не найдена, вставляем новую ноду в конец списка

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))  # Получаем индекс ячейки массива для поиска
        list_at_array = self.array[array_index]  # Получаем экземпляр LinkedList для данной ячейки массива
        node = list_at_array.find_node(key)  # Ищем ноду с заданным ключом в списке
        if node:
            return node.value[1]  # Если нода найдена, возвращаем её значение
        return None  # Если нода не найдена, возвращаем None

# Создаем экземпляр HashMap с размером 10
hash_map = HashMap(10) 

# Вставляем пары ключ-значение в хэш-мапу
hash_map.assign("one", "first")
hash_map.assign("two", "second")

# Выводим значения, связанные с ключами
print(hash_map.retrieve("one"))  # Выведет: "first"
print(hash_map.retrieve("two"))  # Выведет: "second"
print(hash_map.retrieve("three"))  # Выведет: None, так как такого ключа нет

