import os
from .base_handler import BaseLanguageHandler

class ReactHandler(BaseLanguageHandler):
    def get_output_files(self, output_folder):
        return {'react': self._create_output_file(output_folder, "react_code")}

    def process_content(self, content):
        # Add React-specific processing here if needed
        return content

    def write_to_output(self, output_files, relative_path, content):
        self._write_to_file(output_files['react'], relative_path, content)
        return 'react'

    def _write_to_file(self, file_path, relative_path, content):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n# File: {relative_path}\n")
            f.write("```jsx\n")
            f.write(content)
            f.write("\n```\n")