# aips-challenge

Python version 3.9

<span style="color:red">All commands to be executed from project root.</span>.

### Running the project
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

### Running tests
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m unittest discover . 
```

### Assumption
The input file will have all the timestamps (including 0).

If it does not have all timestamps then the requirement:

> "The 1.5 hour period with least cars (i.e. 3 contiguous half hour records)"

The above requirement will be affected if the assumption doesn't hold true.

In case the timestamps are missing (like in sample text), the solution is:
1. Generate a time series dataframe from the minimum timestamp to the maximum timestamp (frequency 30 mins).
2. Left join input data with the time series generated in time step 1, while defaulting the count for missing timestamps as 0.
3. Use the newly generated dataframe for calculation for metric 4 of the requirements.