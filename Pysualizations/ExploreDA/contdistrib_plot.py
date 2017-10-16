
"""
Continious distribution plot
----------------------------
Distribution of continious variables can be plotted and inspected with the
functions of this module.

"""

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats as stats


def cont_distrib_plot(x, n_bins, logscale=False):
    """Function to explore the distribution of a continiuos variable.

    Parameters
    ----------
    x: pd.DataFrame
        the data variable we want to obtain its distribution.
    n_bins: int
        the number of bins we want to use to plot the distribution.
    logscale: boolean (default=False)
        if we want to use logscale for both variables.

    Returns
    -------
    fig: matplotlib.pyplot.figure
        the figure of the distribution required of the variable data defined in
        `x`.

    TODO
    ----
    Kernel density estimation

    """
    ## 0. Preparing inputs
    # Filtering nan
    x = x.dropna()
    # Median
    median = x.quantile(0.5)
    x = np.array(x)

    ### A. Plotting
    fig = plt.figure()
    ## 1. Plot histogram
    ax0 = plt.subplot2grid((5, 1), (0, 0), rowspan=4)
    ax0.hist(x, n_bins)
    # Improving axes
    ax0.set_xlim([x.min(), x.max()])
    ax0.set_ylabel('Counts')
    if logscale:
        ax0.set_yscale('log')
        ax0.set_xscale('log')
    # Mark of median
    l1 = plt.axvline(median, linewidth=2, color='r', label='Median',
                     linestyle='--')
    # Mark of mean
    l2 = plt.axvline(x.mean(), linewidth=2, color='k', label='Mean',
                     linestyle='--')
    ax0.legend([l1, l2], ['Median', 'Mean'])
    ax0.grid(True)

    ## 2. Plot box_plot
    ax1 = plt.subplot2grid((5, 1), (4, 0), sharex=ax0)
    ax1.boxplot(x, 0, 'rs', 0, 0.75)
    # Making up the plot
    mini = x.min()
    maxi = x.max()
    delta = (maxi-mini)/25.
    ax1.set_xlim([mini-delta, maxi+delta])
    if logscale:
        ax1.set_yscale('log')
        ax1.set_xscale('log')
    ax1.grid(True)
    ax1.set_yticklabels('A')
    plt.setp(ax0.get_xticklabels(), visible=False)

    ## 3. Main settings
    fig.suptitle('Distribution exploration of continious variable',
                 fontsize=14, fontweight='bold')
    plt.xlabel('Value')

    return fig


def qqplot(measurements):
    stats.probplot(measurements, dist="norm", plot=plt)
    fig = plt.gcf()
    return fig


def histogram_kde_plot(data_df, varname, title, ylabel):
    ## Distribution of the variable
    fig, ax = plt.subplots(figsize=(12, 8))
    #logi = (data_df[varname].isnull()) | (data_df[varname] == 0)
    #logi = np.logical_not(logi)
    data_var = data_df.loc[:, varname]
    #sns.distplot(a=data_var, bins=100, kde=False)
    sns.distplot(a=data_var, bins=100, kde=True)
    _ = ax.set(title=title, ylabel=ylabel)
    #ax.set_yscale('log')
    #ax.set_xscale('log')

    return fig


def violins_plot(data_df, x_var, y_var, ylabel, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.violinplot(x=x_var, y=y_var, data=data_df, scale='count')
    #sns.swarmplot(data=data_df[internal_chars], color="w", alpha=.2)
    #ax.set_yscale('log')
    ax.set_ylabel(ylabel)
    _ = plt.title(title)
    return fig


def plot_notnull_distributions(data_df, name_feats):
    for name_fea in name_feats:
        logi = (data_df[name_fea].isnull()) | (data_df[name_fea] == 0)
        logi = np.logical_not(logi)
        nonnullvals = data_df.loc[logi, name_fea]
        sns.distplot(a=nonnullvals, bins=100, kde=False, label=name_fea)


def multiple_notnull_histograms(data_df, name_feats, title, xlabel, ylabel,
                                log=True):
    fig, ax = plt.subplots(figsize=(12, 8))
    plot_notnull_distributions(data_df, name_feats)
    ax.set(title=title, ylabel=ylabel)
    if log:
        ax.set_yscale('log')
    ax.set_xlabel(xlabel)
    _ = ax.legend()
    return fig

