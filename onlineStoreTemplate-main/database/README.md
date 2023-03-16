# Database Directory

This directory contains the database files for the application, which includes a reset script (`resetDB.sh`), the schema file (`schema.sql`), a set of starter data (`startingData.sql`), and the main database management file (`db.py`). Upon creation, the `storeRecords.db` file will be located in this directory, and will be used to store the data for the application.

## db.py File

This script contains the core `Database` class, wherein all querying and database management methods are defined. When exploring the current functionality, notice that large comment headers have been added to organize methods by the table they are associated with. Extra querying methods or refactoring of existing methods into a more elegant structure would be a great addition to the codebase.

## resetDB.sh File

This script is automatically run when the `setup.sh` script from root is run, but this can also be run manually whenever the database needs to be reset. Assuming permissions are set correctly, this script can be run by executing `./resetDB.sh` from the `database` directory. This script will delete the `storeRecords.db` file (if it exists), and then run the `schema.sql` and `startingData.sql` files to create a new database with the correct schema and starter data.

## schema.sql File

This file contains the SQL commands to create the database based on a predefined schema. This file is run by the `resetDB.sh` script, and should not be run manually.

## startingData.sql File

This file contains the SQL commands to insert the starter data into the database. This file is run by the `resetDB.sh` script, and should not be run manually.
