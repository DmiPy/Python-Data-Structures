class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        self.insert_or_update(key, value)

    def insert_or_update(self, key, value):
        # Calculate the array index using hash and compression
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # If the slot is empty or the key matches, update or insert
        if current_array_value is None or current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Handle collision using linear probing
        self.handle_collision(key, value, array_index)

    def handle_collision(self, key, value, start_index):
        collisions = 1
        current_array_value = self.array[start_index]

        # Continue probing until an empty slot or matching key is found
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            # If an empty slot or matching key found, insert or update
            if current_array_value is None or current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            collisions += 1

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        # Handle retrieval collision using linear probing
        return self.handle_retrieval_collision(key, array_index)

    def handle_retrieval_collision(self, key, start_index):
        retrieval_collisions = 1
        possible_return_value = self.array[start_index]

        # Continue probing until a matching key is found or an empty slot
        while possible_return_value[0] != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

    def delete(self, key):
        array_index = self.compressor(self.hash(key))
        possible_delete_value = self.array[array_index]

        if possible_delete_value is None:
            return None

        if possible_delete_value[0] == key:
            self.array[array_index] = [None, None]
            return

        # Handle deletion collision using linear probing
        self.handle_deletion_collision(key, array_index)

    def handle_deletion_collision(self, key, start_index):
        collisions = 1
        possible_delete_value = self.array[start_index]

        # Continue probing until a matching key is found or an empty slot
        while possible_delete_value[0] != key:
            new_hash_code = self.hash(key, collisions)
            deleting_array_index = self.compressor(new_hash_code)
            possible_delete_value = self.array[deleting_array_index]

            if possible_delete_value is None:
                return None

            if possible_delete_value[0] == key:
                self.array[deleting_array_index] = [None, None]
                return

            collisions += 1