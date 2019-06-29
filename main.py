from csv import reader
from unicodedata import normalize
from datetime import date
from matplotlib import pyplot

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
    # This function needs no return because uses the pointer of the dict
    if key not in dict_data.keys(): dict_data[key] = 0
    dict_data[key] += sales


deals = get_dictdata("deals")
contacts = get_dictdata("contacts")
companies = get_dictdata("companies")
sectors = get_dictdata("sectors")

employee_sales = {}
month_sales = {}

for key in deals.keys():
    if deals[key][3] in contacts.keys():
        employee = normalize_string(contacts[deals[key][3]][0])
        count_sales(employee, int(deals[key][1]), employee_sales)

    month, day, year = deals[key][0].split("/")
    period = date(int(year), int(month), int(day)).strftime("%B") + "/" + year
    count_sales(period, int(deals[key][1]), month_sales)

# offline.plot({"data": [ {"x" : tuple(employee_sales.keys())},
#                         {"y" : tuple(employee_sales.values())} ],
#       "layout" : {"title" : "Employee Sales Graph",
#       "font" : dict(family = "Comic Sans MS", size = 12)}},
#       image = "png", auto_open = False, image_width = 1000, image_height = 500,
#       filename = "Employee Sales Graph.html")


# plotly.iplot([graph_objs.Bar(  x = tuple(month_sales.keys())
#                              , y = tuple(month_sales.values()))]
#                              , filename = "Month Sales Graph")


y = tuple(employee_sales.values())
x = tuple(employee_sales.keys())

pyplot.plot(x, y, label = "Employee Sales")
pyplot.title("Employee Sales Graph")
pyplot.xticks(x, x, rotation = "vertical")
pyplot.legend(loc="upper center", bbox_to_anchor = (0.5, -0.1), fancybox = True, ncol = 2)

pyplot.savefig("Employee Sales Graph.png")
