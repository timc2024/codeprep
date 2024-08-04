from core.language_handlers import get_language_handler
from utils.file_utils import read_file

class FileProcessor:
    def __init__(self):
        self.language_handler = None

    def set_language_handler(self, language):
        self.language_handler = get_language_handler(language)

    def process_files(self, files, relative_files, output_folder, masking_rules):
        if not self.language_handler:
            raise ValueError("Language handler not set")

        output_files = self.language_handler.get_output_files(output_folder)
        generated_files = set()

        for file_path, relative_path in zip(files, relative_files):
            content = read_file(file_path)
            if masking_rules and masking_rules.rules:
                content = masking_rules.apply_masking(content)
            processed_content = self.language_handler.process_content(content)
            file_type = self.language_handler.write_to_output(output_files, relative_path, processed_content)
            if file_type and file_type in output_files:
                generated_files.add(output_files[file_type])

        return list(generated_files)