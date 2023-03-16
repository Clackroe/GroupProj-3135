# check if the database exists
if [ -f storeRecords.db ]; then
    echo "Database exists. Deleting..."
    rm -rf storeRecords.db
fi
sqlite3 storeRecords.db < schema.sql
sqlite3 storeRecords.db < startingData.sql