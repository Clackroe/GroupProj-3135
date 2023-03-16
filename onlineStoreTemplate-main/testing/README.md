# Testing Directory

This directory contains the unittesting files and reports for the application. Testing functions are organized into separate files, based on the module they are testing (e.g. `dbTests.py` tests features from the `database` module).

## Reports Subdirectory

The `reports` subdirectory is where generated reports are stored after running the `test.py` script from the repository root. Each report is a subdirectory, automatically named by the date and a unique identifier. Within each report, text files are written for each test file that was run, identified by the naming convention `<testType>_report.txt` (e.g. `database_report.txt`). Only failed tests have descriptions written in the output report. Below is an example of a `database_report.txt` file:

```text
Test report for database tests.
Error in test_dict_factory_link: Row factory is not linked to dict_factory.
  - Expected: <function dict_factory at 0x100a7b370>
  - Actual: <sqlite3.Connection object at 0x100857440>
database tests complete.
3 out of 4 tests passed.
```

## authTests.py File

This script contains the unittests for the `authentication` module. The tests focus on evaluating the `hash_password` function from the `authTools.py` file. This is done by ensuring that the salt is generated, used, and returned correctly, which requires the tests to reference generated and provided password hash keys. This is another point where students can easily extend the codebase for their group project, as unittests for all other functions in the `authentication` module are missing.

## dbTests.py File

This script contains the unittests for the `database` module. The tests here are less thorough than the `authTests.py` file, but they cover a wider range of features. The database initialization, `dict_factory` conversion link, connection isolation level, and existence of the `inventory` table are all tested from this file. Students should consider adding more tests to check the existence of other tables and functionality of various query functions in the `db.py` file.

## coreTests.py File

This script contains the unittests for the `core` module. Similar to the `authTests.py` file, the tests here are limited in scope. Functions from the `session.py` are tested, specfically ones that handle session management. More thorough testing for specific user sessions, multiple users, and any functions from the `utils.py` file would be a beneficial addition from students.
