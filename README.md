pdf protector

This Python application allows you to protect PDF files with a password using the PyPDF2 library. It provides a graphical user interface (GUI) for ease of use, 
allowing you to select a PDF file, set a password, and save the protected PDF.

Features
-Simple GUI to select a source PDF file.
-Option to set a password to protect the PDF.
-Output the protected PDF file to a new file.
-Clear error handling and validation.

Prerequisites
Before running the application, you need to have Python installed on your machine along with the following libraries:

-Tkinter: For creating the graphical user interface.
-PyPDF2: For reading, writing, and encrypting PDFs.

Installation
-Install Python from the official website: python.org.
-Install the required libraries using pip.

the application will open a window where you can:

-Select Source PDF: Choose the PDF you want to protect.
-Target PDF: Enter the filename for the protected PDF.
-Set User Password: Enter a password to protect the PDF.
-Click on the "Protect PDF File" button to apply the password protection to the selected PDF. Once successful, a message will appear confirming the completion.

Error Handling
-Empty Fields: If any fields are left empty (source PDF, target file, or password), the user will be shown an error message prompting them to fill in the missing information.
-Invalid Entries: If an invalid PDF is selected or the operation fails, an error message will appear.



