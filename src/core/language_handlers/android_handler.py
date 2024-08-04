import os
from .base_handler import BaseLanguageHandler

class AndroidHandler(BaseLanguageHandler):
    def get_output_files(self, output_folder):
        return {
            'code': self._create_output_file(output_folder, "android_code"),
            'xml': self._create_output_file(output_folder, "android_xml")
        }

    def process_content(self, content):
        lines = content.split('\n')
        return '\n'.join([line for line in lines if not line.strip().startswith(('package', 'import'))])

    def write_to_output(self, output_files, relative_path, content):
        if relative_path.endswith(('.kt', '.java')):
            self._write_to_file(output_files['code'], relative_path, content)
            return 'code'
        elif relative_path.endswith('.xml'):
            self._write_to_file(output_files['xml'], relative_path, content)
            return 'xml'
        return None

    def _write_to_file(self, file_path, relative_path, content):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n# File: {relative_path}\n")
            f.write("```\n")
            f.write(content)
            f.write("\n```\n")