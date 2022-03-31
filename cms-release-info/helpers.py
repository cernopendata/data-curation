import requests
import json

def read_run_range(run_period):
    """Read run range for the given run period."""

    run_range = []

    url = 'http://api-server-cms-release-info.app.cern.ch/runeras/run_min?run_era='+run_period
    run_min = json.loads(requests.get(url).text.strip())
    url = 'http://api-server-cms-release-info.app.cern.ch/runeras/run_max?run_era='+run_period
    run_max = json.loads(requests.get(url).text.strip())
    run_range = run_min + run_max

    return run_range

def run_range_text(input):
    """Return run range text for open data run ranges for a given year or a given run range."""

    if "Run" in input:
        od_run_periods = []
        od_run_periods.append(input)
    else:
        url = 'http://api-server-cms-release-info.app.cern.ch/runeras/run_era?year='+input+'&released=yes'
        od_run_periods = json.loads(requests.get(url).text.strip())
        #od_run_periods = read_run_periods(input, 'od')

    run_range_text = ''
    for period in od_run_periods:
        run_range_str=list(map(str, read_run_range(period)))
        run_range_text += ' '+period+' is between run numbers '+" and ".join(run_range_str)+'.'
    return run_range_text
