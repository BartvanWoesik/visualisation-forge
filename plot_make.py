from visualisation_forge.make_plots import MakePlots

if __name__ == "__main__":
    x = [1, 1, 2]
    y = [0, 0, 1]

    test = MakePlots(plot_config_path="plot_config.yaml", x=x, y=y, model=any)
    test.make()
