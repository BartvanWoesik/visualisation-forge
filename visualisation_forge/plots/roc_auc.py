import os

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

from visualisation_forge.plots.base import Plots


class ROCPlot(Plots):
    def __init__(self, **kwargs):
        self.y = kwargs.get("y")
        self.pred = kwargs.get("pred")
        self.file_name = kwargs.get("split_name") + "_roc_plot.png"
        self.path = "ims/roc"

    def create_and_write(self):
        self.create_image()
        self.write()

    def create_image(self):
        fpr, tpr, _ = roc_curve(self.y, self.pred)
        roc_auc = auc(fpr, tpr)

        plt.figure()
        plt.plot(
            fpr,
            tpr,
            color="darkorange",
            lw=2,
            label="ROC curve (area = %0.2f)" % roc_auc,
        )
        plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("Receiver Operating Characteristic")
        plt.legend(loc="lower right")

    def write(self):
        os.makedirs(self.path, exist_ok=True)
        plt.savefig(self.path + "/" + self.file_name)
        plt.close()
