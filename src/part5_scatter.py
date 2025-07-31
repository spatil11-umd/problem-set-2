import seaborn as sns
import matplotlib.pyplot as plt

def plot_felony_nonfelony_hue_charge(df):
    """
    1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the prediction for nonfelony,
    and hue this by whether the current charge is a felony.

    Print a statement about the group of dots on the right side.
    """
    sns.lmplot(data=df, x='prediction_felony', y='prediction_nonfelony', hue='charge_type', fit_reg=False)
    plt.title('Prediction Felony vs Non-Felony Rearrest by Charge Type')
    plt.savefig('data/part5_plots/felony_vs_nonfelony_by_charge_type.png')
    plt.close()
    print("The group of dots on the right (high felony prediction) mostly corresponds to arrestees with a current felony charge, indicating the model strongly predicts felony rearrest for those individuals.")

def plot_felony_prediction_vs_actual_rearrest(df):
    """
    2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.

    Print a statement about calibration.
    """
    sns.scatterplot(data=df, x='prediction_felony', y='y_felony')
    plt.title('Prediction for Felony Rearrest vs Actual Rearrest')
    plt.savefig('data/part5_plots/felony_pred_vs_actual.png')
    plt.close()
    print("Based on this plot, we can assess calibration by checking if higher predicted probabilities correspond to actual rearrest. A well-calibrated model should show a clear positive association.")
