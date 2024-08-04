# CodePrep

CodePrep is a Python application designed to help prepare and consolidate code for uploading to Claude or other AI assistants. It provides a user-friendly interface for selecting, processing, and formatting code files from various programming languages.

## Features

- Support for multiple programming languages (Python, Android, React, Flutter)
- Drag-and-drop interface for easy file selection
- Code consolidation and formatting
- Masking rules for privacy protection
- Dark mode UI for comfortable usage

## Installation

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

Run the application:

```
python src/main.py
```

1. Select the programming language from the dropdown menu.
2. Drag and drop your code files or folders into the application.
3. (Optional) Add a masking rules file for privacy protection.
4. Click "Prepare Code for Claude" to process your files.
5. Select an output folder for the consolidated code.

## Development

CodePrep uses GitHub Actions for continuous integration and deployment. The workflow automatically builds the application and creates a release when a new version tag is pushed.

To create a new release:

1. Update the version number in your project (if applicable).
2. Commit your changes and push to the main branch.
3. Create and push a new tag:
   ```
   git tag v1.0.0
   git push origin v1.0.0
   ```

This will trigger the workflow to build the application and create a new release with the executable attached.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.