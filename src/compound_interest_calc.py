import locale
from decimal import *
from matplotlib.ticker import ScalarFormatter
import mplcursors
import matplotlib.pyplot as plt
getcontext().prec = 2
locale.setlocale(locale.LC_ALL, '')


def calculate_investments(curr_value, contribution, est_return, time):
    pv = int(curr_value.get())
    cont = contribution.get()
    r = est_return.get()
    t = time.get()

    pmt = 0
    contributions = pv
    y = []
    y_int = []
    all_contributions = []
    for i in range(1, int(t)+1):
        p = float(pv)
        ctr = float(cont)*12
        rt = float(r)/100
        temp_pmt = pmt * (1+rt)
        pmt = temp_pmt + ctr
        fv = p*(1+rt)**i + pmt
        futvalue = "{:0.2f}".format(fv)
        y.append(futvalue)
        y_int.append((int(float(futvalue))))
        contributions += ctr
        all_contributions.append(contributions)

    x = list(range(1, int(t)+1))
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.plot(x, y_int, color='#85BB65')
    ax.plot(x, all_contributions, color='orange')
    data1 = ax.scatter(x, y_int, s=50, color='#85BB65',
                       label='Invested funds + value development')

    data2 = ax.scatter(x, all_contributions, s=50,
                       color='orange', label='Invested funds')
    plt.xticks(range(min(x), max(x)+1))
    # ax.set_yticks(y_int)
    ax.ticklabel_format(useOffset=False)
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.format_coord = format_coord
    ax.ticklabel_format(style='plain')

    plt.legend(loc='upper left')

    cursor = mplcursors.cursor({data1, data2}, hover=True)

    cursor = mplcursors.cursor({data1, data2}, hover=True)

    cursor.connect("add", on_hover)

    plt.xlabel('Years')
    plt.ylabel('Value (€)')
    plt.text(0.025, 0.85, 'Note: see more info by hovering on each data point',
            transform=ax.transAxes)

    plt.title('Investment development')
    fig.tight_layout()

    return fig, ax


def format_coord(x, y):
    # output numbers (not in scientific notation) with one decimal place
    return f"Year:⠀{int(x)}, Value(€):⠀{int(y)}"


def on_hover(s):
    # Get the color of the point being hovered over
    point_color = s.artist.get_facecolor()
    s.annotation.set_bbox(dict(fc=point_color, alpha=0.8))
