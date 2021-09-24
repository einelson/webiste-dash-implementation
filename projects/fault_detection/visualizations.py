'''
Visualizations.py
Overview:
    This file will be for visualizing data. This will
    be used to better understand the data, get a better understanding of how to
    visualize and manipulate the data.

Classes:
    visual()- contains the df as well as the visuals

Functions:
    __init__()- this will initalize the df to what the user inputs
    open_csv()- This will be used to import the selected csv file
    z_score()- Will calculate the distributions for every sensor column
    heat_map()- Creats and displays a correlation heat map of the data
    time_series_visualization()- Creates a time series graph that is displayed
    histogram()- will show a histogram of the sensor data

TODO:
    I need to apply darkly css styling to these graphs
'''


'''
Import the libraries used in this file
'''
# general
import os

# data manipulation
import pandas as pd
import numpy as np

# distribution
from sklearn.preprocessing import StandardScaler

# visualization
import plotly.express as px
import plotly.graph_objects as go
# import plotly.figure_factory as ff

from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA



'''
VISUAL
Contains the functions needed to create diffrent visuals
'''
class Visuals():
    '''
    __INIT__
    initalize the data file
    '''
    def __init__(self, df = '', num_clusters = 8):
        # initalize  the df
        self.open_df(df)
        self.num_clusters = num_clusters
        # self.compute_histogram()
        # print(self.df)

    '''
    OPEN_df
    Opens the desired csv file and makes sure that the data is formatted correctly

    This will also open a new df if called

    Errors:
    '''
    def open_df(self, df = ''):
        # open csv
        df = pd.read_csv(df)

        # drop first column (the first column is the row number and is a repeat)
        self.df = df.drop(df.columns[0], axis=1)

        # cut off first 1000 rows
        # df = df.iloc[100:, :]

        # keep only 1st 1,000 rows for small scale testing
        # self.df = df.iloc[:1000, :]

        # normalize
        self.df = self.z_score()

    '''
    DISTRIBUTIONS
    Calculates the distributions of every column.
    Distributions used:
        Z-score

    Resources:
        https://towardsdatascience.com/data-normalization-with-pandas-and-scikit-learn-7c1cc6ed6475
        https://towardsdatascience.com/understanding-the-normal-distribution-with-python-e70bb855b027
        
    '''
    # distributions by column
    def distributions(self):
        fig = px.line(self.df, y=self.df.columns[0])
        
        fig.update_layout(title='Visual distribution z-score')
        fig.update_xaxes(title_text='Time (min)')
        fig.update_yaxes(title_text='Sensor Value')
        return fig


    '''
    HEAT_MAP
    Calculates and visualizes the heat map of the dataframe

    This heatmap is not organized currently and only displays
    regular column values

    Errors:
        There is an issue where it only displays the name of ~70 columns when fully zoomed out.
        The rest of the names will appear when the graph is zoomed in

    Resources:
        https://datatofish.com/correlation-matrix-pandas/
    '''
    def heat_map(self):
        # make correlation df
        corr_matrix = self.df.corr()
        corr_matrix = np.abs(corr_matrix)
        # print(corr_matrix)


        fig = px.imshow(corr_matrix, title='Correlation heatmap')
        fig.update_layout(
            autosize=True,
            width=800,
            height=800
        )
        # fig.update_xaxes(title_text='Sensor')
        fig.update_yaxes(title_text='Sensor')
        return fig


    '''
    TIME_SERIES
    Creates a visual for the time series data

    This will work but will take a long time to load. The lines
    also jumbled and too close. You can click on the sensors in
    the legend to switch what is visable

    Resources:
        https://plotly.com/python/time-series/
        https://plotly.com/python/range-slider/
    '''
    def time_series(self):
        fig = px.line(self.df, y=self.df.columns,
                title='Time series data')
        fig.update_xaxes(title_text='Time (min)')
        fig.update_yaxes(title_text='Sensor Value')
        fig.update_layout(xaxis=dict(rangeslider=dict(visible=True),
                                type="linear"))
        
        return fig


    '''
    HISTOGRAM
    Creates a kernel density histogram of the data
    Only works for one column for now

    Resources:
        https://plotly.com/python/histograms/
    '''
    def compute_histogram(self):
        # without kernel density
        self.histogram_list = []
    
        for col in self.df:
            # print(col)
            # without kernel density
            fig = px.histogram(self.df, x=col, nbins=20, marginal='box') #nbins is number of bars in graph Marginal = rug, box, violin
            fig.update_layout(title='Histogram for ' + col)
            fig.update_yaxes(title_text='Value count')
            fig.update_xaxes(title_text='Sensor Value')
            self.histogram_list.append(fig)
        print('done computing histograms')

    '''
    GET_HISTOGRAM
    Returns a histogram graph
    '''
    def get_histogram(self, sensor=0):
        return self.histogram_list[sensor]

    '''
    REDUCE PCA
    Apply dimensionality reduction algorithm
    '''
    def reduce_pca(self):
        # pca
        pca = PCA(n_components=4, svd_solver='full')
        pcs = pca.fit_transform(self.dft.values)
        self.clusters['pc1'] = pcs[:, 0]
        self.clusters['pc2'] = pcs[:, 1]
        self.clusters['pc3'] = pcs[:, 2]

    '''
    Z SCORE
    Apply standard scaling to our algorithm
    '''
    def z_score(self):
        # scale with zscore
        z_score = StandardScaler()
        z_score.fit(self.df)
        z_data = z_score.transform(self.df)
        return pd.DataFrame (z_data, columns = self.df.columns)


    '''
    VISUALIZE
    Makes a scatterpolt of the visualizations in 3d
    '''
    def visualize(self, name='None'):
        # print(clusters.columns)
        # clusters.to_csv(os.getcwd() + '\\data\\testing.csv')
        # visualize
        fig = px.scatter_3d(self.clusters, x=self.clusters['pc1'], y=self.clusters['pc2'], z=self.clusters['pc3'], hover_data={'names':True}, color = 'cluster')
        fig.update_layout(title='PCA 3D clustering: '+ name)
        # fig.show()
        self.cluster_fig = fig

    '''
    GET_CLUSTER_VIZ
    performs clustering on the dataset, calls the visualize function and returns the 3d graph
    '''
    def get_cluster_viz(self):
        # normalize
        # self.df = self.z_score()

        # save names in list
        self.names_list = list(self.df.columns)

        # cluster
        self.dft = self.df.transpose()
        hiearchical = AgglomerativeClustering(n_clusters=self.num_clusters).fit(self.dft)
        
        # I probably do not have to copy all the data, just the column number
        self.clusters = self.dft
        self.clusters['cluster'] = hiearchical.labels_.astype(str)

        # pca
        self.reduce_pca()
        self.clusters['names'] = self.names_list

        # visualize
        self.visualize('hiearchical')

        return self.cluster_fig
