from csv import reader, writer
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
            temp_dict[str(row[0]).replace('"','')] = row[1:]
    return temp_dict

def plot_graphs(x, y, label, title):
    ### variables ###
    x     : tuple # data to be ploted at x vector
    y     : tuple # data to be ploted at y vector
    label : str   # label for the y data
    title : str   # title for the graph
    ### return ###
    None
    pyplot.bar(x, y, label = label)
    pyplot.title(title)
    pyplot.xticks(x, x, rotation = 40)
    pyplot.legend( loc="upper center", bbox_to_anchor = (0.5, -0.1)
                 , fancybox = True, ncol = 2)
    fig = pyplot.gcf()
    fig.set_size_inches(15, 8.5)
    pyplot.savefig( title + ".png" )
    pyplot.clf()
    pyplot.cla()
    pyplot.close()

def report(sectors, sales):
    ### variables ###
    sectors : tuple # List of sector ordened by sales volume
    sales   : tuple # List of sales in a descendent order
    ### return ###
    None
    with open("sector report.csv", "w", newline = "\n") as file:
        csv_writer = writer(file, delimiter = ";", )
        print("Report:\nThose are the sectors of the company ranked by the sales")
        for ind, sec in enumerate(sectors):
            csv_writer.writerow((str(int(ind) + 1), sec, sales[ind]))
            print(str(int(ind) + 1), sec, sales[ind])
