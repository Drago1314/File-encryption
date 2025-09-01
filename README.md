**Introduction**

This project involves the development of a Python-based file encryption and decryption tool designed to enhance data security. Utilizing symmetric encryption through the `cryptography` library, the tool ensures the confidentiality of sensitive files. A graphical user interface (GUI) built with Tkinter facilitates user-friendly interactions, enabling seamless encryption, decryption, and backup management. The application is designed for portability, allowing users to generate password-protected encryption keys and handle various file types without requiring additional dependencies.

**Objective**

The primary goals of this project are to strengthen programming proficiency and provide hands-on experience in the following areas:

* **File Encryption and Decryption**: Implementing secure encryption and decryption mechanisms using the `cryptography` library.
* **Graphical User Interface (GUI)**: Designing an intuitive user interface to streamline encryption and decryption processes.
* **Password Protection**: Employing password-based key derivation (PBKDF2HMAC) for secure encryption key management.
* **Backup Management**: Implementing an automated backup system to prevent accidental data loss.
* **Portability**: Packaging the application into a standalone executable for seamless deployment on Windows machines without requiring a Python environment.

**Relevance to the Course**

This project reinforces key technical competencies, including:

* **File Handling**: Efficiently managing binary file read/write operations for encryption and decryption.
* **Cryptography**: Applying industry-standard encryption techniques to ensure data security.
* **GUI Development**: Constructing an interactive and responsive interface using Tkinter and `ttkthemes`.
* **Error Handling**: Implementing exception handling mechanisms for incorrect passwords, corrupted files, and missing dependencies.
* **Software Deployment**: Utilizing PyInstaller to package the tool into a portable executable, demonstrating real-world software distribution strategies.

**Implementation**

### Encryption and Decryption Mechanism

* **Encryption**: The tool employs the Fernet symmetric encryption algorithm from the `cryptography` library. A unique encryption key is generated and protected via a user-defined password.
* **Decryption**: The decryption process utilizes the same key and password, ensuring data integrity and confidentiality.

### Secure Key Derivation

* The encryption key is derived using the PBKDF2HMAC algorithm with a fixed salt and 100,000 iterations for enhanced security.
* Users must input the correct password to generate or load the encryption key.

### Graphical User Interface

* The GUI provides options for key generation, file encryption, file decryption, and access to user instructions.
* Progress bars visually represent the encryption and decryption processes.

### Automated Backup System

* Prior to encryption, the tool generates a backup of the original file in a dedicated "backups" folder, allowing file recovery if necessary.

### Software Packaging

* The tool is compiled into a single executable using PyInstaller, ensuring portability and ease of distribution.

**Key Features**

* **File Encryption and Decryption**:

  * Supports common file formats, including `.txt`, `.jpg`, `.pdf`, `.docx`, etc.
  * Enables batch processing for handling multiple files simultaneously.
* **Password Protection**:

  * Encryption keys are secured using a user-defined password to prevent unauthorized access.
* **Automated Backup System**:

  * Generates backups in a dedicated "backups" folder to mitigate accidental data loss.
* **Progress Indicators**:

  * Displays progress bars to keep users informed during encryption and decryption.
* **Help & Documentation**:

  * A built-in "Help" section provides comprehensive usage instructions and security best practices.
* **Portability**:

  * The application runs as a standalone executable without requiring Python installation.

**Challenges and Solutions**

### Challenge 1: File Corruption During Encryption

* **Issue**: Editing an encrypted file results in irreversible corruption.
* **Solution**: Implemented user warnings within the GUI to prevent direct modification of encrypted files.

### Challenge 2: Password Management

* **Issue**: Users cannot decrypt files if they forget their password.
* **Solution**: Integrated clear instructions to remind users of password security best practices.

### Challenge 3: Packaging Dependencies

* **Issue**: Ensuring all required dependencies, such as `key.key` and the "backups" folder, are included in the packaged executable.
* **Solution**: Created a `.spec` file for PyInstaller to bundle necessary files, ensuring compatibility across different machines.

### Challenge 4: Cross-Platform Compatibility

* **Issue**: Ensuring the executable runs on various Windows configurations, including restricted environments like college PCs.
* **Solution**: Conducted extensive testing on multiple machines to verify dependency inclusion and execution stability.

**Conclusion**

### Project Summary

This project successfully demonstrates key cybersecurity principles, emphasizing secure file handling and encryption. Major takeaways include:

* **Hands-on Cryptography**: Practical experience with encryption algorithms and secure key management.
* **GUI Development**: Implementation of an intuitive, interactive interface.
* **Software Deployment**: Understanding the process of creating portable executables for real-world application.

### Lessons Learned

The development process highlighted the significance of:

* Thorough planning and testing to ensure data security and integrity.
* Comprehensive user guidance to prevent unintended misuse.
* Iterative debugging to address issues related to packaging and dependency management.

**References**

* **Python Official Documentation**: Comprehensive references for Tkinter, `cryptography`, and PyInstaller.
* **Cryptography Library**: [https://cryptography.io](https://cryptography.io)
* **PyInstaller Documentation**: [https://pyinstaller.org](https://pyinstaller.org)
* **Stack Overflow & Technical Forums**: Insights and solutions for encryption, GUI design, and software packaging.
* **Online Technical Tutorials**: Guides on developing encryption tools and creating standalone executables.

**Abstract**

This project presents the design and implementation of a Python-based file encryption and decryption tool aimed at enhancing data security. By leveraging the `cryptography` library, the tool enables symmetric encryption to safeguard confidential files. Core functionalities include password-protected key management, automated file backups, and an intuitive GUI built with Tkinter. Packaged as a standalone executable via PyInstaller, the tool ensures portability across Windows environments. Through this project, students gain practical experience in cryptography, secure file handling, GUI design, and software deployment, establishing a foundation for advanced cybersecurity applications.
