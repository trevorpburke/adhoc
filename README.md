## Adhoc – a Flask app UI to manage automated SQL reports

Adhoc is a Python package in-the-making that will provide a user interface to manage and schedule SQL reports.

The Adhoc UI is built with Flask and will allow users to input database information, write queries, schedule those queries, and manage their delivery method whether via email or SFTP. 

Overall Goals: 

    – Simple, but effective UI
    – Support for email and FTP/SFTP delivery of reports
    – Syntax highlighting on input
    – Multiple SQL dialect support
    – Sophisticated error-handling
    – SSH-tunnel capabilities 
    – Command line interface 
    – Advanced cron-like scheduling formatting

To Install & Run Locally:

    $ git clone https://github.com/trevorpburke/adhoc.git && cd ahoc
    $ python3 -m venv .
    $ source bin/activate
    $ pip install -r requirements.txt
    $ flask db migrate -m "create tables" # run migrations
    $ flask db upgrade 
    $ flask run

Preliminary screenshots of the Report and Configuration routes:

![Configuration Route](https://raw.githubusercontent.com/trevorpburke/adhoc/master/images/configuration_route.png)
![Report Route](https://raw.githubusercontent.com/trevorpburke/adhoc/master/images/report_route.png)
