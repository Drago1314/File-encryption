# File Encryption and Decryption Tool

A Python-based file encryption and decryption tool with a graphical user interface, designed for secure file handling using symmetric encryption.

## Features

- Symmetric Encryption -- Uses Fernet (AES-128-CBC) from the cryptography library
- Password-Protected Keys -- PBKDF2-HMAC key derivation with 100,000 iterations
- GUI Interface -- Tkinter-based interface with progress bars and themed widgets
- Automated Backups -- Creates backups before encryption to prevent data loss
- Multi-Format Support -- Encrypts .txt, .jpg, .pdf, .docx, and more
- Batch Processing -- Handle multiple files simultaneously
- Portable Executable -- Packaged with PyInstaller for standalone use

## Quick Start

### From Source
```bash
# Clone the repo
git clone https://github.com/Drago1314/File-encryption.git
cd File-encryption

# Install dependencies
pip install cryptography ttkthemes

# Run the tool
python encrypt_decrypt_gui.py
```

### Standalone Executable
Download the latest release and run encrypt_decrypt_gui.exe -- no Python installation required.

## How It Works

1. Generate Key -- Create a password-protected encryption key
2. Select Files -- Choose file(s) to encrypt or decrypt
3. Process -- Watch progress bar as files are encrypted/decrypted
4. Backup -- Original files backed up automatically in backups/ folder

## Important Notes

- Never forget your password -- files cannot be decrypted without it
- Don't edit encrypted files -- binary modification causes irreversible corruption
- Keep key.key safe -- losing it means losing access to encrypted files

## Tech Stack

- Python 3.12 -- Core language
- cryptography -- Fernet symmetric encryption
- Tkinter + ttkthemes -- GUI framework
- PyInstaller -- Executable packaging

## License

This project is licensed under the MIT License -- see the LICENSE file for details.

## Author

Faazil Mirza Shaikh
B.E. Computer Science -- M.H. Saboo Siddik College of Engineering, Mumbai
