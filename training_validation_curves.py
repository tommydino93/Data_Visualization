import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

"""Suppose we trained a machine learning model and we saved the learning history;
we now want to plot the training and validation curves in the same image."""

train_accuracy = [.2, .45, .55, .60, .65, .68, .75, .80, .91, .92, .93, .94, .94, .94]  # type: list
val_accuracy = [.18, .40, .50, .55, .59, .65, .70, .75, .82, .83, .83, .84, .84, .84]  # type: list

train_loss = [.9, .65, .50, .42, .40, .37, .32, .3, .2, .16, .15, .14, .14, .14]  # type: list
val_loss = [.9, .7, .55, .46, .44, .41, .37, .35, .3, .24, .24, .24, .24, .26]  # type: list

# since the input vectors have same length, just use one of them to extract epochs
x_axis = np.arange(1, len(train_accuracy)+1, 1)  # type: np.ndarray

fig, ax1 = plt.subplots()  # create figure

color_1 = 'tab:blue'  # choose color
ax1.set_xlabel('Epochs')  # set label for x axis
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))  # only keep integers in x axis
ax1.set_ylabel('Dice')  # set label for y axis
ax1.plot(x_axis, train_accuracy, color=color_1, label='Train acc')  # plot train accuracy
ax1.plot(x_axis, val_accuracy, "--", color=color_1, label='Val acc')  # plot validation accuracy with dashed line
ax1.tick_params(axis='y', labelcolor=color_1)  # set color for ticks in y axis
ax1.set_ylim([0, 1])  # set upper and lower bound for y-axis ticks

ax2 = ax1.twinx()  # share x axis between the two subplots
color_2 = 'tab:red'  # choose another color
ax2.set_ylabel("Loss")  # set label for y axis
ax2.plot(x_axis, train_loss, color=color_2, label='Train loss')  # plot train loss
ax2.plot(x_axis, val_loss, "--", color=color_2, label='Val loss')  # plot validation loss with dashed line
ax2.tick_params(axis='y', labelcolor=color_2)  # set color for ticks in new y axis
ax2.set_ylim([0, 1])  # set upper and lower bound for y-axis ticks
fig.suptitle('Train/Val Curves', fontsize=16, fontweight='bold'), fig.legend(loc="lower left")
plt.show()
