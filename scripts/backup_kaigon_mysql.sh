BACKUP_DIR="/Users/DerekNien/Documents/NTU/Special Project/Projects/kaigon/db-backups-test"
BACKUP_CODE="/Users/DerekNien/Documents/NTU/Special Project/Projects/kaigon/db-scripts/Backup-To-Google-Drive"
#Sql file name with year-month-date-hour-minute
NAME='kaigon_'`date +%Y-%m-%d-%H%M`
SQLFILE=$NAME'.sql'
FILE_PATH="$BACKUP_DIR/$SQLFILE"

DBNAME='kaigon_dev'
DBUSER='root'
DBPASSWORD=''
echo "Dumping DB name=$DBNAME into $BACKUP_DIR"
#Create backup folder if folder is not existing
mkdir -p "$BACKUP_DIR"
cd "$BACKUP_DIR"
#Dump sql file to $SQLFILE
mysqldump -u $DBUSER -p $DBNAME --password=$DBPASSWORD --skip-lock-tables --force > $SQLFILE
#Cd to backup code folder
cd "$BACKUP_CODE"
echo "Uploading $SQLFILE to google drive"
#Upload backup file to google drive
python backup.py configs/config.json "$FILE_PATH"
echo "Done"

