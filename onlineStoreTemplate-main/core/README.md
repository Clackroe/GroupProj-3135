# Core Directory

In this directory, general functionality files are stored. Note that these are not the files for running or testing the application, but rather the group of files that can contribute to a wide range of application functionality.

## session.py File

To encourage modularity in session management functionality expansions, the `session.py` file is located in this directory. This file contains the classes `UserSession` and `Sessions`, which are used to manage user sessions. The `UserSession` class is used to create a session for a user, and the `Sessions` class is used to manage all sessions for the application. The `Sessions` class is intended to be treated as a singleton, though the `UserSession` class is not. If a student is interested in refactoring the session management functionality to support the singleton pattern, this would be an impressive but challenging addition to the codebase.

## utils.py File

This file contains a few utility functions that are used throughout the application. Aside from their ubiquity in the codebase, functions in this file do not necessarily have a connection to each other. This is a great place to house loose, unstructured feature implementations that do not fit well with other files when completing your group's project.
