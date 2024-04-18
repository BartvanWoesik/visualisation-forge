from visualisation_forge.plots.base import Plots


class MakePlots:
    """
    Class to loop over _implementations of IPlots, create plots, and write them to a designated folder
    """

    @staticmethod
    def make_and_write_plots(folder, X, y, pred, pred_proba, split_name):
        """
        Stuff we could get:
            - y
             - pred
             - pred_proba
             -




        """
        print("Creating and writing plots...")
        for _, plot_func in Plots._implementations.items():
            try:
                plot_instance = plot_func(
                    folder=folder,
                    pred=pred,
                    X=X,
                    y=y,
                    pred_proba=pred_proba,
                    split_name=split_name,
                )
                plot_instance.create_and_write()

                print(f"{plot_instance.__class__.__name__} plot is created.")
            except Exception as e:
                print(
                    f"Failed to create or write {plot_instance.__class__.__name__} plot: {str(e)}"
                )
                # Print stack trace if needed: print(traceback.format_exc())


if __name__ == "__main__":
    MakePlots.make_and_write_plots(output_folder="ims")
