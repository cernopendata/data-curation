#!/usr/bin/env python3

# Simple script to convert csv metadata file into a full js code file

# For pretty printing
import json

# For csv reading
import csv

# Open our metadata file to go through all the EVNT samples we've gathered metadata for
with open('EVNT_metadata.csv','r') as evgen_metadata_csv_file, open('EVNT_metadata.js','w') as evgen_js:
    # Write a header
    evgen_js.write('''import React, { useState } from 'react';
import '../css/custom.css';

const data = [
''')

    # Now for each line in the metadata file we're going to re-write the line as part of a list of dictionaries
    # Open the metadata as a formatted dictionary
    md_reader = csv.DictReader(evgen_metadata_csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')
    # Loop through all the rows in the file (header skipped automatically for DictReader)
    for row in md_reader:
        evgen_js.write( json.dumps(row,indent=3)+',\n' )

    # Now just add a footer for the js file
    evgen_js.write('''];

  const FilterableTable = () => {
      const [searchTerm, setSearchTerm] = useState('');

      const handleSearchChange = (event) => {
          setSearchTerm(event.target.value);
      };

      const filteredData = data.filter((row) => {
          return Object.values(row).some((value) =>
              value.toString().toLowerCase().includes(searchTerm.toLowerCase())
          );
      });

      return (
          <div>
            <input
              type="text"
              placeholder="Search..."
              value={searchTerm}
              onChange={handleSearchChange}
              style={{ marginBottom: '10px', padding: '3px', width: '100%' }}
            />
            <div className="scrollable-table-container">
              <table className="scrollable-table">
                <thead>
                  <tr>
                    <th>Dataset ID</th>
                    <th>Physics short</th>
                    <th>CoM energy (GeV)</th>
                    <th>Cross section (pb)</th>
                    <th>Filter efficiency</th>
                    <th>K-factor</th>
                    <th>Number of events</th>
                    <th>Generated events</th>
                    <th>Generators used</th>
                    <th>Generator tune</th>
                    <th>PDF</th>
                    <th>Keywords</th>
                    <th>Process description</th>
                    <th>Release</th>
                    <th>Filters</th>
                    <th>Job options</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredData.map((row) => (
                    <tr key={row.DSID}>
                      <td>{row.DSID}</td>
                      <td>{row.PhysicsShort}</td>
                      <td>{row.CoMEnergy}</td>
                      <td>{row.XSec}</td>
                      <td>{row.FiltEff}</td>
                      <td>{row.kFactor}</td>
                      <td>{row.Events}</td>
                      <td>{row.GenEvents}</td>
                      <td>{row.GenName}</td>
                      <td>{row.GenTune}</td>
                      <td>{row.PDF}</td>
                      <td>{row.Keywords}</td>
                      <td>{row.PhysComment}</td>
                      <td>{row.Release}</td>
                      <td>{row.Filters}</td>
                      <td>
                        <a
                          href={row.JobOptions}
                          target="_blank"
                          rel="noopener noreferrer"
                        >
                          link
                        </a>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
      );
  };

  export default FilterableTable;
''')
