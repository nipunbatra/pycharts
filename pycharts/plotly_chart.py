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

    def line(self, x, ylist, df):
        x = df[x].values
        lines = {}
        for key, value in df[ylist].iteritems():
            lines[key] = {}
            lines[key]["x"] = x
            lines[key]["y"] = value.values
            lines[key]["name"] = key

        # Appending all lines
        lines_plotly = [lines[key] for key in df[ylist]]
        json_data = lines_plotly
        plotly_response = self.plotly.plot(json_data, verbose=False)
        url = plotly_response["url"]
        s = '<iframe height="650" id="igraph" scrolling="no" seamless="seamless" src="' + \
            url + '/900/600" width="900"></iframe>'
        return s

    def scatter(self, x, y, df):
        xdata = df[x].values
        ydata = df[y].values
        json_data = {"x": xdata, "y": ydata,
                     "type": "scatter", "mode": "markers"}
        json_data["text"] = df.index.values
        json_data["marker"] = {'size': 10, 'opacity': 0.55}
        layout = {
            'xaxis': {'title': x},
            'yaxis': {'title': y},
        }
        plotly_response = self.plotly.plot(
            json_data, layout=layout, verbose=False)
        url = plotly_response["url"]
        s = '<iframe height="650" id="igraph" scrolling="no" seamless="seamless" src="' + \
            url + '/900/600" width="900"></iframe>'
        return s
