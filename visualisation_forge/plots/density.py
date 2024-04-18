import os

import seaborn as sns
import matplotlib.pyplot as plt

from visualisation_forge.plots.base import Plots


class DensityPlot(Plots):
    def __init__(self, **kwargs):
        self.y = kwargs.get("y")
        self.pred = kwargs.get("pred")
        self.file_name = kwargs.get("split_name") + "_density_plot.png"
        self.path = "ims/density"
        self.threshold = 0.5

    def create_and_write(self):
        self.create_image()
        self.write()

    def create_image(self):
        pred_1 = [x if y > self.threshold else 0 for x, y in zip(self.pred, self.y)]
        pred_1 = [x for x in pred_1 if x != 0]

        pred_0 = [x if y < self.threshold else 0 for x, y in zip(self.pred, self.y)]
        pred_0 = [x for x in pred_0 if x != 0]

        # Create a density plot using seaborn
        sns.kdeplot(pred_0, fill=True)
        sns.kdeplot(pred_1, fill=True)
        plt.xlabel("Probability")
        plt.ylabel("Density")
        plt.title("Density Plot of Predicted Probabilities")

    def write(self):
        os.makedirs(self.path, exist_ok=True)
        plt.savefig(self.path + "/" + self.file_name)
        plt.close()
