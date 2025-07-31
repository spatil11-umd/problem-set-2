import seaborn as sns
import matplotlib.pyplot as plt

def plot_felony_prediction_bar(df):
    """
    1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
    """
    sns.set(style="whitegrid")
    g = sns.catplot(
        data=df,
        kind='bar',
        x='charge_type',
        y='prediction_felony',
        height=5,
        aspect=1.5,
        ci=None
    )
    g.set_axis_labels("Charge Type", "Average Predicted Felony Rearrest")
    g.set_titles("Average Predicted Felony Rearrest by Charge Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('data/part4_plots/felony_pred_by_charge_type.png')
    plt.close()

def plot_nonfelony_prediction_bar(df):
    """
    2. Now repeat but have the y-axis be prediction for nonfelony rearrest
    """
    sns.catplot(data=df, x='charge_type', y='prediction_nonfelony', kind='bar')
    plt.title('Prediction for Non-Felony Rearrest by Current Charge Type')
    plt.savefig('data/part4_plots/nonfelony_pred_by_charge_type.png')
    plt.close()
    print("Difference explanation: The prediction for non-felony rearrest tends to be higher for misdemeanor charges because those individuals are more likely to be rearrested for less serious offenses, while felony charges correspond to more serious crimes influencing felony rearrest predictions.")

def plot_felony_prediction_hue_actual_rearrest(df):
    """
    3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
    """
    sns.catplot(data=df, x='charge_type', y='prediction_felony', hue='rearrest_felony', kind='bar')
    plt.title('Felony Prediction by Current Charge and Actual Felony Rearrest')
    plt.savefig('data/part4_plots/felony_pred_hue_rearrest_by_charge_type.png')
    plt.close()
    print("Interpretation: Arrestees with a current felony charge but who did not get rearrested for a felony have a higher predicted probability than misdemeanor arrestees who did get rearrested for a felony, likely reflecting the model's weighting of current charge seriousness over actual outcome in prediction probabilities.")
