from unicodedata import normalize
from operator import itemgetter

def normalize_string(name):
    ### variables ###
    file_name : str  # the name of the employee
    ### return ###
    temp_dict : dict # the name normalized
    return normalize("NFKD", name).encode("ASCII", "ignore").decode("utf-8")

def count_sales(key, sales, dict_data):
    ### variables ###
    key       : str  # the name of the employee or the date as month/year
    sales     : int  # the value of the sales
    dict_data : dict  # a pointer to the dict
    ### return ###
    None # This function needs no return because uses the pointer of the dict
    if key not in dict_data.keys(): dict_data[key] = 0
    dict_data[key] += sales

def greatest_scores(dict_data, lenght):
    ### variables ###
    dict_data : dict # dictionary to be ordened by value
    lenght    : int # lenght of the returned tuple
    ### return ###
    keys      : tuple # ordened keys
    values    : tuple # ordened values
    keys, values = [], []
    for k, v in sorted(dict_data.items(), key = itemgetter(1))[::-1]:
        keys.append(k)
        values.append(v)
    return tuple(keys[:lenght]), tuple(values[:lenght])
