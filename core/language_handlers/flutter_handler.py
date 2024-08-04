from .base_handler import BaseLanguageHandler

class FlutterHandler(BaseLanguageHandler):
    def get_output_files(self, output_folder):
        return {'flutter': self._create_output_file(output_folder, "flutter_code")}

    def process_content(self, content):
        # Add Flutter-specific processing here if needed
        return content

    def write_to_output(self, output_files, relative_path, content):
        self._write_to_file(output_files['flutter'], relative_path, content)
        return 'flutter'