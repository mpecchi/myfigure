# %%
import pathlib as plib
import numpy as np
import pandas as pd
from myfigure.myfigure import MyFigure, create_inset, colors, linestyles, markers, hatches, letters


# Define the output path for saving figures
out_path = plib.Path(__file__).resolve().parent / "output"

out_path = plib.Path("/Users/matteo/Projects/myfigure/examples/output")

# create some random data for plotting
x0 = np.linspace(0, 10, 10)
y0 = np.linspace(0, 10, 10)
y1 = np.linspace(15, 5, 10)

# %%
# Create a MyFigure instance and save it with default settings
f0 = MyFigure(filename="f0", out_path=out_path)
f0.save_figure()

# %%
# Create another MyFigure instance, plot line and scatter plot, then save
f1 = MyFigure(filename="f1", out_path=out_path)
f1.axs[0].plot(x0, y0, color=colors[5], linestyle=linestyles[1])
f1.axs[0].scatter(x0, y1, color=colors[1], marker=markers[2])
f1.save_figure()
# %%
# Create a figure with twin axes, plot on both, and save the figure
f2 = MyFigure(filename="f2", out_path=out_path, twinx=True, legend_loc="lower center")
f2.axs[0].plot(x0, y0, label="y0")
f2.axts[0].plot(x0, y1, label="y1", color=colors[1])
f2.save_figure()

# %%
# Create a figure with two rows and custom labels, then save it
f3 = MyFigure(filename="f3", out_path=out_path, rows=2, width=4, x_lab=["aaa", "bbb"])
f3.axs[0].plot(x0, y0, color=colors[5], linestyle=linestyles[1], label="1")
f3.axs[0].scatter(x0, y1, color=colors[1], marker=markers[2], label="2")
f3.axs[1].plot(x0, y0, color=colors[5], linestyle=linestyles[1], label="1")
f3.axs[1].scatter(x0, y1, color=colors[1], marker=markers[2], label="2")
f3.save_figure()

# %%
# Create a figure with twin axes on two rows, apply LaTeX labels, and save
f4 = MyFigure(
    filename="f4",
    out_path=out_path,
    twinx=True,
    rows=2,
    width=4,
    x_lab=r"x_lab$\int^1_2$",
    y_lab=r"y_lab$\int^1_2$",
    yt_lab=r"y_lab$\int^1_2$",
    x_lim=[0, 10],
    legend_loc="upper center",
)
f4.axs[0].plot(x0, y0, color=colors[0], linestyle=linestyles[0], label="y0")
f4.axts[0].plot(x0, y1, color=colors[1], linestyle=linestyles[1], label="y1")
f4.axs[1].scatter(x0, y0, color=colors[0], marker=markers[0], label="y0")
f4.axts[1].scatter(x0, y1, color=colors[1], marker=markers[1], label="y1")
f4.save_figure()
# %%
# Create a figure with custom axes limits and tick settings, then save
f5 = MyFigure(
    filename="f5",
    out_path=out_path,
    rows=2,
    width=4,
    height=8,
    x_lab=["x_lab", r"x_lab$\int^1_2$"],
    y_lab=["y_lab", r"y_lab$\int^1_2$"],
    x_lim=[[0, 9], [0, 10]],
    # y_lim=[[0, 0.9], [0, 0.5]],
    x_ticks=[[0, 40, 80], [0, 20, 40, 50, 90]],
    y_ticks=[0, 0.40, 0.50],
    legend=False,
)
f5.axs[0].plot(x0, y0, color=colors[5], linestyle=linestyles[1])
f5.axs[1].scatter(x0, y1, color=colors[1], marker=markers[2])
f5.save_figure()
# %%
# More complex example with twinx, multiple rows, and extensive customization
f6 = MyFigure(
    filename="f6",
    out_path=out_path,
    twinx=True,
    rows=2,
    width=5,
    height=8,
    x_lab=r"x_lab$\int^1_2$",
    yt_lab=["yt_lab", r"yt_lab$\int^1_2$"],
    y_lab=["y_lab", r"y_lab$\int^1_2$"],
    x_lim=[0, 9],
    y_lim=[[0, 0.9], [0, 0.5]],
    x_ticks=[[0, 4, 8], [0, 2, 4, 5, 9]],
    y_ticks=[0, 40, 50],
    yt_ticks=[[0, 10, 14], [0, 4, 10]],
)
f6.axs[0].plot(x0, y0, color=colors[0], linestyle=linestyles[0], label="1")
f6.axs[0].plot(x0, y0 * y1, color=colors[4], linestyle=linestyles[4], label="5")
f6.axs[1].scatter(x0, y1, color=colors[1], marker=markers[1], label="2")
f6.axts[0].plot(x0, y1, color=colors[2], linestyle=linestyles[2], label="3")
f6.axts[1].scatter(x0, y0, color=colors[3], marker=markers[3], label="4")
f6.save_figure()
# %%
# create additional random dataframe for plotting
df_ave = pd.DataFrame(data=[[1, 2, 3, 4, 5], [6, 5, 4, 3, 2]], columns=["1", "2", "3", "4", "5a"])
df_std = pd.DataFrame(
    data=[[0.1, 0.2, 0.3, 0.4, 0.5], [0.6, 0.65, 0.4, 0.3, 0.2]], columns=["1", "2", "3", "4", "5a"]
)
# %%
# Create a figure to display bar plots with error bars, specific outlier annotations, and save
f7 = MyFigure(
    filename="f7",
    out_path=out_path,
    width=4,
    height=4,
    annotate_outliers=True,
    annotate_outliers_decimal_places=1,
    # auto_apply_hatches_to_bars=False,
    y_lim=[0, 5.5],
)
df_ave.plot(ax=f7.axs[0], kind="bar", yerr=df_std, capsize=2, edgecolor="k")
f7.save_figure()
# %%
# as f7 but with only 1 decimal place in annotate ouliers
f7b = MyFigure(
    filename="f7b",
    out_path=out_path,
    annotate_outliers=True,
    annotate_outliers_decimal_places=1,
    y_lim=[0, 3],
)
df_ave.plot(ax=f7.axs[0], kind="bar", yerr=df_std, capsize=2)
f7b.save_figure()
# %%
# Create a figure to display inverted bar plots with annotations for outliers and save
f8 = MyFigure(
    filename="f8",
    out_path=out_path,
    auto_apply_hatches_to_bars=False,
    annotate_outliers=True,
    y_lim=[-3, 0],
)
df_ave.mul(-1).plot(ax=f8.axs[0], kind="bar", yerr=df_std, capsize=2)
f8.save_figure()
# %%
# Create a figure with twin axes to display separate bar and line plots and save
f9 = MyFigure(
    filename="f9",
    out_path=out_path,
    twinx=True,
    auto_apply_hatches_to_bars=True,
)
df_ave[["1", "2"]].plot(ax=f9.axts[0], kind="bar", yerr=df_std, capsize=2, legend=False)
df_ave[["3", "4"]].plot(ax=f9.axs[0], kind="line", yerr=df_std, capsize=2, color=colors[3:5])
f9.save_figure()
# %%
# additional random data
df_ave = pd.DataFrame(
    data=[[1, 2, 3, 4, 5], [6, 5, 4, 3, 2]], columns=["1", "2", "3", "4", "5a"], index=["i1", "i2"]
)
df_std = pd.DataFrame(
    data=[[0.1, 0.2, 0.3, 0.4, 2.5], [0.7, 0.5, 0.4, 0.3, 0.2]],
    columns=["1", "2", "3", "4", "5a"],
    index=["i1", "i2"],
)
# Create a figure to display a bar plot with error bars and outlier annotations, with specific y-axis limits
f10 = MyFigure(
    filename="f10",
    out_path=out_path,
    annotate_outliers=True,
    annotate_outliers_decimal_places=1,
    y_lim=[0, 4],
)
df_ave.plot(ax=f10.axs[0], kind="bar", yerr=df_std, capsize=2, legend=False)
f10.save_figure()

# %%
# Create a figure with twin axes and multiple rows for plotting complex data and save

f11 = MyFigure(
    filename="f11",
    out_path=out_path,
    twinx=True,
    rows=2,
    width=4,
    annotate_letters=letters[:2],
)
f11.axs[0].plot(x0, y0, color=colors[0], linestyle=linestyles[0], label="y0")
f11.axts[0].plot(x0, y1, color=colors[1], linestyle=linestyles[1], label="y1")
f11.axs[1].scatter(x0, y0, color=colors[0], marker=markers[0], label="y0")
f11.axts[1].scatter(x0, y1, color=colors[1], marker=markers[1], label="y1")
f11.save_figure()

# %%
# %%

df_ave = pd.DataFrame(data=[[1, 2, 3, 4], [6, 5, 4, 3], [3, 5, 4, 6]], columns=["1", "2", "3", "4"])
df_std = pd.DataFrame(
    data=[[1.1, 0.2, 3.3, 0.4], [0.6, 5.65, 0.4, 0.3], [1.3, 4, 5, 7]], columns=["1", "2", "3", "4"]
)
# Create a figure that automatically masks insignificant data and save
f12 = MyFigure(
    filename="f12",
    out_path=out_path,
    annotate_outliers=True,
    annotate_outliers_decimal_places=1,
    # y_lim=[0, 0.3],
    mask_insignificant_data=True,
    mask_insignificant_data_alpha=0.1,
)
df_ave.plot(ax=f12.axs[0], kind="bar", yerr=df_std, capsize=2)
f12.save_figure()
# %%
# add an inset to the plot
f13 = MyFigure(filename="f13", out_path=out_path)
f13.axs[0].plot(x0, y0, color=colors[5], linestyle=linestyles[1])
f13.axs[0].scatter(x0, y1, color=colors[1], marker=markers[2])
ins = create_inset(f13.axs[0], x_loc=(0.1, 0.4), y_loc=(0.35, 0.65), x_lim=(5, 7), y_lim=(4, 10))
ins.plot(x0, y0, color=colors[5], linestyle=linestyles[1])
ins.scatter(x0, y1, color=colors[1], marker=markers[2])
f13.save_figure()
