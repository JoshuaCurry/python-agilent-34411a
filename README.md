# python-agilent-34411a
Python logger for Keysight/Agilent 34411A Digital Multimeter


## Usage

Set your multimeter address statically in `scope.py`.

Run the code using:

```
python scope.py
```

Press <kbd>CTRL</kbd><kbd>C</kbd> to end capture.

The script will generate a file like `reading-2017-09-13-15-01-35.300354.csv` with timestamps (in seconds) against readings, which are in SI units.
