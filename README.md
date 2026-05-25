# Garmin FIT Exporter

**Garmin FIT Exporter** allows you to export some types of fit files to gpx or to markdown.

- What do you need?
  *Your Garmin watch with a USB connection*

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

## CONTRIBUTING

Thank you for your interest in contributing! Please follow these simple rules to keep the project organized and collaborative.

### Prerequisites

- Python 3.10+

### How to Propose a Change

1. Fork the repository
2. Create a dedicated branch (`git checkout -b feature/your-feature-name`)
3. Implement your changes
4. Ensure all tests pass
5. Open a Pull Request with a clear description of what you did

### Pull Request Rules

- Keep PRs small and focused
- Clearly describe the problem being solved
- Link any related issues
- Update documentation if needed
- Ensure code is formatted and linted

### Code Style

- Follow PEP8
- Avoid overly long functions
- Use clear and meaningful names
<!-- - Use Black for formatting -->

<!-- ### Tests

- Use pytest
- Add tests for every new feature
- Ensure `pytest` runs without errors -->

### Bug Reporting

When opening an issue, include:

- Steps to reproduce
- Expected behavior
- Observed behavior
- Environment details (OS, Python version, project version)

### Feature Requests

Please include:

- Why the feature is useful
- Who benefits from it
- How it integrates into the project

<!-- ### Code of Conduct

This project follows the *Contributor Covenant*.
Please act respectfully and professionally. -->

## LICENSE

All rights reserved.
License to be defined.

## AUTHOR

Roberto Quintiliani
