# Browser History Analyzer

This is a tool that will analyze your browser history up since the last time you deleted your browser history.

## Current Features
    * Can specify:
        * the database to pull data from
        * if you need to pull new data
        * the target to write the database data to

    * Simple count of:
        * Number of times you:
            * visited a website
            * visited a specific page

## TODO
    * Near term
        * Download data by weekly use and store in seperate files
        * Add analysis of peak use hours and days
        * Add analysis of if certain sites are more likely to be visited at a certain time of day or day of week
        * Chart of 5 most popular sites visited per day
        * Flexible SQL query format (to access other database tables)

    * Next Steps
        * Send emailed report
        * App version? (seperate project)
        * potentially add option to store the data on s3 bucket

    * Other tables to add:
        * keyword_search_terms: google query search analysis
        * downloads: infograph of downloads from chrome

    * Other aspects to include
        * hook up other browsers and devices to get a hollistic picture
            * i.e. personal computer, smart phone, etc.

