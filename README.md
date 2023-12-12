# Project Overview

Python 3.11 was used but most 3.x versions should work. Check requirements.txt for the necessary additional packages.

## 1. Code
This section contains various code files for data manipulation, the model itself and visualization.
 - *raw_to_usable.py* - converts the raw data to a list of each athlete
 - *event_pair_frequency.py* - creates the plots found in the paper
 - *random_sampling.py* - allows for random sampling of the data set and testing specified orders
 - the_model/
   - *main.py* - runs through all 5*11! permutations in a single thread
   - *resumable_data.json* - saves the iteration and current best every 10000 loops so the program can pick up where it left off

## 2. Data
This section contains 5 files in total.

The following three,
- EventsBySwimmer_Boys.tsv
- EventsBySwimmer_Girls.tsv
- EventsBySwimmer_Combined.tsv

are tab separated files containing the participating athletes and their respective events.
The combined file is simply the boys file appended with the girls file.

The following two,
- NYSPHSAA_22-23_Boys.csv
- NYSPHSAA_22-23_Girls.csv

are files containing the raw data from each meet, modified for readability.

## Other Notes

The folder code2 contains 11 separate files, each with their own implementation of model.
Because I didn't have time to code in multiprocessing, each file was run concurrently on a large computer, each writing to their own json file.
Use at your own risk but they should work.


Though not useful in any conceivable way, the worst event order found so far (by randomly sampling from the input space) is 794 with the following order:

['500 Free', '200 Free', '50 Free', '100 Free', '400 FR', '200 FR', '200 MR', '100 Fly', '200 IM', '100 Back', '100 Breast', 'Diving']