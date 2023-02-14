 # User authentication system that allows the creation and login of user accounts.

This code uses Python to create an SQLite database and allow users to create accounts and then log in to them.

When running the code, the user will be prompted to indicate whether they want to create a new account or sign in to an existing account. If they select "y" to create an account, they will be prompted to enter a username, email address, and password.

The password must have at least 4 characters, a capital letter, a number and no more than 10 characters. The password is encrypted and added to the database along with the username, email address, and a unique random salt.

Before adding a new account to the database, the code checks if the username and email address already exist in the database. If a duplicate username or email address is found, the user is notified and the account is not added to the database.

If the user selects "n" to log in, they will be prompted to enter their email address and password. The code checks that the email address is valid and then adds the salt that is on the same line as the email and uses the hash function to check if the password entered is correct for that account. If the email address and password are correct, a welcome message is displayed with the corresponding username. If they are not correct, the user is informed that the wrong credentials were entered.
