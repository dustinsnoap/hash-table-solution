class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # $%$Start
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.item_count = 0
        # $%$End

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # $%$Start
        return len(self.storage)
        # $%$End

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # $%$Start
        return self.item_count / self.capacity
        # $%$End

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # $%$Start
        # 64-bit constants
        FNV_offset_basis_64 = 0xcbf29ce484222325
        FNV_prime_64 = 0x100000001b3

        # Cast the key to a string and get bytes
        str_key = str(key).encode()

        hash = FNV_offset_basis_64

        for b in str_key:
            hash *= FNV_prime_64
            hash ^= b
            hash &= 0xffffffffffffffff  # 64-bit hash

        return hash
        # $%$End

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # $%$Start
        # Cast the key to a string and get bytes
        str_key = str(key).encode()

        # Start from an arbitrary large prime
        hash_value = 5381

        # Bit-shift and sum value for each character
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits

        return hash_value
        # $%$End

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # $%$Start
        index = self.hash_index(key)

        current_entry = self.storage[index]

        #if current_entry is not None and current_entry.key != key:
        #    print(f"collision ({key}<>{current_entry.key})")

        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next

        if current_entry is not None:
            current_entry.value = value
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry

            # Auto resize if load factor too high
            self.item_count += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
        # $%$End

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # $%$Start
        index = self.hash_index(key)

        current_entry = self.storage[index]
        last_entry = None

        while current_entry is not None and current_entry.key != key:
            last_entry = current_entry
            current_entry = last_entry.next

        if current_entry is None:
            print("ERROR: Unable to remove entry with key " + key)
        else:
            if last_entry is None:  # Removing the first element in the LL
                self.storage[index] = current_entry.next
            else:
                last_entry.next = current_entry.next

            # Auto resize if load factor too low
            self.item_count -= 1
            if self.get_load_factor() < 0.2:
                if self.capacity > MIN_CAPACITY:
                    new_capacity = self.capacity // 2
                    if new_capacity < MIN_CAPACITY:
                        new_capacity = MIN_CAPACITY

                    self.resize(new_capacity)
        # $%$End

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # $%$Start
        index = self.hash_index(key)

        current_entry = self.storage[index]

        while current_entry is not None:
            if(current_entry.key == key):
                return current_entry.value
            current_entry = current_entry.next
        # $%$End

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # $%$Start
        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * self.capacity

        current_entry = None

        # Save this because put adds to it, and we don't want it to.
        # It might be less hackish to pass a flag to put indicating that
        # we're in a resize and don't want to modify item count.
        old_item_count = self.item_count

        for bucket_item in old_storage:
            current_entry = bucket_item
            while current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next

        # Restore this to the correct number
        self.item_count = old_item_count
        # $%$End


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
