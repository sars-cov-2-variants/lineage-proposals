#!/bin/bash

# This script adds to the recombinants.csv file, taking the issue URL as the argument
# 1. Select the first field from TSV files in ~/Downloads/nextstrain_fetch*.
# 2. Append the provided URL to the end of each line.
# 3. Skip the first line (header) and append the result to recombinants.csv
# 4. Deduplicate identical lines to make the script idempotent
# 5. Remove all files matching the ~/Downloads/nextstrain_fetch* pattern.

usage() {
  echo "Usage: $0 <URL>
  echo "Example: $0 https://github.com/sars-cov-2-variants/lineage-proposals/issues/984
}

url="$1"

if [ -z "$url" ]; then
  echo "Error: Please provide a url as an argument."
  usage
  exit 1
fi

tsv-select -f1 ~/Downloads/nextstrain_fetch* \
  | sed "s,\$,\t${url}," \
  | tail -n +2 \
  >>recombinants.tsv

cp recombinants.tsv tmp/recombinants.tsv
cat tmp/recombinants.tsv | awk '!a[$0]++' >recombinants.tsv
rm tmp/recombinants.tsv

#rm ~/Downloads/nextstrain_fetch*

