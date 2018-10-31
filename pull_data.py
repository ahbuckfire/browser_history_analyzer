import argparse
import datetime
import itertools
import logging
import pandas as pd
import sqlite3
import sys
import unicodecsv as csv



DATABASES_OF_INTEREST = {"urls": ["last_visit_time", "url", "title", "visit_count"],
                         "visits": ["id", "url", "visit_time", "from_visit", "transition", "segment_id", "visit_duration"],
                         "keyword_search_terms": ["keyword_id", "url_id", "lower_term", "term"],
                         "downloads": ["start_time", "current_path", "received_bytes", "total_bytes", "danger_type", "interrupt_reason", "opened", "last_access_time", "site_url", "tab_url", "mime_type", "last_modified"]}

DB_CHROME_LOCATION = "~/Library/Application\\ Support/Google/Chrome/Default/History"


def _parse_args():
    parser = argparse.ArgumentParser("Analyze chrome history")
    parser.add_argument("-d", "--database", default=DB_CHROME_LOCATION)
    parser.add_argument("-t", "--table", default="urls")
    parser.add_argument("-a", "--analyze", default=False)
    return parser.parse_args()


def create_db_connection(database_path):
    return sqlite3.connect(database_path)


def create_sql_query(table):
    return "SELECT {} FROM {};".format(", ".join(DATABASES_OF_INTEREST[table]), table)


def db_to_df(query, conn):
    return pd.read_sql_query(query, conn)


def db_to_csv(table, df):
    csv_path = table + ".csv"
    df.to_csv(csv_path, encoding="utf-8")
    return csv_path

def get_database_contents(database_path, table):
    logging.info("Querying database table named {}".format(table))
    csv_path = db_to_csv(
                    table,
                    db_to_df(
                        create_sql_query(table),
                        create_db_connection(database_path)))
    logging.info("The data for table {} has been written to csv at location: {}".format(table, csv_path))


def main():
    args = _parse_args()
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="[%(asctime)s] %(message)s")
    database_contents = get_database_contents(args.database, args.table)
    if args.analyze:
        pass
        # trigger analysis

if __name__ == "__main__":
    main()
