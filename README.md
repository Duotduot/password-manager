[Link To Git repository](https://github.com/Duotduot/password-manager)

PEP 8 is the style guide used in this application. Some of the PEP 8 styling conventions used include:  
- Using 4 spaces for indentation  
- Using comments in the code. Also writing them on a separate line  
- Descriptive variable names  
- Consistent naming convention for functions, classes and modules.  

## FEATURES  
1. **Add password**- This feature allows the user to add a new password to the password manager. The user will be prompted to enter a site name and password, and the password will be encrypted and stored in the password manager's dictionary. The application will also write the updated password data to a JSON file on disk. This feature demonstrates the use of variables and variable scope to store and modify password data, as well as the use of error handling to catch file write errors.  
2. **Show password**- This feature allows the user to retrieve a saved password from the password manager. The user will be prompted to enter a site name, and the application will check if the site name is present in the password manager's dictionary. If the site name is found, the corresponding encrypted password will be retrieved, decrypted, and printed to the console. If the site name is not found, the application will notify the user. This feature demonstrates the use of conditional control structures to check for the presence of site names in the password manager's dictionary.   
3. **Delete password**- This feature allows the user to delete a saved password from the password manager. The user will be prompted to enter a site name, and the application will check if the site name is present in the password manager's dictionary. If the site name is found, the corresponding password will be deleted from the dictionary and the updated password data will be written to the JSON file. If the site name is not found, the application will notify the user. This feature demonstrates the use of loops and conditional control structures to search for and delete password data from the password manager's dictionary, as well as the use of error handling to catch file write errors.  