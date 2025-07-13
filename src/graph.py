import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.patches import FancyBboxPatch

def plot_language_usage(
    start, end, time_spent, language_data, filename="lang_stats.svg"
):
    label_color = "#757A7F"       # Y-axis language names
    annotation_color = "#757A7F"  # Text at bar end
    title_color = "#757A7F"       # Title color

    df = pd.DataFrame(language_data, columns=["Language", "Percent", "Label"])
    df = df.sort_values("Percent", ascending=False).reset_index(drop=True)

    colors = sns.color_palette("tab10", len(df)) 

    sns.set_theme(style="white")
    sns.set_color_codes("pastel")

    fig, ax = plt.subplots(figsize=(7, 3))

    barplot = sns.barplot(
        data=df,
        x="Percent",
        y="Language",
        ax=ax,
        palette=colors
    )

    new_patches = []
    for i, patch in enumerate(reversed(ax.patches)):
        bb = patch.get_bbox()
        p_bbox = FancyBboxPatch(
            (bb.xmin, bb.ymin),
            abs(bb.width), abs(bb.height),
            boxstyle="round,pad=-0.004,rounding_size=2",
            ec="none", fc=colors[len(df) - 1 - i],
            mutation_aspect=0.2
        )
        patch.remove()
        new_patches.append(p_bbox)

    for patch in new_patches:
        ax.add_patch(patch)

    for i, (percent, label) in enumerate(zip(df["Percent"], df["Label"])):
        ax.text(
            percent + 1,
            i,
            f"{label} ({percent:.2f}%)",
            va="center",
            fontsize=13,
            color=annotation_color
        )

    for label in ax.get_yticklabels():
        label.set_color(label_color)
        label.set_fontsize(13)

    ax.set_title(
        f"Languages : {start} → {end}  -  {time_spent}",
        color=title_color,
        fontsize=14
    )

    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks([])
    ax.tick_params(axis='both', which='both', length=0)
    sns.despine(left=True, bottom=True)

    plt.tight_layout()
    plt.savefig(filename, transparent=True)
    plt.close()
