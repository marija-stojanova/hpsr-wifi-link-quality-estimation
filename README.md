<h1>Wi-Fi link quality estimation framework</h1>

This code accompanies the paper published in IEEE HPSR 2023. 
The notebook complete_modely.ipynb can be used as is, or modified and adapted to new data. 
The provided code generates a Ridge linear regression model for estimating the Frame Delivery Ratio (FDR) using experimental Wi-Fi data.

The data is detailed in the published paper. It was collected on a homemade platform using Wi-Fi 5 devices in our laboratory.


<h4>Usage</h4>
If adding new data, first apply "clean_data.sh" to it. This will add the names of the columns and make sure that the data is in the proper .csv format used later.

Then the "add_columns.py" is only used only once in the beginning to add the missing columns in the .csv files (distance, LoS, antenna orientation) and to generate the "complete_data.csv" file for each folder. Same as the "clean_data.sh", this only needs to be executed once for new samples (the existing samples are already ready to be used). If generating new data, make sure that the format "anetennaOrientation_distance_runNumber_*" is respected, as this is used to extract the "distance" and "antenna" columns in the "add_columns.py" script. Otherwise, modify the script accordingly. Pay attention that the "LoS" (line of sight) column is properly set for new data. 

The "complete_model.ipynb" is the notebook that should be executed and modified for visualizing/analyzing the data, studying the correlations, and fitting and examining the model (Ridge linear regression is implemented, but it can be extended to any other model). All the metrics and features are explained in it.

