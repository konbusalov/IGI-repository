from services.series_func import SeriesFunction

def task3():
    series_function = SeriesFunction(x=3.14, eps=1e-9)

    series_function.plot_series_function()
    print(series_function.n)
