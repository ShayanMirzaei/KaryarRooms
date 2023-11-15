import sys

from cli import CliInterface
from database.csv_database import CsvDatabase
from database.json_database import JsonDatabase
from service import Service


def main():
    csv_database = CsvDatabase(data_path="../data/csv")
    json_database = JsonDatabase(data_path="../data/json")

    database_flag = sys.argv[1]
    if database_flag == 'json':
        db = json_database
    elif database_flag == 'csv':
        db = csv_database
    else:
        print('invalid database flag')
        exit()

    service = Service(database=db)

    cli = CliInterface(service)
    cli.run()


if __name__ == "__main__":
    main()
