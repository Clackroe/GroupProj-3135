# Authentication Directory

This directory contains the files for user authentication. The intention here is to follow a salt protocol for hashing user passwords and to prepare them for database storage. There are intentional redundancies in this section of the codebase that present potential security vulnerabilities. This is done as a learning exercise for students to identify and fix these vulnerabilities, if they choose to do so as a part of their project.

## authTools.py File

This script contains functions that modify the `passwords.txt` file, handle password hashing under the SHA-512 algorithm. Students are encouraged to explore the `hashlib` library before attempting to implement new features in this file.

## passwords.txt File

This file is where relevant hashes and other information are stored. Pay close attention to the format of this file, as the delimiters are unique.
