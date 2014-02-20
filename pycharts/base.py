class BaseChart(object):

    def line(self, x, ylist, df):
        """Creates a line chart

        Parameters
        ----------
        x: string
            column name for x axis
        ylist: list
            list of column names for y axis
        df: pd.DataFrame
        """
        raise NotImplementedError
