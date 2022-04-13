# cms-release-info

This directory contains CMS year-specific and run-era-specific information and the code for deployment of an API server.

- `cms_release_info.json` contains the year-specific information such as luminosity information, CMSSW release to be used, the Global tag for the condition data, the lists of validated data. 
- `run_ranges.json` lists the information of each run era.

All information beyond the currently released data will be verified at the time of the release.

The directory also contains the code for an API server which is deployed through paas.cern.ch in http://api-server-cms-release-info.app.cern.ch/

- `Dockerfile` serves for building the software image to be deployed
- `index.js` defines the application
- `public/favicon.ico` is the web site icon
- `package*.json` files defines the packages needed for building the application.

This information is used in building of open data portal records. It can eventually be used also for getting the year-specific information for configuring software and/or computing environment for CMS open data analysis.

### Local testing with nodejs

For local testing of the API server, if `npm` and `nodejs` are available, install the required modules and run the start script (defined in `package.json`) with:

```
npm install
npm start
```

The server opens in http://localhost:8080

### Local testing with docker 

If `docker` is available locally, build and run the image with:

```
docker build --tag cms-info-server .
docker run -p 8080:8080 cms-info-server
```

The server opens in http://localhost:8080


