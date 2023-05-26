#!/bin/bash

# This script trigger the YCSB benchmarking tool and
# results parser to generate the final csv file
# with the measurement results collected from the analysis.
# It accepts the number of executions as input or 1
# execution will be made by default.

# Retrieve the number of executions from the argument
num_executions=$1

# Check if the argument is provided
if [ -z "$1" ]; then
  num_executions=1
fi

OUTPUT_FILE="measurement_results.csv"

# output header
echo "File, RunTime(ms), Throughput(ops/sec), Count_Scavenge, Time_Scavenge(ms), Time_Scavenge(%), Count_MarkSweep, Time_MarkSweep(ms), Time_MarkSweep(%), Total_GCs, Total_GC_Time(ms), Total_GC_Time(%), CLEANUP_Operations, CLEANUP_AverageLatency(us), CLEANUP_MinLatency(us), CLEANUP_MaxLatency(us), CLEANUP_95thPercentileLatency(us), CLEANUP_99thPercentileLatency(us), INSERT_Operations, INSERT_AverageLatency(us), INSERT_MinLatency(us), INSERT_MaxLatency(us), INSERT_95thPercentileLatency(us), INSERT_99thPercentileLatency(us), INSERT_ReturnOK" > "$OUTPUT_FILE"

echo "Running benchmark script $num_executions times..."

# Run the script n times
for ((i=1; i<="$num_executions"; i++)); do
	./benchmarking-script.sh
	./parse-results.sh
	sync "$OUTPUT_FILE"
done
