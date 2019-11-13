import tkinter as tk
import math

global output

PRODUCT_TYPE_OPTIONS = ["Road/TT/Gravel Bike", "Mountain Bike", "Wheels", "Mountain Bike Frame", "Road/TT/Gravel Frame", "Power Meter",
                        "Crankset", "Handlebars", "Forks", "Chainrings", "Shifters", "Groupset", "Cassette", "Computer/GPS", "Seatpost",
                        "Rear Shocks", "Brakes", "Stem", "Saddle", "Bottle Cage", "Pedals", "Hub"]
product_entries = []
product_titles = []

root = tk.Tk()
root.minsize(970, 600)
mainFrame = tk.Frame(root)
secondaryFrame = tk.Frame(mainFrame)
mainFrame.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)

output = tk.Text(secondaryFrame, wrap=tk.WORD, height=10)
cl_output = tk.Text(secondaryFrame, wrap=tk.WORD, height=10)

def addAttributes():
    for widget in secondaryFrame.winfo_children():
        widget.destroy()
    global output
    global cl_output
    output = tk.Text(secondaryFrame, wrap=tk.WORD, height=10)
    cl_output = tk.Text(secondaryFrame, wrap=tk.WORD, height=10)

    prod_type = productType.get()
    if prod_type == PRODUCT_TYPE_OPTIONS[0]:
        addTitles(["Year", "Brand", "Model", "Size", "Frame", "Fork", "Front Derailleur", "Rear Derailleur",
                               "Shifters", "Crankset", "Chainrings", "Cassette", "Handlebar", "Stem", "Seatpost", "Saddle",
                               "Wheels", "Brakes"])
    elif prod_type == PRODUCT_TYPE_OPTIONS[1]:
        addTitles(["Year", "Brand", "Model", "Size", "Frame", "Fork", "Shock", "Front Derailleur", "Rear Derailleur",
                               "Shifters", "Crankset", "Chainrings", "Cassette", "Handlebar", "Stem", "Seatpost", "Saddle",
                               "Wheels", "Brakes"])
    elif prod_type == PRODUCT_TYPE_OPTIONS[2]:
        addTitles(["Brand", "Model", "Rim Type", "Size", "Hubs", "Rim Material", "Freehub Type",
                            "Front Axle", "Rear Axle", "Brake Type", "Valve Type", "Skewers", "Use"])
    elif prod_type == PRODUCT_TYPE_OPTIONS[3]:
        addTitles(["Year", "Brand", "Model", "Size", "Frame Material", "Fork", "Fork Travel", "Steerer Tube", "Rear Shock", "Rear Travel", "Brake Type", "Front Derailleur Mount", "Headset", "Bottom Bracket", "Seatpost Clamp", "Rear Axle"])
    elif prod_type == PRODUCT_TYPE_OPTIONS[4]:
        addTitles(["Year", "Brand", "Model", "Size", "Frame Material", "Steerer Tube", "Brake Type", "Front Derailleur Mount", "Headset", "Bottom Bracket", "Seatpost Clamp","Front Axle", "Rear Axle"])
    elif prod_type == PRODUCT_TYPE_OPTIONS[5]:
        addTitles(["Brand", "Model", "Arm Length", "Chain Rings", "Bottom Bracket", "Wireless Protocol"])
    #Crankset
    elif prod_type == PRODUCT_TYPE_OPTIONS[6]:
        addTitles(["Brand", "Model", "Group", "Chain Rings", "Arm Length", "Bottom Bracket Type", "Use"])
    #Handlebars
    elif prod_type == PRODUCT_TYPE_OPTIONS[7]:
        addTitles(["Brand", "Model", "Type", "Material", "Clamp Diameter", "Width", "Reach", "Drop", "Use"])
    # Forks
    elif prod_type == PRODUCT_TYPE_OPTIONS[8]:
        addTitles(["Brand", "Model", "Wheel Size", "Travel", "Stanchion Size", "Spring Type", "Steerer Tube Diameter", "Steerer Tube Length",
                   "Brake Type"])
    # Chainrings
    elif prod_type == PRODUCT_TYPE_OPTIONS[9]:
        addTitles(["Brand", "Model", "Speed", "Type", "Number of Teeth", "Use"])
    # Forks
    elif prod_type == PRODUCT_TYPE_OPTIONS[10]:
        addTitles(["Brand", "Model", "Type", "Left Shifter", "Right Shifter", "Actuation", "Brake Type", "Use"])
    # Groupset
    elif prod_type == PRODUCT_TYPE_OPTIONS[11]:
        addTitles(["Brand", "Group", "Type", "Front Shifter", "Rear Shifter", "Front Derailleur", "Rear Derailleur", "Crankset", "Brakes",
                   "Chain", "Cassette", "Bottom Bracket", "Use"])
    # Cassette
    elif prod_type == PRODUCT_TYPE_OPTIONS[12]:
        addTitles(["Brand", "Model", "Speed", "Gear Range", "Freehub Type", "Use"])
    # Computer
    elif prod_type == PRODUCT_TYPE_OPTIONS[13]:
        addTitles(["Brand", "Model", "Wireless", "Protocols", "GPS", "Mount", "Charger", "Heart Rate Strap", "Speed Sensor"])
    # Seatpost
    elif prod_type == PRODUCT_TYPE_OPTIONS[14]:
        addTitles(["Brand", "Model", "Length", "Diameter", "Travel", "Material", "Use"])
    # Rear Shock
    elif prod_type == PRODUCT_TYPE_OPTIONS[15]:
        addTitles(["Brand", "Model", "Size", "Type"])
    # Brakes
    elif prod_type == PRODUCT_TYPE_OPTIONS[16]:
        addTitles(["Brand", "Model", "Position", "Type", "Hose Length", "Use"])
    # Stem
    elif prod_type == PRODUCT_TYPE_OPTIONS[17]:
        addTitles(["Brand", "Model", "Steerer Clamp", "Length", "Clamp Size", "Material", "Use"])
    # Saddle
    elif prod_type == PRODUCT_TYPE_OPTIONS[18]:
        addTitles(["Brand", "Model", "Type", "Rail Material"])
    # Bottle Cage
    elif prod_type == PRODUCT_TYPE_OPTIONS[19]:
        addTitles(["Brand", "Model", "Type", "Material"])
    # Pedals
    elif prod_type == PRODUCT_TYPE_OPTIONS[20]:
        addTitles(["Brand", "Model", "Spindle", "Type", "Material", "Use", "Cleat Type"])
    # Hub
    elif prod_type == PRODUCT_TYPE_OPTIONS[21]:
        addTitles(["Brand", "Model", "Freehub Type", "Brake Type", "Use"])

def generateListing():
    output.delete('1.0', tk.END)
    output.insert(tk.END, getHeader())
    output.insert(tk.END, addUpperHTML())
    output.insert(tk.END, createColumns())
    output.insert(tk.END, addConditionNotes())
    generateCLListing()

def generateCLListing():
    cl_output.delete('1.0', tk.END)
    for i in range(len(product_entries)):
        cl_output.insert(tk.END, product_titles[i] + ": " + product_entries[i].get() + "\n\n")

    if productType.get() == PRODUCT_TYPE_OPTIONS[0] or productType.get() == PRODUCT_TYPE_OPTIONS[1]:
        cl_output.insert(tk.END, "Call, text, or email to come see the bike.")
    elif productType.get() == PRODUCT_TYPE_OPTIONS[2]:
        cl_output.insert(tk.END, "Call, text, or email to come see the wheels.")
    else:
        cl_output.insert(tk.END, "")



def getHeader():
    if (productType.get() == PRODUCT_TYPE_OPTIONS[0] or productType.get() == PRODUCT_TYPE_OPTIONS[1]):
        return('<h2 style="text-align: center;">Bike Specs</h2>')
    elif (productType.get() == PRODUCT_TYPE_OPTIONS[2]):
        return('<h2 style="text-align: center;">Wheel Specs</h2>')
    elif (productType.get() == PRODUCT_TYPE_OPTIONS[3]):
        return('<h2 style="text-align: center;">Frame Specs</h2>')
    elif (productType.get() == PRODUCT_TYPE_OPTIONS[4]):
        return('<h2 style="text-align: center;">Frame Specs</h2>')
    else:
        return('<h2 style="text-align: center;">Part Specs</h2>')

def addConditionNotes():
    return('</div></div><h3 style="text-align: center; font-family: sans-serif;">Condition Notes:</h3>'
           '<p style="text-align: center; font-family: sans-serif;">' + product_entries[len(product_entries)-1].get()) + '</p>'

def addUpperHTML():
    return('<div class="myRow"><div>')

def addColumn2():
    return('<div class="myColumn2"></div>')

def createColumns():
    midpoint = math.ceil((len(product_entries)-1)/2)

    output_string = '<div class="myColumn"><table width="100%" style="text-align: center;"><tbody>'

    for i in range(midpoint):
        output_string += ('<tr><td width="50%" valign="top"><b>' + product_titles[i] + ':</b></td><td width="50%" valign="top"><span>' + product_entries[i].get() + '</span></td></tr>')

    output_string += ('</tbody></table></div>')
    output_string += (addColumn2())
    output_string += '<div class="myColumn"><table width="100%" style="text-align: center;"><tbody>'
    for i in range(midpoint, (len(product_entries)-1)):
        output_string += ('<tr><td width="50%" valign="top"><b>' + product_titles[i] + ':</b></td><td width="50%" valign="top"><span>' + product_entries[i].get() + '</span></td></tr>')

    output_string += ('</tbody></table></div>')
    return output_string

def addTitles(titles):
    product_entries.clear()
    product_titles.clear()

    for i in range(len(titles)):
        tk.Label(secondaryFrame, text=titles[i]).grid(row=i, column=0, columnspan=1, sticky=tk.NSEW, padx=5, pady=1)
        product_titles.append(titles[i])
        entry = tk.Entry(secondaryFrame)
        product_entries.append(entry)
        entry.grid(row=i, column=1, sticky=tk.NSEW, columnspan=1, padx=5, pady=1)

    tk.Label(secondaryFrame, text="Condition Notes").grid(row=len(titles), column=0, columnspan=1, sticky=tk.NSEW, padx=5, pady=1)
    product_titles.append("Condition Notes")
    entry = tk.Entry(secondaryFrame)
    product_entries.append(entry)
    entry.grid(row=len(titles), column=1, sticky=tk.NSEW, columnspan=1, padx = 5, pady=1)

    generateButton = tk.Button(secondaryFrame, text="Generate Listing", command=generateListing)
    generateButton.grid(row=0, column=2, columnspan =1, sticky=tk.NSEW)
    output.grid(row=1, column=2, columnspan=1, rowspan=len(titles)//2, sticky=tk.NSEW)
    tk.Label(secondaryFrame, text="Craigslist Ad").grid(row=((len(titles)//2)+1), column=2, columnspan=1, sticky=tk.NSEW)
    cl_output.grid(row=(len(titles)//2)+2, column=2, columnspan=1, rowspan=len(titles)//2, sticky=tk.NSEW)


def clearLayout():
    for widget in secondaryFrame.winfo_children():
        widget.destroy()

def layoutGrid():
    mainFrame.grid_columnconfigure(0, weight=1)
    mainFrame.grid_columnconfigure(1, weight=1)
    mainFrame.grid_columnconfigure(2, weight=1)

    secondaryFrame.grid_columnconfigure(0, weight=1)
    secondaryFrame.grid_columnconfigure(1, weight=1)
    secondaryFrame.grid_columnconfigure(2, weight=1)

    productTitle.grid(row=0, column=1, columnspan=1, sticky=tk.NSEW)
    productTypeSelector.grid(row=1, column=1, columnspan=1, sticky=tk.NSEW)
    submitButton.grid(row=2, column=1, columnspan=1, sticky=tk.NSEW)
    secondaryFrame.grid(row=4, column=0, columnspan=3, sticky=tk.NSEW, pady=50, padx=50)


root.title("OCC Product Generator")
root.state('zoomed')

productTitle = tk.Label(mainFrame, text="")

productType = tk.StringVar(mainFrame)
productType.set(PRODUCT_TYPE_OPTIONS[1])
productTypeSelector = tk.OptionMenu(*(mainFrame, productType) + tuple(PRODUCT_TYPE_OPTIONS))

submitButton = tk.Button(mainFrame, text="Submit", width=25, command=addAttributes)

layoutGrid()
root.mainloop()
