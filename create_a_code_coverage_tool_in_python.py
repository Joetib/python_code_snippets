# Use coverage package to measure code coverage
# Install coverage using
# >> pip install coverage

import coverage

# Create a coverage object
cov = coverage.Coverage()

# Start measuring code coverage
cov.start()

# Run the code you want to measure coverage for
# For example, run your tests here

# Stop measuring coverage
cov.stop()

# Generate a report
cov.save()
cov.html_report()

# Output
# A coverage report will be generated in HTML format
# Please Like and Subscribe