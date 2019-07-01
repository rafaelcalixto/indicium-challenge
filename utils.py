def get_dictdata(file_name):
    ### variables ###
    file_name : str  # the name of the tsv file without the extention
    ### return ###
    temp_dict : dict # dictionary with the id column as key and the rest of the
                     # row as value
    temp_dict = {}
    with open("data/" + file_name + ".tsv") as file:
        for row in tuple(reader(file, delimiter = "\t"))[1:]:
            temp_dict[row[0]] = row[1:]
    return temp_dict

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

def plot_graphs(x, y, label, title):
    ### variables ###
    x     : tuple # data to be ploted at x vector
    y     : tuple # data to be ploted at y vector
    label : str   # label for the y data
    title : str   # title for the graph
    ### return ###
    None
    pyplot.plot(x, y, label = label)
    pyplot.title(title)
    pyplot.xticks(x, x, rotation = "vertical")
    pyplot.legend( loc="upper center", bbox_to_anchor = (0.5, -0.1)
                 , fancybox = True, ncol = 2)
    pyplot.savefig( title + ".png" )
