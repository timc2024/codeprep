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