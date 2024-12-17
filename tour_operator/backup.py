import os
import time
import yadisk
import schedule
import datetime
import shutil
from tour_operator.settings import DATABASES

YA_DISK_CONFIG = {
    "app_id": "",
    "app_secret": "",
    "token": "",
    "backup_path": "db_backups"
}


def get_sqlite_dump(db_file: str):
    if not os.path.exists(db_file):
        raise Exception(f"Database file {db_file} does not exist.")
    return db_file


def make_backup():
    cloud_client = yadisk.Client(YA_DISK_CONFIG['app_id'], YA_DISK_CONFIG['app_secret'], YA_DISK_CONFIG['token'])
    config = DATABASES['default']

    db_file = config['NAME']
    format_date = datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    output_file = f"dump_{format_date}.db"

    shutil.copy(db_file, output_file)
    print(f"SQLite dump created: {output_file}")

    link = cloud_client.upload(output_file, f"{YA_DISK_CONFIG['backup_path']}/{output_file}")
    print("Backup successfully uploaded to Yandex.Disk ->", link.href)

    os.remove(output_file)


if __name__ == "__main__":
    print("Making first backup force...")
    make_backup()

    print("\nBackup scheduler started")
    schedule.every(1).hours.do(make_backup)
    while True:
        schedule.run_pending()
        time.sleep(1)