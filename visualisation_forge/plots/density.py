import os

import seaborn as sns
import matplotlib.pyplot as plt

from visualisation_forge.plots.base import Plots


class DensityPlot(Plots):
    """
    Class for creating and saving a density plot of predicted probabilities.
    """

    def __init__(self, **kwargs):
        self.y = kwargs.get("y")
        self.pred_proba = kwargs.get("pred_proba")
        self.file_name = kwargs.get("split_name") + "_density_plot.png"
        self.path = kwargs.get("folder") + "/density/"
        self.threshold = 0.5

    def create_image(self):
        """
        Creates the density plot using seaborn.
        """
        pred_1 = [
            x if y > self.threshold else 0
            for x, y in zip(self.pred_proba[:, 1], self.y)
        ]
        pred_1 = [x for x in pred_1 if x != 0]

        pred_0 = [
            x if y < self.threshold else 0
            for x, y in zip(self.pred_proba[:, 1], self.y)
        ]
        pred_0 = [x for x in pred_0 if x != 0]

        sns.kdeplot(pred_0, fill=True)
        sns.kdeplot(pred_1, fill=True)
        plt.xlabel("Probability")
        plt.ylabel("Density")
        plt.title("Density Plot of Predicted Probabilities")

    def write(self):
        """
        Writes the density plot to a file.
        """
        os.makedirs(self.path, exist_ok=True)
        plt.savefig(self.path + self.file_name)
        plt.close()
