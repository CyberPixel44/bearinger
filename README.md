# Bearinger

Bearinger is a Python script for calculating the bearing, short path, and long path distance for amateur radio operations. It uses latitude and longitude or Maidenhead grid squares as input.

## Features

- Calculate bearing between two points
- Calculate short path and long path distance between two points
- Input can be latitude and longitude or Maidenhead grid squares
- Distance can be displayed in kilometers or miles
- Interactive mode for easy usage

## Usage

You can use Bearinger in interactive mode or by passing arguments directly.

### Interactive Mode

To run Bearinger in interactive mode, use the `-i` or `--interactive` option:

```bash
python bearinger.py -i
```

In interactive mode, you will be prompted to select the distance unit (miles or kilometers), the input method (latitude and longitude or Maidenhead grid square), and to enter the coordinates or grid squares.

### Latitude and Longitude

To calculate the bearing and distance using latitude and longitude, use the `-l` or `--latlong` option followed by the coordinates:

```bash
python bearinger.py -l lat1 lon1 lat2 lon2
```

### Maidenhead Grid Square

To calculate the bearing and distance using Maidenhead grid squares, use the `-g` or `--grid` option followed by the grid squares:

```bash
python bearinger.py -g grid1 grid2
```

### Distance in Miles

By default, the distance is displayed in kilometers. To display the distance in miles, use the `-mi` or `--miles` option:

```bash
python bearinger.py -mi -l lat1 lon1 lat2 lon2
```

## Help

To display the help message, use the `-h` or `--help` option:

```bash
python bearinger.py -h
```

