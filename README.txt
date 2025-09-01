File Encryption and Decryption Tool
===================================

This tool allows you to encrypt and decrypt files securely using a password-protected key.

Requirements:
-------------
- Ensure the executable (`encrypt_decrypt_gui.exe`) is in the same folder as the `key.key` file.
- If you are decrypting files, ensure the `key.key` file matches the one used for encryption.

How to Use:
-----------
1. Generate a Key:
   - Click "Generate Key" and enter a password.
   - The key will be saved as `key.key`.

2. Encrypt Files:
   - Click "Encrypt Files" and select the files you want to encrypt.
   - A backup of the original files will be saved in the `backups` folder.

3. Decrypt Files:
   - Click "Decrypt Files" and select the encrypted files.
   - Enter the password used to generate the key.

Important Notes:
----------------
- Do not edit encrypted files directly. Always decrypt them first, make changes, and re-encrypt.
- Keep the `key.key` file safe. Without it, you cannot decrypt your files.
- The `backups` folder contains unencrypted copies of your files for recovery.

Troubleshooting:
----------------
- If the program doesn't work, ensure all required files (`key.key`, `backups`) are in the same folder as the executable.
- If you encounter antivirus warnings, whitelist the executable.

Contact:
--------
For support, contact Faazil Mirza at faazil.231849.ci@mhssce.ac.in.