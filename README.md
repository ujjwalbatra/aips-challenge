# aips-challenge

Python version 3.9

**All commands to be executed from project root.**

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


### Project structure
```shell
├── README.md
├── input_data
│   └── input.txt
├── output                                        # stores the generated report in text format
│   ├── report:2022-07-16 19:51:31.550992.txt
├── requirements.txt
├── src                                           # source code
│   ├── data_reader.py                      # class for reading data from input directory
│   ├── main.py                             # orchestrator
│   ├── metrics_generator                   # directory for storing reporting classes
│   │   ├── __init__.py
│   │   ├── base_metric_generator.py  # base reporting abstract class to be extended by all things reporting
│   │   ├── metric1_total_cars_metric_generator.py                    # output 1
│   │   ├── metric2_total_cars_grouped_by_day_metric_generator.py     # output 2
│   │   ├── metric3_top_three_values_metric_generator.py              # output 3
│   │   └── metric4_three_least_consecutive_total_metric_generator.py # output 4
│   └── output_generator.py                 # writing result to a text file
└── test                                          # contains all the unit tests
    ├── Makefile
    ├── __init__.py
    │   ├── __init__.cpython-38.pyc
    │   ├── test_metric1_total_cars_metric_generator.cpython-38.pyc
    │   ├── test_metric2_total_cars_grouped_by_day_metric_generator.cpython-38.pyc
    │   ├── test_metric3_top_three_values_metric_generator.cpython-38.pyc
    │   └── test_metric4_three_least_consecutive_total_metric_generator.cpython-38.pyc
    ├── test_metric1_total_cars_metric_generator.py
    ├── test_metric2_total_cars_grouped_by_day_metric_generator.py
    ├── test_metric3_top_three_values_metric_generator.py
    └── test_metric4_three_least_consecutive_total_metric_generator.py
```