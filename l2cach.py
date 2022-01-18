import math
import numpy as np
import pandas as pd

def l2_cache_fun(cache_length, associativity_type):
    # cache table creation
    cache_table = {}
    # default =128
    cache_length = cache_length
    # associativity_type = 2,4
    associativity_type = associativity_type

    total_sets = int(cache_length / associativity_type)

    # index and tag address creation:
    for i in range(total_sets):
        x = bin(i)[2:]
        while len(x) < math.log2(total_sets):
            x = '0' + x
        cache_table[str(x)] = []
    for i in range(total_sets):
        x = bin(i)[2:]
        while len(x) < math.log2(total_sets):
            x = '0' + x
        cache_table[str(x)].append([])
        cache_table[str(x)].append([])
        for j in range(int(associativity_type)):
            cache_table[str(x)][0].append('')
            cache_table[str(x)][1].append('')
    #####################################################################

    # memory table creation:
    membits = int(input("enter membits"))
    cache = int(input("enter cache bits"))
    mem = {}
    mem['index'] = []
    mem['address'] = []
    mem['tag'] = []
    mem['index_memory'] = []
    mem['data'] = []
    set_associativity_type = associativity_type
    num_of_set = (2 ** cache) / set_associativity_type

    tag_index_divider = math.log2(num_of_set)

    for i in range(2 ** membits):
        mem['index'].append(i)
        x = bin(i)[2:]
        while len(x) < membits:
            x = '0' + x
        mem['address'].append(x)
        t = int(math.log2((2 ** membits) // num_of_set))
        mem['index_memory'].append(x[t:])
        mem['tag'].append(x[:t])
        mem['data'].append(np.random.randint(10, 2000))
    df = pd.DataFrame(mem)
    ################################################################################

    # Associating main memory to cache memory and finding for cache miss/ cache hit:
    while True:
        memory_bits = int(input("enter memory location to search"))
        x = bin(memory_bits)[2:]
        while len(x) < membits:
            x = '0' + x
        corresponding_tag = x[:t]
        corresponding_index = x[t:]
        corresponding_tag_int = int(corresponding_tag, 2)
        print("corresponding_tag: ", corresponding_tag, ' corresponding_index: ', corresponding_index)

        if (str(corresponding_tag) in cache_table[corresponding_index][0]):
            print("cache hit")

        else:
            print("cache miss")
            data_to_write = df.iloc[memory_bits, 4]
            tag_to_write = df.iloc[memory_bits, 2]

            cache_table[str(corresponding_index)][0].append(tag_to_write)

            if '' not in cache_table[corresponding_index][1]:
                index_remover = np.random.randint(0, len(cache_table[corresponding_index][1]))
                cache_table[corresponding_index][1][index_remover] = ''

            for open_slot, stuff in enumerate(cache_table[corresponding_index][1]):
                if stuff == '':
                    cache_table[corresponding_index][1][open_slot] = str(data_to_write)
                    break

        print(pd.DataFrame(cache_table).transpose())


if __name__ == '__main__':
    # default =128
    cache_length = int(input("enter cache length"))
    # associativity_type = 2,4
    associativity_type = int(input("enter associativity type"))
    l2_cache_fun(cache_length, associativity_type)