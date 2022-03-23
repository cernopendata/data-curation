def read_run_periods(year, flag):
    """Read run periods for the given year, if flag od, only those released, if flag pp-phys, only those certified for pp."""

    run_periods = []
    with open("../cms-release-info/run_ranges_run2.txt", "r") as f:
        for line in f.readlines():
            run_period = line.split(",")[0]
            opendata = line.split(",")[3]
            run_type = line.split(",")[4]
            if year in run_period:
                if 'od' in flag:
                    if 'yes' in opendata:
                        run_periods.append(run_period)
                elif 'pp-phys' in flag:
                    if 'pp-phys' in run_type:
                        run_periods.append(run_period)
                else:
                    run_periods.append(run_period)
    return run_periods

def read_run_range(run_period):
    """Read run range for the given run period."""

    run_range = []
    with open("../cms-release-info/run_ranges_run2.txt", "r") as f:
        for line in f.readlines():
            if line.split(",")[0] == run_period:                
              run_range.append(line.split(",")[1].strip())
              run_range.append(line.split(",")[2].strip())
    return run_range

def run_range_text(input):
    """Return run range text for open data run rages for a given year or a give run range."""

    if "Run" in input:
        od_run_periods = []
        od_run_periods.append(input)
    else:
        od_run_periods = read_run_periods(input, 'od')

    run_range_text = ''
    for period in od_run_periods:
        run_range_text += ' '+period+' is between run numbers '+",".join(read_run_range(period)).replace(",", " and ")+'.'
    return run_range_text
