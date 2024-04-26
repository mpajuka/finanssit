import locale
from decimal import getcontext
from matplotlib.ticker import ScalarFormatter
import mplcursors
import matplotlib.pyplot as plt
getcontext().prec = 2
locale.setlocale(locale.LC_ALL, '')


def calculate_investments(curr_value, cont, r, t):
    """Calculate the development of investment based on the initial invested sum,
    the possible monthly contribution, user determined estimated return, and the
    time horizon for which the funds are aimed to be invested for. After the
    calculations have been formed a matplotlib figure is formed of the data,
    

    Args:
        curr_value (ttk.Entry): Current (€) value of invested funds
        cont (ttk.Entry): Possible monthly contribution added to the investments (€)
        r (ttk.Entry): Estimated percentage of yearly returs (% p.a.)
        t (ttk.Entry): Time horizon in years
    """
    initial_investment_value = float(curr_value)

    regular_contributions = 0
    total_current_contributions = initial_investment_value
    y = []
    y_int = []
    all_contributions = []
    for i in range(1, int(t)+1):
        year_of_monthly_contributions = float(cont)*12
        return_as_float = float(r)/100

        temp = regular_contributions * (1 + return_as_float)
        regular_contributions = temp + year_of_monthly_contributions

        future_value = initial_investment_value * (1 + return_as_float) ** i + regular_contributions

        y.append("{:0.2f}".format(future_value))
        y_int.append((int(float("{:0.2f}".format(future_value)))))

        total_current_contributions += year_of_monthly_contributions
        all_contributions.append(total_current_contributions)

    form_plot(y_int, all_contributions, t)

def form_plot(y_int, all_contributions, t):
    """Forms the matplotlib figure from the data calculated with possible returns
    initial investment and monthly contributions, for each yearly point. A trend line
    is then formed which contains the datapoints which have annotations display additional
    information when hovered on.

    Args:
        y_int (list): y-axis values appended as integers
        all_contributions (list): investments value at each year
        t (string): the time horizon in years
    """
    x = list(range(1, int(t)+1))
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.plot(x, y_int, color='#85BB65')
    ax.plot(x, all_contributions, color='orange')
    data1 = ax.scatter(x, y_int, s=50, color='#85BB65',
                       label='Invested funds + value development')

    data2 = ax.scatter(x, all_contributions, s=50,
                       color='orange', label='Invested funds')
    plt.xticks(range(min(x), max(x)+1))

    ax.ticklabel_format(useOffset=False)
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.format_coord = format_coord
    ax.ticklabel_format(style='plain')

    plt.legend(loc='upper left')

    mplcursors.cursor({data1, data2}, hover=True).connect("add", on_hover)

    plt.xlabel('Years')
    plt.ylabel('Value (€)')
    plt.text(0.025, 0.85, 'Note: see more info by hovering on each data point',
            transform=ax.transAxes)

    plt.title('Investment development')
    fig.tight_layout()
    plt.show()

def format_coord(x, y):
    """
    Args:
        x: x-coordinate
        y: y-coordinate
    Returns:
        Each datapoint is formatted to have a specific corresponding text
    """
    return f"Year:⠀{int(x)}, Value(€):⠀{int(y)}"


def on_hover(s):
    """Sets the annotation color to correspond the line which the user hovers on

    Args:
        s: the point hovered on
    """
    point_color = s.artist.get_facecolor()
    s.annotation.set_bbox(dict(fc=point_color, alpha=0.8))
