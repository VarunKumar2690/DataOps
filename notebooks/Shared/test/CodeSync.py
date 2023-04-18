# Databricks notebook source
import subprocess

# Specify the directory containing the shell script
script_directory = "DataOps"

# Change to the script directory
subprocess.run(["cd", script_directory], shell=True)

# Run the shell script
subprocess.run(["./CodeSync.sh"], shell=True, cwd=script_directory)
