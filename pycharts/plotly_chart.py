from base import BaseChart
import plotly


class PlotlyChart(BaseChart):

    def __init__(self, username, api):
        """Creates a plotly object

        Parameters
        -----------
        username: string
                plotly username
        api: string
                plotly api
        """
        super(PlotlyChart, self).__init__()
        self.plotly = plotly.plotly(username, api)

    def line(x, ylist, df):
        x = df.x
        lines = {}
        for key, value in df.iteritems():
            lines[key] = {}
            lines[key]["x"] = x
            lines[key]["y"] = value
            lines[key]["name"] = key

        # Appending all lines
        lines_plotly = [lines[key] for key in df]
        return lines_plotly
