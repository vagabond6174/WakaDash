import matplotlib.pyplot as plt


def plot_language_usage(
    start, end, time_spent, language_data, filename="lang_stats.svg"
):
    text_color = "#757A7F"
    annotation_color = "#757A7F"

    langs, percents, labels = zip(*language_data)

    cmap = plt.get_cmap("tab10")
    colors = [cmap(i % cmap.N) for i in range(len(langs))]

    fig, ax = plt.subplots(figsize=(6, 3))
    y_pos = range(len(langs))

    bars = ax.barh(y_pos, percents, color=colors)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(langs, color=text_color, fontdict= {'fontsize' : 13})
    ax.invert_yaxis()
    ax.set_title(
        f"Languages : {start} → {end}  -  {time_spent}",
        color=text_color,
        fontdict={"fontsize": 13},
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlabel("")
    ax.set_xticks([])
    ax.tick_params(left=False)

    for i, bar in enumerate(bars):
        ax.text(
            bar.get_width() + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{labels[i]} ({percents[i]:.2f}%)",
            va="center",
            fontsize=12,
            color=annotation_color,
        )

    plt.tight_layout()
    plt.savefig(filename, transparent=True)
    plt.close()
