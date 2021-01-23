# Calculate biorhythm

Calculate place in the three biorhythm cycles based on days since date of birth (https://en.wikipedia.org/wiki/Biorhythm_(pseudoscience))

Takes birth date as required parameter. Optionally, a specific date for which to calculate
the positions in the three cycles can be given. If no specific date is given, the date of
today is used.

Just a random project to do some coding.
Got the idea from: https://rosettacode.org/wiki/Biorhythms

### Requirements
Developed on Windows 10 using python 3.7, because python 3.8 + Windows + streamlit didn't play nice.
Added a windows_requirements.txt that contains the package versions that got streamlit running on Windows 10 at time of development.

### Command line implementation
`python run.py --birth-date 2011-11-02 [--specific-date 2020-02-02]`

Example output:
```
3014 days between birth date and specified date
Physical currently at: 1
Emotional currently at: 18
Physical currently at: 11
```

### Streamlit implementation
Provides a dashboard running at localhost

`pip install -r requirements.txt`
or
`pip install -r windows_requirements.txt # generated 23jan.2021`

To run the dashboard:

`streamlit run dashboard.py`