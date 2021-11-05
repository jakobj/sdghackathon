import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    start_year = 2008
    end_year = 2022

    n = (end_year - start_year) * 12
    time = np.arange(n)
    sdg_spending = 10 + 0.05 * time + 0.3 * np.random.randn(n)
    total_spending = 40 + 0.04 * time + 0.2 * np.random.randn(n)
    index = 10 * (40 + 0.04 * time + 0.2 * np.random.randn(n))
    measure = 10 - 0.05 * time + 0.3 * np.random.randn(n)

    fig = plt.figure(figsize=(6, 6 / 1.618))
    ax_positive = fig.add_axes([0.05, 0.5, 0.85, 0.4])
    ax_negative = fig.add_axes([0.05, 0.1, 0.85, 0.4])

    ax_positive.yaxis.set_label_position("right")
    ax_positive.yaxis.tick_right()
    ax_positive.spines['left'].set_visible(False)
    ax_positive.spines['top'].set_visible(False)
    ax_positive.set_ylim([0, 50])

    ax_negative.patch.set_alpha(0.0)
    ax_negative.yaxis.tick_right()
    ax_negative.set_xticks([])
    ax_negative.spines['left'].set_visible(False)
    ax_negative.spines['bottom'].set_visible(False)
    ax_negative.set_ylim([0, 25])

    offset = 0
    ax_positive.fill_between(time, offset, offset + sdg_spending)
    offset += sdg_spending
    ax_positive.fill_between(time, offset, total_spending)

    ax_negative.plot(time, measure)

    fig.savefig('plot.pdf')
