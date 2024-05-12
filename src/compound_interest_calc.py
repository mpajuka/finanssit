import locale
from decimal import getcontext
from matplotlib.ticker import ScalarFormatter
import mplcursors
import matplotlib.pyplot as plt
getcontext().prec = 2
locale.setlocale(locale.LC_ALL, '')


def format_input(curr_value: int, cont: int, r: int, t: int, is_test=None):
    """formats the input for the investment calculator

    Args:
        curr_value (int): current_value from the tkinter Scale
        cont (int): monthly contribution from the tkinter Scale
        r (int): return for investment from the tkinter Scale
        t (int): _description_
        is_test (bool, optional): 
            variable to determine if a plot is formed, if true only the future value is returned.
            Defaults to None in normal execution.

    Returns:
        int: 
            the future value for the investments after the input time period and possible returns
    """
    flt_curr_value = float(curr_value)
    flt_cont = float(cont)
    flt_r = float(r)

    if not is_test:
        fut_value = calculate_investments(flt_curr_value, flt_cont, flt_r, t)
    else:
        fut_value = calculate_investments(
            flt_curr_value, flt_cont, flt_r, t, is_test)
    return fut_value


def calculate_investments(curr_value: float, cont: float, return_pa: float,
                          time_in_years: int, is_test=None):
    """Calculate the development of investment based on the initial invested sum,
    the possible monthly contribution, user determined estimated return, and the
    time horizon for which the funds are aimed to be invested for. After the
    calculations have been formed a matplotlib figure is formed of the data,


    Args:
        curr_value (float): Current (€) value of invested funds
        cont (float): Possible monthly contribution added to the investments (€)
        return_pa (float): Estimated percentage of yearly returs (% p.a.)
        time_in_years (int): Time horizon in years
        is_test (bool, optional): 
            variable to determine if a plot is formed, if true only the future value is returned.
            Defaults to None in normal execution.  
    Returns:
        int: 
            the future value for the investments after the input time period and possible returns
    """
    regular_contributions = 0
    total_current_contributions = curr_value
    y = []
    y_int = []
    all_contributions = []
    for i in range(1, time_in_years+1):
        year_of_monthly_contributions = cont*12
        return_as_float = return_pa/100

        temp = regular_contributions * (1 + return_as_float)
        regular_contributions = temp + year_of_monthly_contributions

        future_value = curr_value * \
            (1 + return_as_float) ** i + regular_contributions

        y.append(f"{future_value:0.2f}")
        y_int.append((int(float(f"{future_value:0.2f}"))))

        total_current_contributions += year_of_monthly_contributions
        all_contributions.append(total_current_contributions)

    form_plot(y_int, all_contributions, list(
        range(1, int(time_in_years)+1)), is_test)
    return future_value


def form_plot(y_int, all_contributions, x, is_test):
    """Forms the matplotlib figure from the data calculated with possible returns
    initial investment and monthly contributions, for each yearly point. A trend line
    is then formed which contains the datapoints which have annotations display additional
    information when hovered on.

    Args:
        y_int (list): y-axis values appended as integers
        all_contributions (list): investments value at each year
        t (string): the time horizon in years
    """
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

    plt.xlabel('Years (After initial investment)')
    plt.ylabel('Value (€)')
    plt.text(0.025, 0.85, 'Note: see more info by hovering on each data point',
             transform=ax.transAxes)

    plt.title('Investment development')
    fig.tight_layout()
    if not is_test:
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
    s.annotation.set_bbox({"fc": point_color, "alpha": 0.8})
