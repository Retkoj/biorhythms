# Calculate biorhythm

Calculate place in the three biorhythm cycles based on days since date of birth (https://en.wikipedia.org/wiki/Biorhythm_(pseudoscience))

Takes birth date as required parameter. Optionally, a specific date for which to calculate
the positions in the three cycles can be given. If no specific date is given, the date of
today is used.

`python run.py --birth-date 2011-11-02 [--specific-date 2020-02-02]`

Example output:
```
3014 days between birth date and specified date
Physical currently at: 1
Emotional currently at: 18
Physical currently at: 11
```


Just a random project to do some coding.
Got the idea from: https://rosettacode.org/wiki/Biorhythms