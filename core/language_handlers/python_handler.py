from .base_handler import BaseLanguageHandler

class PythonHandler(BaseLanguageHandler):
    def get_output_files(self, output_folder):
        return {'python': self._create_output_file(output_folder, "python_code")}

    def process_content(self, content):
        lines = content.split('\n')
        return '\n'.join([line for line in lines if not line.strip().startswith('import')])

    def write_to_output(self, output_files, relative_path, content):
        self._write_to_file(output_files['python'], relative_path, content)
        return 'python'