import pandas as pd
import matplotlib.pyplot as plt

lblue = '#41B6E6'
dblue = '#002D72'
green = '#84BD00'
dgrey = '#7D868C'
lgrey =  '#BCBEC0'

cmap = ['#002D72', '#BCBEC0', '#84BD00', '#575F80','#736D5A', '#BCBEC0', '#41B6E6', '#294F89', '#84BD00', '#1C7599']

def plot(df, kind='line', figsize=(15,5), color=dgrey, ax=None, lw=None, stacked=False, highlight=False, highlight_list=None, highlight_color=None, labels_num=False, labels_pct=False):

    '''
    Parameters:
    df: pandas dataframe or pandas series
    kind: str, type of graph to plot. Choices are same as pandas plot
    figsize: tuple, (width, height)
    color: str, HEX code of color of plot elements
    ax: axis to use if different from default
    lw: int, linewidth
    stacked: boolen, creates a stacked barchart if true
    highlight: boolean, if true allows the user to highlight certain points on the chart
    highlight_list: array, list of points to highlight
    highlight_color: str, HEX code of color to highlight the points in highlight_list
    labels_num: boolean, creates labels for the graph. Formatted as numbers
    labels_pct: boolean, creates labels for the graph. Formatted as percents

    Colors:
    lblue: asurion light blue
    dblue: asurion dark blue
    green: asurion green
    dgrey: asurion dark grey
    lgrey: asurion light grey
    '''

    ax = df.plot(kind=kind, figsize=figsize, color=color, lw=lw, ax=ax, stacked=stacked)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_color(lgrey)
    ax.spines['left'].set_color(lgrey)
    ax.yaxis.label.set_color(dgrey)
    ax.xaxis.label.set_color(dgrey)
    ax.tick_params(axis='x', colors=dgrey, size=5)
    ax.tick_params(axis='y', colors=dgrey, size=5, labelsize=18)
    plt.ylabel(fontsize=12, fontweight='bold')
    plt.xlabel(fontsize=12, fontweight='bold')
    if highlight == True:
        for i in highlight_list:
            ax.patches[i].set_color(highlight_color)
            ax.get_yticklabels()[i].set_fontweight('bold')
            ax.get_yticklabels()[i].set_color(highlight_color)
    if labels_pct == True:
        for i, val in enumerate(df):
            plt.text(list(df.index)[i], val + (val * 0.05), '{}%'.format(round(val * 100, 2)), color=dgrey, weight='bold')
    if labels_num == True:
        for i, val in enumerate(df):
            plt.text(list(df.index)[i], val + (val * 0.05), '{}'.format(round(val, 2)), color=dgrey, weight='bold')
