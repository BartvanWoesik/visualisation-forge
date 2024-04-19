import os

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

from visualisation_forge.plots.base import Plots


class ROCPlot(Plots):
    """
    Class for creating and saving ROC plots.

    Args:
        y (array-like): True labels.
        pred_proba (array-like): Predicted probabilities.
        split_name (str): Name of the split.
        folder (str): Path to the folder where the plot will be saved.

    Attributes:
        y (array-like): True labels.
        pred_proba (array-like): Predicted probabilities.
        file_name (str): Name of the plot file.
        path (str): Path to the folder where the plot will be saved.
    """

    def __init__(self, **kwargs):
        self.y = kwargs.get("y")
        self.pred_proba = kwargs.get("pred_proba")
        self.file_name = kwargs.get("split_name") + "_roc_plot.png"
        self.path = kwargs.get("folder") + "/roc_auc/"

    def create_image(self):
        """
        Create the ROC plot.
        """
        fpr, tpr, _ = roc_curve(self.y, self.pred_proba[:, 1])
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
        """
        Save the ROC plot to a file.
        """
        os.makedirs(self.path, exist_ok=True)
        plt.savefig(self.path + self.file_name)
        plt.close()
