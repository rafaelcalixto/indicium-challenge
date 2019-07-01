from csv import reader
from unicodedata import normalize
from datetime import date
from matplotlib import pyplot
from utils import get_dictdata, normalize_string, count_sales

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

plot_graphs( tuple(employee_sales.keys())
           , tuple(employee_sales.values())
           , "Employee Sales"
           , "Employee Sales Graph")

plot_graphs( tuple(month_sales.keys())
           , tuple(month_sales.values())
           , "Month Sales"
           , "Month Sales Graph")
