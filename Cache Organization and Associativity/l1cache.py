import math
import numpy as np
import pandas as pd


def l1cache_fun(cache, membits):
    mem = {}
    mem['index'] = []
    mem['address'] = []
    mem['tag'] = []
    mem['index_memory'] = []
    mem['data'] = []
    for i in range(2 ** membits):
        mem['index'].append(i)
        x = bin(i)[2:]
        while len(x) < membits:
            x = '0' + x
        mem['address'].append(x)
        t = int(math.log2((2 ** membits) // (2 ** cache)))
        mem['index_memory'].append(x[t:])
        mem['tag'].append(x[:t])
        mem['data'].append(np.random.randint(10, 2000))
    df = pd.DataFrame(mem)
    print("df: \n", df)

    # Creating Cache memory
    cach_mem = {}
    cach_mem['tag'] = []
    cach_mem['index_cache'] = []
    cach_mem['data'] = []
    cach_mem['valid_bit'] = []
    for i in range(2 ** cache):
        x = bin(i)[2:]
        while len(x) < membits:
            x = '0' + x
        t = int(math.log2((2 ** membits) // (2 ** cache)))

        cach_mem['index_cache'].append(x[t:])
        cach_mem['tag'].append(x[:t])
        cach_mem['data'].append('None')
        cach_mem['valid_bit'].append('0')
    cdf = pd.DataFrame(cach_mem)
    print("cdf: \n", cdf)
    ##########################################################################

    while True:
        inp = int(input("enter the index u want to search"))
        t = int(math.log2((2 ** membits) // (2 ** cache)))
        bin_inp = bin(inp)
        x = bin_inp[2:]
        while len(x) < membits:
            x = '0' + x
        print("x: ", x)
        tag = x[:t]
        index_to_search = x[t:]
        print("tag: ", tag, " index: ", index_to_search)
        if float(index_to_search) == float(cdf.loc[(cdf['index_cache'] == index_to_search), 'index_cache']):
            print("condition 1: ", float(tag) == float(cdf.loc[(cdf['index_cache'] == index_to_search), 'tag']),
                  " condition 2: ", float(cdf.loc[(cdf['index_cache'] == index_to_search), 'valid_bit'] == 1.0))
            if (float(tag) == float(cdf.loc[(cdf['index_cache'] == index_to_search), 'tag']) and float(
                    cdf.loc[(cdf['index_cache'] == index_to_search), 'valid_bit']) == 1.0):

                print(" Cache Hit! Data found and retriving from cache: ",
                      cdf.loc[(cdf['index_cache'] == index_to_search), 'data'])

            else:
                print("Tag not found retrieving from memory... Cache miss!")
                tag_to_replace = df['tag'][inp]
                data_to_replace = df['data'][inp]
                cdf.loc[(cdf['index_cache'] == index_to_search), 'tag'] = str(tag_to_replace)
                cdf.loc[(cdf['index_cache'] == index_to_search), 'data'] = str(data_to_replace)
                cdf.loc[(cdf['index_cache'] == index_to_search), 'valid_bit'] = str(1)
                print("Updated cache table:\n ", cdf, "\n")


if __name__ == "__main__":
    mem_size = int(input("Enter the num of bits address "))
    cache = int(input("Enter the cache size "))
    l1cache_fun(cache, mem_size)

