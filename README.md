
## Password Manager

This is a simple password manager built using Python and the Tkinter library. The app helps users securely store their website credentials (email and password) in a JSON file, with the ability to generate strong passwords and retrieve saved passwords by searching for specific websites.

---

## Features

- **Password Generation**: Automatically generates a random, secure password containing letters, numbers, and special symbols.
- **Password Storage**: Stores website credentials (email and password) in a JSON file.
- **Search Password**: Retrieve stored passwords for a specific website.
- **Clipboard Integration**: Copy the generated password to the clipboard for easy use.
- **Data Storage**: Saves all the credentials securely in a JSON file for persistence.
- **User-Friendly Interface**: Easy-to-use GUI built with Tkinter for an interactive experience.

---

## How It Works

1. **Password Generator**:
   - Generates a random password consisting of uppercase letters, lowercase letters, numbers, and special symbols.
   - Automatically copies the generated password to the clipboard for easy use.

2. **Store Credentials**:
   - Input the website, email/username, and password to be saved.
   - The credentials are saved in a `mydata.json` file, which keeps your information securely organized.

3. **Search Password**:
   - Search for saved credentials by entering the website name.
   - Displays the corresponding email/username and password associated with the website.

---

## Setup

### Requirements:
- Python 
- Tkinter (usually included in standard Python distributions)
- pyperclip (for clipboard functionality)
  
Install the required package via:
```bash
pip install pyperclip
```

### Running the Application:
1. Clone the repository:
   ```bash
   git clone https://github.com/Sanjula2005/Password_Manager_Tkinter_app.git
   cd Password_Manager_Tkinter_app
   ```

2. Run the Python script:
   ```bash
   python main.py
   ```

---

## Application Walkthrough

### **UI Elements:**
- **Website**: The name of the website for which you want to save credentials.
- **Email/Username**: Your email or username associated with the website.
- **Password**: The password for the website.
- **Generate Password**: Button to generate a random password.
- **Add**: Button to save the entered website credentials.
- **Search**: Button to search for saved credentials by the website name.

### **How to Use:**
- **To Generate a Password**: Click on the "Generate password" button. A strong random password will be generated and copied to your clipboard.
- **To Save Credentials**: Enter the website name, email/username, and password, then click "Add" to save them in the JSON file.
- **To Search for Credentials**: Enter the website name and click "Search" to retrieve the associated email/username and password.

---

## File Structure

The application saves your credentials in the `mydata.json` file, which stores the data in the following format:

```json
{
    "website_name": {
        "email": "your_email@example.com",
        "password": "your_password"
    }
}
```

---

## Notes

- Ensure that the `mydata.json` file is in the same directory as the script for the app to work properly.
- The app saves data in a local file, so please ensure you keep it secure.
- The password generator creates a strong password with a mix of letters, numbers, and special characters for added security.

---
