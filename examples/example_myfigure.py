# %%
import pathlib as plib
import numpy as np
import pandas as pd
from myfigure.myfigure import MyFigure, colors, linestyles, markers, hatches

out_path = plib.Path("/Users/matteo/Projects/myfigure/examples/output")

x0 = np.linspace(0, 100, 10)
y0 = np.random.random(10)
y1 = np.random.random(10)

f0 = MyFigure(filename="f0", out_path=out_path)
f0.save_figure()

f1 = MyFigure(filename="f1", out_path=out_path)
f1.axs[0].plot(x0, y0, color=colors[5], linestyle=linestyles[1])
f1.axs[0].scatter(x0, y1, color=colors[1], marker=markers[2])
f1.save_figure()

f2 = MyFigure(filename="f2", out_path=out_path, twinx=True)
f2.axs[0].plot(x0, y0, label="y0")
f2.axts[0].plot(x0, y1, label="y1", color=colors[1])
f2.save_figure()

# %%
f3 = MyFigure(filename="f3", out_path=out_path, rows=2, width=4)
f3.axs[0].plot(x0, y0, color=colors[5], linestyle=linestyles[1])
f3.axs[1].scatter(x0, y1, color=colors[1], marker=markers[2])
f3.save_figure()

# %%
f4 = MyFigure(filename="f4", out_path=out_path, twinx=True, rows=2, width=4)
f4.axs[0].plot(x0, y0, color=colors[0], linestyle=linestyles[0], label="y0")
f4.axts[0].plot(x0, y1, color=colors[1], linestyle=linestyles[1], label="y1")
f4.axs[1].scatter(x0, y0, color=colors[0], marker=markers[0], label="y0")
f4.axts[1].scatter(x0, y1, color=colors[1], marker=markers[1], label="y1")
f4.save_figure()
# %%
f5 = MyFigure(
    filename="f5",
    out_path=out_path,
    rows=2,
    width=4,
    height=8,
    x_lab=r"x_lab$\int^1_2$",
    y_lab=["y_lab", r"y_lab$\int^1_2$"],
    x_lim=[0, 90],
    y_lim=[[0, 0.9], [0, 0.5]],
    x_ticks=[[0, 40, 80], [0, 20, 40, 50, 90]],
    y_ticks=[0, 0.40, 0.50],
    legend=False,
)
f5.axs[0].plot(x0, y0, color=colors[5], linestyle=linestyles[1])
f5.axs[1].scatter(x0, y1, color=colors[1], marker=markers[2])
f5.save_figure()
# %%
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
    x_lim=[0, 90],
    y_lim=[[0, 0.9], [0, 0.5]],
    x_ticks=[[0, 40, 80], [0, 20, 40, 50, 90]],
    y_ticks=[0, 0.40, 0.50],
)
f6.axs[0].plot(x0, y0, color=colors[0], linestyle=linestyles[0], label="1")
f6.axs[0].plot(x0, y0 * y1, color=colors[4], linestyle=linestyles[4], label="5")
f6.axs[1].scatter(x0, y1, color=colors[1], marker=markers[1], label="2")
f6.axts[0].plot(x0, y1, color=colors[2], linestyle=linestyles[2], label="3")
f6.axts[1].scatter(x0, y0, color=colors[3], marker=markers[3], label="4")
f6.save_figure()
# %%

df_ave = pd.DataFrame(data=np.random.random((5, 5)))
df_std = pd.DataFrame(data=np.random.random((5, 5)) * np.random.random((5, 5)))

f1 = MyFigure(filename="f1", out_path=out_path, masked_unsignificant_data=True)
df_ave.plot(ax=f1.axs[0], kind="bar", yerr=df_std, capsize=2)
f1.save_figure()


# %%
# f0.save_figure()
# f = MyFigure(
#     filename="my_plot",
#     rows=1,
#     cols=1,
#     width=6,
#     #     height=12,
#     twinx=True,
#     #     x_lab=["aaa", "qqq", "aa", "qq"],
#     #     y_lab="bbb",
#     #     yt_lab="ccc",
#     #     x_lim=[0, 1],
#     y_lim=[0, 1],
#     #     yt_lim=[[0, 1], [0, 0.5], [0, 1], [0, 0.5]],
#     #     x_ticks=[[0, 0.5, 1], [0, 0.5, 2], [0, 1], [0, 0.5]],
#     #     # x_ticklabels=["a", "c", "d"],
#     #     grid=True,
#     #     annotate_lttrs=["a", "b", "a", "b"],
#     #     annotate_lttrs_xy=[-0.11, -0.15],
#     #     x_ticklabels_rotation=0,
#     annotate_outliers=True,
# )
# f.axs[0].bar(["A", "B", "C"], [10, 20, 30], yerr=[1, 2, 3])
# # f.axs[0].plot([0, 1], [0, 3], label="a")
# # f.axts[0].plot([0, 2], [0, 4], label="b")
# # f.axts[0].plot([0, 2], [0, 5], label="ccc")
# # f.axs[1].plot([0, 1], [0, 3], label="aaa")

# # f.annotate_outliers_in_ax()

# # ins = f.create_inset(f.axs[0], [0.6, 0.8], [0.4, 0.6], [0, 0.2], [0, 0.2])
# # ins.plot([0, 1], [0, 3], label="a")
# f.save_figure()
# %%
