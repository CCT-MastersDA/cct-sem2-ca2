#!/bin/bash

# This script runs the YCSB benchmarking tool using the
# properties and config defined locally in the machine
# for MYSQL and MongoDB. Please, adatpt the script
# parameters to your own needs before using it.

# Path to the local ycsb folder
YCSB_PATH="/home/hduser/ycsb-0.17.0"

# Create the results folder (delete it first if exists)
if [ -d "results" ]; then
  rm -rf results
fi
mkdir results

# List of workloads
workloads=("workloada" "workloadb" "workloadc")

echo "Performing benchmarking tests on MongoDB and MySQL using YCSB..."

# Iterate over the list of workloads
for workload in "${workloads[@]}"
do
  echo "Deleting rows from usertable in MySQL..."
  mysql -uroot -ppassword -e "USE Benchmarking; DELETE FROM usertable;"
  
  echo "MYSQL - Running YCSB command for workload: $workload"
  $YCSB_PATH/bin/ycsb.sh load jdbc -P $YCSB_PATH/jdbc-binding/conf/db.properties -P $YCSB_PATH/workloads/$workload > "./results/mysql-$workload.txt"

  echo "Deleting usertable collection from MongoDB..."
  mongo ycsb --eval "db.usertable.drop();"

  echo "Mongo - Running YCSB command for workload: $workload"
  $YCSB_PATH/bin/ycsb.sh load mongodb -s -P $YCSB_PATH/workloads/$workload > "./results/mongo-$workload.txt"
  
  echo "========Completed workload: $workload========"
done
