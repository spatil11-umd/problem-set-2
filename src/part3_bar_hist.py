import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

def plot_fta_bar(df):
    """
    1. Using the pre_universe data frame, create a bar plot for the fta column.
    """
    sns.countplot(data=df, x='fta')
    plt.title('FTA Counts')
    plt.savefig('data/part3_plots/fta_bar.png')
    plt.close()

def plot_fta_sex_hue_bar(df):
    """
    2. Hue the previous barplot by sex
    """
    sns.countplot(data=df, x='fta', hue='sex')
    plt.title('FTA Counts by Sex')
    plt.savefig('data/part3_plots/fta_sex_hue_bar.png')
    plt.close()

def plot_age_histogram(df):
    """
    3. Plot a histogram of age_at_arrest
    """
    sns.histplot(data=df, x='age_at_arrest', bins=30)
    plt.title('Histogram of Age at Arrest')
    plt.savefig('data/part3_plots/age_histogram.png')
    plt.close()

def plot_age_histogram_binned(df):
    """
    4. Plot the same histogram, but create bins that represent the following age groups:
       - 18 to 21
       - 21 to 30
       - 30 to 40
       - 40 to 100
    """
    bins = [18, 21, 30, 40, 100]
    labels = ['18-21', '21-30', '30-40', '40-100']
    df['age_group'] = pd.cut(df['age_at_arrest'], bins=bins, labels=labels, right=False)

    sns.countplot(data=df, x='age_group', order=labels)
    plt.title('Histogram of Age Groups at Arrest')
    plt.savefig('data/part3_plots/age_group_histogram.png')
    plt.close()
