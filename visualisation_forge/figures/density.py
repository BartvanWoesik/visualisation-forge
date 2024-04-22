import os

import seaborn as sns
import matplotlib.pyplot as plt

from interfaces.plots import IPlots


class DensityPlot(IPlots):
    """
    Class for creating and saving a density plot of predicted probabilities.
    """

    def __init__(self, y, pred_proba, file_prefix: str = '',       folder_path: str = '', threshold: float = 0.5):
        self.y = [y]
        self.pred_proba = [pred_proba]
        self.file_name = f"{file_prefix}_density_plot.png"
        self.path = f"{folder_path}/"
        self.threshold = threshold

    def create_image(self):
        """
        Creates the density plot using seaborn.
        """
        # pred_1 = [
        #     x if y > self.threshold else 0
        #     for x, y in zip(self.pred_proba[:, 1], self.y)
        # ]
        # pred_1 = [x for x in pred_1 if x != 0]
        #
        # pred_0 = [
        #     x if y < self.threshold else 0
        #     for x, y in zip(self.pred_proba[:, 1], self.y)
        # ]
        # pred_0 = [x for x in pred_0 if x != 0]

        sns.kdeplot([x for x in self.pred_proba if x != 0], fill=True)
        sns.kdeplot([x for x in self.pred_proba if x != 1], fill=True)
        plt.xlabel("Probability")
        plt.ylabel("Density")
        plt.title("Density Plot of Predicted Probabilities")

    def write(self):
        """
        Writes the density plot to a file.
        """
        os.makedirs(name=self.path, exist_ok=True)
        plt.savefig(f"{self.path}{self.file_name}")
        plt.close()
