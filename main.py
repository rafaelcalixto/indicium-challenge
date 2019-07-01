from datetime import date
from io_utils import get_dictdata, report, plot_graphs
from logic_utils import greatest_scores, normalize_string, count_sales

deals = get_dictdata("deals")
contacts = get_dictdata("contacts")
companies = get_dictdata("companies")
sectors = get_dictdata("sectors")

employee_sales = {}
month_sales = {}
sector_sales = {}

for key in deals.keys():
    if deals[key][2] in contacts.keys():
        employee = normalize_string(contacts[deals[key][2]][0])
        count_sales(employee, int(deals[key][1]), employee_sales)

    month, day, year = deals[key][0].split("/")
    period = date(int(year), int(month), int(day)).strftime("%B") + "/" + year
    count_sales(period, int(deals[key][1]), month_sales)

    if deals[key][3] in contacts.keys():
        sector = sectors[companies[deals[key][3]][-1]][0]
        count_sales(sector, int(deals[key][1]), sector_sales)

k_employees, v_employees = greatest_scores(employee_sales, 10)
k_month, v_month = greatest_scores(month_sales, 10)
sectors, sales = greatest_scores(sector_sales, len(sector_sales))

plot_graphs(k_employees, v_employees, "Employee Sales", "Employee Sales Graph")
plot_graphs(k_month, v_month, "Month Sales", "Month Sales Graph")

report(sectors, sales)
