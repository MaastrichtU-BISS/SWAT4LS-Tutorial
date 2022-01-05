import matplotlib.pyplot as plt
import matplotlib as mpl

def make_hists(df, fig_kwargs=None, hist_kwargs=None,
               style_cycle=None):
    '''

    Parameters
    ----------
    df : pd.DataFrame
        Datasource

    fig_kwargs : dict, optional
        kwargs to pass to `plt.subplots`

        defaults to {'fig_size': (4, 1.5*len(df.columns),
                     'tight_layout': True}

    hist_kwargs : dict, optional
        Extra kwargs to pass to `ax.hist`, defaults
        to `{'bins': 'auto'}

    style_cycle : cycler
        Style cycle to use, defaults to 
        mpl.rcParams['axes.prop_cycle']

    Returns
    -------
    fig : mpl.figure.Figure
        The figure created

    ax_list : list
        The mpl.axes.Axes objects created 

    arts : dict 
        maps column names to the histogram artist
    '''
    if style_cycle is None:
        style_cycle = mpl.rcParams['axes.prop_cycle']

    if fig_kwargs is None:
        fig_kwargs = {}
    if hist_kwargs is None:
        hist_kwargs = {}

    hist_kwargs.setdefault('log', True)
    # this requires nmupy >= 1.11
    hist_kwargs.setdefault('bins', 'auto')
    cols = df.columns

    fig_kwargs.setdefault('figsize', (4, 1.5*len(cols)))
    fig_kwargs.setdefault('tight_layout', True)
    fig, ax_lst = plt.subplots(len(cols), 1, **fig_kwargs)
    arts = {}
    for ax, col, sty in zip(ax_lst, cols, style_cycle()):
        h = ax.hist(col, data=df, **hist_kwargs, **sty)
        ax.legend()

        arts[col] = h

    return fig, list(ax_lst), arts