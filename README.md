# Garmin FIT Exporter

**Garmin FIT Exporter** allows you to export some types of fit files to gpx or to markdown.

- What do you need? *Your Garmin watch with a USB connection*

## REQUIRED

- Hardware: *Garmin watch* + *USB connection*
- Main library: `pip install garmin_fit_sdk`

## PROJECT STRUCTURE

- Package **garmin_fit_export**: *Garmin FIT file export and debug manager*
- `garmin_fit_exporter.py`: main script

## USAGE

```bash
usage: garmin_fit_exporter.py [-h] -s SOURCE -d DESTINATION [-dg]

options:
  -h, --help            show this help message and exit
  -s, --source SOURCE   file or directory source
  -d, --destination DESTINATION
                        directory destination
  --debug          Export debug raw file
```

### Gpx

Fit file types that are exported to **gpx**:

- Location
- Activity
- Course

### Markdown

Fit file types that are exported to **markdown**:

- Record
- Workout

### Debug - option

The `debug` option allows you to export all types of fit files in raw format.
The output file will have the extension: **.fit_bak.txt**

#### Main device

**Instinct 2** is the device from which I get the *FIT files* to run the debug tests

## CONTRIBUTING

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

## CODE OF CONDUCT

See [CODE OF CONDUCT](./CODE_OF_CONDUCT.md) for details.

## LICENSE

See [LICENSE](./LICENSE) for details.

## AUTHOR

Roberto Quintiliani
