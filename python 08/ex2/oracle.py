"""
Exercice
1 lire l exercice, lister les choses à apprendre
2 remplir le work instructions
3 Lire le w3school/autre concerne
4 réorganiser les instructions de façon claire et compréhensible avec une
checklist des éléments importants
X si exo long organiser la liste des choses a faire (objectif clair + feedback)
X regarder liste pauses

Si bloqué:
-Voir exemples
-réexpliquer par GPT
-arrêter de se casser le crâne à voir plus compliqué
-accepter que exo mal fait
-faire morceau par morceau et implémenter
---------------------------------------------
G [tutorials]
python-dotenv modules
gitignore
.env file

[authorized functions]
os, sys, python-dotenv modules, file operations

[needed files]
oracle.py, .env.example, .gitignore

XXX[exercise instructions - organized + general goal + explanation by gpt?]

-create a "secure system" with environment variables and .env files
-supposed to connect to external system without exposing vulnerable data
-use python-dotenv library and .env for configuration managment
-Do NOT implement custom parser

oracle.py
    -load config from environment variable
    -use a .env file for development setting
    -Demonstrates different configuration for development/production [???]
        -I can implement what I want to show difference, must be visible [???]
            -simple guess, react to differents .env and give different output
    -error handling for missing config

    Must handle:
        • MATRIX_MODE - "development" or "production"
        • DATABASE_URL - Connection string for data storage
        • API_KEY - Secret key for external services
        • LOG_LEVEL - Logging verbosity
        • ZION_ENDPOINT - URL for the resistance network

keep .env in gitignore, except a copy as .env.exemple


.env need python-dotenv (pip install python-dotenv)
    <from dotenv import load_dotenv> to import into the code



TODO[exercise instructions - to reorganize]


Configuration Requirements
Your program should handle these configuration variables:
• MATRIX_MODE - "development" or "production"
• DATABASE_URL - Connection string for data storage
• API_KEY - Secret key for external services
• LOG_LEVEL - Logging verbosity
• ZION_ENDPOINT - URL for the resistance network

Never commit real secrets to version control! Your .env file should
be in .gitignore. You must be able to explain why.



[Copy]
Your final mission is to create a secure configuration system using
environment variables and .env files. You’ll build a data pipeline that
connects to external systems safely.

You should use the python-dotenv library to load environment
variables from .env files. The goal is to learn how to use .env
files for configuration management, not to implement a custom parser.

Mission Briefing
Create a program called oracle.py that:
• Loads configuration from environment variables
• Uses a .env file for development settings
• Demonstrates different configuration for development/production
• Includes proper error handling for missing configuration

You are free to implement whatever you choose to showcase difference
in development/production. But it must be visible in the output when
testing your program.

Configuration Requirements
Your program should handle these configuration variables:
• MATRIX_MODE - "development" or "production"
• DATABASE_URL - Connection string for data storage
• API_KEY - Secret key for external services
• LOG_LEVEL - Logging verbosity
• ZION_ENDPOINT - URL for the resistance network

Never commit real secrets to version control! Your .env file should
be in .gitignore. You must be able to explain why.

G [general project instructions]
• Your project must be written in Python 3.10 or later.
• Your project must adhere to the flake8 coding standard.
• All code must include comprehensive type annotations. Check
this using mypy .
• Exception handling should protect the data streams from corruption.
• All standard classes and collections are authorized, along with their
methods (int, str, list, dict, etc.).
• All built-in functions are authorized.
• Test your programs in different environments (with/without virtual
env, with/without dependencies).


"""
