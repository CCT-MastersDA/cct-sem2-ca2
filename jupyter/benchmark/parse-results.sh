#!/bin/bash

# This script reads a local results folder with
# the output from the YCSB benchmarking tool execution.
# The parsed results are expected to be stored in a file
# called measurement_results.csv in the local folder.

# Output CSV file path
OUTPUT_FILE="measurement_results.csv"

echo "Parsing the results folder..."

# Iterate over files in the results folder
for file in results/*.txt; do
    # getting file name
	filename=$(basename "$file")

	echo -n "$filename" >> "$OUTPUT_FILE"

    counter=0

	# Skip processing for the first lines
	skip=3
	if [[ "$filename" == *"mongo"*  ]]; then
	  skip=2
	fi

	# Read the file line by line	
	while IFS= read -r line; do
	    counter=$((counter+1))

		# Skip processing for the first three lines
		if [ "$counter" -le "$skip" ]; then
		  continue
		fi

		# Split the line by comma
		IFS=',' read -ra elements <<< "$line"
    
		# Extract the third element
		measurement=",${elements[2]}"

		# Append the measurement to the output file
		echo -n "$measurement" >> "$OUTPUT_FILE"
	done < "$file"
	echo "" >> "$OUTPUT_FILE"
done

echo "========Measurement results extracted and written to $OUTPUT_FILE.========"
