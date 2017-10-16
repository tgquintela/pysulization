

import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


def percentage_missing_per_variable(data_df, missing_val=0):
    """Plotting function for missing values.

    Parameters
    ----------
    train_df: pd.DataFrame
        the data we want to study.

    """
    data_na = (data_df.isnull().sum() / len(data_df)) * 100
    data_na = data_na.drop(data_na[data_na == 0].index).\
        sort_values(ascending=False)
    ## Proportion of missing values per variable
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.xticks(rotation='90')
    sns.barplot(x=data_na.index, y=data_na)
    _ = ax.set(title='Percent missing data by feature', ylabel='% missing')
    return fig


def missing_values_matrix(data_df):
    fig = msno.matrix(data_df, inline=False)
    w, h = fig.get_size_inches()
    h *= 3/2.
    print(w, h)
    fig.set_size_inches(w, h)

#    axes = []
#    for ax in fig.get_axes():
#        pos = ax.get_position()
#        ax.set_position([pos.x0, 0.02, pos.x1, pos.y1-pos.y0+0.02])
#        axes.append(ax)

    _ = fig.suptitle('Matrix with missing values', fontsize=40)
    return fig

