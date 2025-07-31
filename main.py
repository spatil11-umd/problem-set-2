import pandas as pd
import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
    ##  PART 2: PLOT EXAMPLES  ##
    part2.seaborn_settings()
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)
    
    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    part3.plot_fta_bar(pred_universe)
    part3.plot_fta_sex_hue_bar(pred_universe)
    part3.plot_age_histogram(pred_universe)
    part3.plot_age_histogram_binned(pred_universe)
    
    ##  PART 4: CATEGORICAL PLOTS  ##
    part4.plot_felony_prediction_bar(pred_universe)
    part4.plot_nonfelony_prediction_bar(pred_universe)
    part4.plot_felony_prediction_hue_actual_rearrest(pred_universe)
    
    ##  PART 5: SCATTERPLOTS  ##
    part5.plot_felony_nonfelony_hue_charge(pred_universe)
    part5.plot_felony_prediction_vs_actual_rearrest(pred_universe)

if __name__ == "__main__":
    main()
