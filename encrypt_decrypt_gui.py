import os
from tkinter import *
from tkinter import filedialog, messagebox, simpledialog, ttk
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

# Function to generate a key from a password
def generate_key_from_password(password):
    salt = b'salt_for_password'  # You can randomize this for better security
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Function to generate a key and save it into a file
def generate_key():
    password = simpledialog.askstring("Password", "Enter a password to protect the key:", show='*')
    if not password:
        messagebox.showwarning("No Password", "Key generation canceled. No password provided.")
        return

    key = generate_key_from_password(password)
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generated", "New encryption key has been generated and saved.")

# Function to load the key from the current directory named `key.key`
def load_key():
    try:
        password = simpledialog.askstring("Password", "Enter the password to load the key:", show='*')
        if not password:
            messagebox.showwarning("No Password", "Key loading canceled. No password provided.")
            return None

        with open("key.key", "rb") as key_file:
            stored_key = key_file.read()

        # Verify the key by re-generating it with the password
        derived_key = generate_key_from_password(password)
        if stored_key != derived_key:
            messagebox.showerror("Error", "Incorrect password. Cannot load the key.")
            return None

        return stored_key
    except FileNotFoundError:
        messagebox.showerror("Error", "Key file not found. Please generate a key first.")
        return None

# Function to encrypt files
def encrypt_files():
    file_paths = filedialog.askopenfilenames(title="Select files to encrypt")
    if not file_paths:
        return  # User canceled the file dialog

    key = load_key()
    if not key:
        return

    fernet = Fernet(key)

    progress = Toplevel(root)
    progress.title("Encryption Progress")
    progress.geometry("300x100")
    Label(progress, text="Encrypting files...").pack(pady=10)

    # Customize the progress bar style
    style = ttk.Style()
    style.theme_use("default")  # Use the default theme for customization
    style.configure("green.Horizontal.TProgressbar", background="green")  # Set the bar color to green

    progress_bar = ttk.Progressbar(progress, orient="horizontal", length=200, mode="determinate",
                                   style="green.Horizontal.TProgressbar")  # Apply the custom style
    progress_bar.pack(pady=10)
    progress_bar["maximum"] = len(file_paths)

    try:
        for i, file_path in enumerate(file_paths):
            # Create a backup of the original file
            backup_dir = os.path.join(os.getcwd(), "backups")
            os.makedirs(backup_dir, exist_ok=True)
            backup_path = os.path.join(backup_dir, os.path.basename(file_path) + ".bak")

            with open(file_path, "rb") as original_file:
                with open(backup_path, "wb") as backup_file:
                    backup_file.write(original_file.read())

            # Encrypt the file
            with open(file_path, "rb") as file:
                file_data = file.read()

            encrypted_data = fernet.encrypt(file_data)

            with open(file_path, "wb") as file:
                file.write(encrypted_data)

            # Update progress bar
            progress_bar["value"] = i + 1
            progress.update_idletasks()

        messagebox.showinfo("Success", f"{len(file_paths)} file(s) have been encrypted.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to encrypt files: {e}")
    finally:
        progress.destroy()

# Function to decrypt files
def decrypt_files():
    file_paths = filedialog.askopenfilenames(title="Select files to decrypt")
    if not file_paths:
        return  # User canceled the file dialog

    key = load_key()
    if not key:
        return

    fernet = Fernet(key)

    progress = Toplevel(root)
    progress.title("Decryption Progress")
    progress.geometry("300x100")
    Label(progress, text="Decrypting files...").pack(pady=10)

    # Customize the progress bar style
    style = ttk.Style()
    style.theme_use("default")  # Use the default theme for customization
    style.configure("green.Horizontal.TProgressbar", background="green")  # Set the bar color to green

    progress_bar = ttk.Progressbar(progress, orient="horizontal", length=200, mode="determinate",
                                   style="green.Horizontal.TProgressbar")  # Apply the custom style
    progress_bar.pack(pady=10)
    progress_bar["maximum"] = len(file_paths)

    try:
        for i, file_path in enumerate(file_paths):
            with open(file_path, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = fernet.decrypt(encrypted_data)

            with open(file_path, "wb") as file:
                file.write(decrypted_data)

            # Update progress bar
            progress_bar["value"] = i + 1
            progress.update_idletasks()

        messagebox.showinfo("Success", f"{len(file_paths)} file(s) have been decrypted.")
    except Exception as e:
        messagebox.showerror("Decryption Failed", 
                             "Failed to decrypt the file. Ensure the file has not been modified after encryption "
                             "and that the correct key is being used.\n\nError Details: " + str(e))
    finally:
        progress.destroy()

# Function to display help/instructions
def show_help():
    help_message = (
        "How to Use This Tool Safely:\n\n"
        "1. Generate a Key:\n"
        "   - Click 'Generate Key' to create an encryption key (key.key).\n"
        "   - Protect the key with a password.\n\n"
        "2. Encrypt Files:\n"
        "   - Click 'Encrypt Files' and select the files you want to encrypt.\n"
        "   - Backups of the original files are saved in the 'backups' folder.\n\n"
        "3. Decrypt Files:\n"
        "   - Click 'Decrypt Files' and select the encrypted files.\n"
        "   - Never edit encrypted files directly. Always decrypt them first, make changes, and re-encrypt.\n\n"
        "4. Multiple Files:\n"
        "   - You can encrypt or decrypt multiple files at once."
    )
    messagebox.showinfo("Help", help_message)

# Create the main application window
root = Tk()
root.title("File Encryption and Decryption Tool")
root.geometry("400x300")

# Create and place widgets
Label(root, text="File Encryption and Decryption", font=("Arial", 16)).pack(pady=10)

Button(root, text="Generate Key", command=generate_key, width=20).pack(pady=5)
Button(root, text="Encrypt Files", command=encrypt_files, width=20).pack(pady=5)
Button(root, text="Decrypt Files", command=decrypt_files, width=20).pack(pady=5)
Button(root, text="Help", command=show_help, width=20).pack(pady=5)

# Run the application
root.mainloop()