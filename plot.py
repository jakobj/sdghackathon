import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from scipy.interpolate import splrep, splev


def smooth_curve(x, y, s=5):
    bspl = splrep(x, y, s=s)
    bspl_y = splev(x, bspl)
    return bspl_y


if __name__ == '__main__':

    start_year = 2008
    end_year = 2022

    n_years = end_year - start_year
    n_months = n_years * 12
    time_years = np.arange(n_years)
    time_months = np.arange(n_months)
    sdg_spending = 10 + 0.05 * time_months + 0.3 * np.random.randn(n_months)
    total_spending = 40 + 0.04 * time_months + 0.2 * np.random.randn(n_months)
    index = 10 * (40 + 0.04 * time_months + 0.2 * np.random.randn(n_months))
    measure_one = 30 - 2.05 * time_years + 0.4 * np.random.randn(n_years)
    measure_two = 10 + 1.45 * time_years + 0.8 * np.random.randn(n_years)
    measure_three = 20 - 1.05 * time_years + 0.4 * np.random.randn(n_years)
    measure_four = 1 + 3.45 * time_years + 0.8 * np.random.randn(n_years)

    tick_every_x_year = 2
    ticks_months = np.arange(0, n_months + 1, tick_every_x_year * 12)
    tickslabels_years = np.arange(start_year, end_year + 1, tick_every_x_year)

    fig = plt.figure(figsize=(6, 6 / 1.618))
    ax_positive = fig.add_axes([0.05, 0.5, 0.85, 0.4])
    ax_negative = fig.add_axes([0.05, 0.1, 0.85, 0.4])

    ax_positive.yaxis.set_label_position("right")
    ax_positive.yaxis.tick_right()
    ax_positive.spines['left'].set_visible(False)
    ax_positive.spines['top'].set_visible(False)
    ax_positive.set_xlim([0, n_months])
    ax_positive.set_ylim([0, 50])
    ax_positive.set_xticks(ticks_months)
    ax_positive.set_xticklabels(tickslabels_years)

    ax_negative.patch.set_alpha(0.0)
    ax_negative.yaxis.tick_right()
    ax_negative.set_xticks([])
    ax_negative.set_yticks([])
    ax_negative.spines['right'].set_visible(False)
    ax_negative.spines['left'].set_visible(False)
    ax_negative.spines['bottom'].set_visible(False)
    ax_negative.set_xlim([0, n_months])
    ax_negative.set_ylim([-5, 10])

    offset = 0
    ax_positive.fill_between(time_months, offset, offset + sdg_spending)
    offset += sdg_spending
    ax_positive.fill_between(time_months, offset, total_spending)

    scale = 1.0
    for year_idx in range(n_years):
        ax_negative.plot()
        ax_negative.add_patch(Rectangle(((year_idx + 0.5) * 12, 0), -scale * math.sqrt(measure_one[year_idx]), scale * math.sqrt(measure_one[year_idx]), facecolor='C2'))
        ax_negative.add_patch(Rectangle(((year_idx + 0.5) * 12, 0),  scale * math.sqrt(measure_two[year_idx]), scale * math.sqrt(measure_two[year_idx]), facecolor='C3'))
        ax_negative.add_patch(Rectangle(((year_idx + 0.5) * 12, 0), -scale * math.sqrt(measure_three[year_idx]), -scale * math.sqrt(measure_three[year_idx]), facecolor='C4'))
        ax_negative.add_patch(Rectangle(((year_idx + 0.5) * 12, 0),  scale * math.sqrt(measure_four[year_idx]), -scale * math.sqrt(measure_four[year_idx]), facecolor='C5'))

    fig.savefig('plot.pdf')
