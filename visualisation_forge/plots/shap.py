from visualisation_forge.plots.base import Plots

from random import randint
import shap
import os
import matplotlib.pyplot as plt


class ShapPlots(Plots):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.get("model")
        self.X = self.model.transform_without_predictor(kwargs.get("X")[:10_000])
        self.shap_values = self.create_shap_values()
        self.split_name = kwargs.get("split_name")
        self.path = kwargs.get("folder") + "/shap/"

    def create_image(self) -> None:
        pass

    def create_shap_values(self):
        explainer = shap.TreeExplainer(self.model[-1])
        return explainer(self.X)

    def create_shap_beeswarm(self, num_of_features: int = 10):
        _ = shap.plots.beeswarm(
            self.shap_values, max_display=num_of_features, show=False
        )
        self.write(path_extension="beeswarm/", name=self.split_name + "_beeswarm")

    def create_heatmap(self, show: bool = False):
        """
        Creates a heatmap plot using SHAP values.

        Parameters:
            show (bool): If True, the heatmap plot will be displayed. If False, the plot will be saved as "heatmap.png" in the current directory.
        """

        _ = shap.plots.heatmap(self.shap_values.sample(1000), show=False)
        self.write(path_extension="heatmap/", name=self.split_name + "_heatmap.png")

    def create_waterfall(self, show: bool = False):
        """
        Creates a waterfall plot using SHAP values.

        Parameters:
            show (bool): If True, the waterfall plot will be displayed. If False, the plot will be saved as "waterfall.png" in the current directory.
        """

        row = randint(0, len(self.shap_values) - 1)
        _ = shap.plots.waterfall(self.shap_values[row], show=False)
        self.write(path_extension="waterfall/", name=self.split_name + "_waterfall.png")

    def create_and_write(self):
        self.create_shap_beeswarm()
        self.create_waterfall()
        self.create_heatmap()

    def write(self, path_extension: str = "shap", name: str = "Plot"):
        """
        Helper function to handle saving or displaying the plot.

        Parameters:
            show (bool): If True, the plot will be displayed. If False, the plot will be saved.
            name (str): The name of the plot file.
        """
        full_path = self.path + path_extension
        os.makedirs(full_path, exist_ok=True)
        plt.title(name.split(".")[0])
        plt.savefig(full_path + name, bbox_inches="tight")
        plt.close()
