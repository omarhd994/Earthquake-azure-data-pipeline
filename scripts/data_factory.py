# Databricks notebook receiving parameters from ADF

# Bronze
@string(activity('Bronze Notebook').output.runOutput)

# Silver
@string(activity('Silver Notebook').output.runOutput)   
