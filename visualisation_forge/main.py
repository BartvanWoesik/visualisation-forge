from plots.base import Plots


class Make:
    """
    Class to loop over _implementations of IPlots, create plots, and write them to a designated folder
    """

    @staticmethod
    def make_and_write_plots(output_folder):
        """
        Stuff we could get:
            - y
             - pred
             - pred_proba
             -




        """
        for _, plot_func in Plots._implementations.items():
            try:
                pred = {
                    "test": [0.2, 0.4, 0.6, 0.8, 0.3],
                    "train": [0.1, 0.3, 0.5, 0.7, 0.2, 0.8, 0.8],
                }
                pred_proba = {
                    "test": [0.2, 0.4, 0.6, 0.8, 0.3],
                    "train": [0.1, 0.3, 0.5, 0.7, 0.2, 0.8, 0.8],
                }
                y = {"test": [1, 0, 1, 0, 1], "train": [1, 1, 1, 0, 1, 0, 0]}
                path = output_folder
                for split in pred.keys():
                    plot_instance = plot_func(
                        pred=pred[split],
                        y=y[split],
                        pred_proba=pred_proba[split],
                        path=path,
                        split=split,
                    )
                    plot_instance.create_and_write()

                print(
                    f"{plot_instance.__class__.__name__} plot is created and written to {output_folder}"
                )
            except Exception as e:
                print(
                    f"Failed to create or write {plot_instance.__class__.__name__} plot: {str(e)}"
                )
                # Print stack trace if needed: print(traceback.format_exc())


if __name__ == "__main__":
    Make.make_and_write_plots(output_folder="ims")
