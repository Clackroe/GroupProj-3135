from testing.authTests import test_hash_password_generates_salt, test_salt_length, test_hash_password_returns_given_salt, test_hash_password_uses_given_salt
from core.utils import generate_unique_id
from datetime import datetime
from testing.dbTests import test_init_db, test_get_inventory_exists, test_dict_factory_link, test_check_connection_threaded
from testing.coreTests import test_init_sessions, test_add_new_session, test_get_session
import os

# -------- Testing Function Constants --------

AUTH_FUNCS = [test_hash_password_generates_salt,
              test_salt_length,
              test_hash_password_returns_given_salt,
              test_hash_password_uses_given_salt]

DB_FUNCS = [test_init_db, test_get_inventory_exists,
            test_dict_factory_link,
            test_check_connection_threaded]

CORE_FUNCS = [test_init_sessions,
              test_add_new_session,
              test_get_session]

TESTING_FUNCTIONS = {"core": CORE_FUNCS,
                     "database": DB_FUNCS,
                     "authentication": AUTH_FUNCS}


def run_tests(test_type: str, test_funcs: list, report_file_path: str) -> int:
    """
    Runs all tests for a given set of test functions.

    args:
        - test_funcs: a list of test functions to run.
        - report_file_path: the path to the report file, where the results of the tests will be written.

    returns:
        - the number of failed tests as an integer.

    output:
        - Prints the results of failed tests.
    """
    failed_tests = 0
    with open(report_file_path, "a") as report_file:
        for test in test_funcs:
            result, error = test()
            if not result:
                report_file.write(f"{error}\n")
                failed_tests += 1
        report_file.write(f"{test_type} tests complete.\n")
        report_file.write(
            f"{len(test_funcs) - failed_tests} out of {len(test_funcs)} tests passed.\n")


def create_report_folder() -> str:
    """
    Creates a folder for the test reports.

    args:
        - None

    returns:
        - a unique, identifiable folder path for the reports as a string.
    """
    unique_id = generate_unique_id()
    current_date = datetime.now().strftime("%Y-%m-%d")
    report_folder_path = f"testing/reports/{current_date}_{unique_id}"
    os.makedirs(report_folder_path)
    return report_folder_path


def create_report_file(report_folder_path: str, test_type: str) -> str:
    """
    Creates a report file for a given test type.

    args:
        - report_folder_path: the path to the folder where the reports will be stored.
        - test_type: the type of tests being run.

    returns:
        - the path to the report file as a string.
    """
    report_file_path = f"{report_folder_path}/{test_type}_report.txt"
    with open(report_file_path, "w") as report_file:
        report_file.write(f"Test report for {test_type} tests.\n")
    return report_file_path


def main() -> None:
    """
    Runs all tests for the application.
    """
    report_folder_path = create_report_folder()
    for test_type, test_funcs in TESTING_FUNCTIONS.items():
        report_file_path = create_report_file(report_folder_path, test_type)
        run_tests(test_type, test_funcs, report_file_path)


if __name__ == "__main__":
    main()
