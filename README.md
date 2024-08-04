# CodePrep

CodePrep is a cross-platform Python application designed to help prepare and consolidate code for uploading to Claude or other AI assistants. It provides a user-friendly interface for selecting, processing, and formatting code files from various programming languages.

## Features

- Support for multiple programming languages (Python, Android, React, Flutter)
- Cross-platform compatibility (Windows and macOS)
- Drag-and-drop interface for easy file selection
- Code consolidation and formatting
- Masking rules for privacy protection
- Dark mode UI for comfortable usage

## Installation

### For Users

1. Go to the [Releases](https://github.com/yourusername/codeprep/releases) page of this repository.
2. Download the appropriate version for your operating system:
   - For Windows: `CodePrep-Windows.exe`
   - For macOS: `CodePrep-macOS`

### For Developers

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/codeprep.git
   cd codeprep
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Windows Users

1. Double-click the `CodePrep-Windows.exe` file to run the application.

Note: If you encounter a Windows Defender SmartScreen warning:
- Click "More info" and then "Run anyway" to proceed.
- This warning occurs because the application is not digitally signed. We are working on resolving this issue.

### macOS Users

1. Open Terminal and navigate to the directory containing the downloaded file.
2. Make the file executable by running:
   ```
   chmod +x CodePrep-macOS
   ```
3. Run the application:
   ```
   ./CodePrep-macOS
   ```

Note: If macOS prevents the application from running:
- Right-click (or Control-click) the app and select "Open".
- Click "Open" in the dialog box that appears.
- Future launches can be done by double-clicking.

### Using CodePrep

1. Select the programming language from the dropdown menu.
2. Drag and drop your code files or folders into the application.
3. (Optional) Add a masking rules file for privacy protection.
4. Click "Prepare Code for Claude" to process your files.
5. Select an output folder for the consolidated code.

## Development

CodePrep uses GitHub Actions for continuous integration and deployment. The workflow automatically builds the application for both Windows and macOS, and creates a release when a new version tag is pushed.

To create a new release:

1. Update the version number in your project (if applicable).
2. Commit your changes and push to the main branch.
3. Create and push a new tag:
   ```
   git tag v1.0.0
   git push origin v1.0.0
   ```

This will trigger the workflow to build the application for both platforms and create a new release with the executables attached.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Security Note

CodePrep is built using PyInstaller, which may cause some antivirus software to flag it as potentially unsafe. This is a false positive.

We are working on obtaining a code signing certificate to resolve this issue permanently. If you have concerns, you can review the source code in this repository and build the executable yourself using the provided build instructions.

## License

[MIT License](LICENSE)

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.