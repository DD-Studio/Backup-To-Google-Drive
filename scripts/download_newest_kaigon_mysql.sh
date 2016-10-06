BACKUP_DIR="/Users/DerekNien/Documents/NTU/Special Project/Projects/kaigon/db-auto-backups/"
BACKUP_CODE="/Users/DerekNien/Documents/NTU/Special Project/Projects/kaigon/db-scripts/Backup-To-Google-Drive"

cd "$BACKUP_CODE"
echo "Downloading newest file from to google drive"
#Upload backup file to google drive
python download_newest.py configs/config.json "$BACKUP_DIR"
echo "Done"

