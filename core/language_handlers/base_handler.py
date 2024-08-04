from abc import ABC, abstractmethod
from datetime import datetime
import os

class BaseLanguageHandler(ABC):
    @abstractmethod
    def get_output_files(self, output_folder):
        pass

    @abstractmethod
    def process_content(self, content):
        pass

    @abstractmethod
    def write_to_output(self, output_files, relative_path, content):
        pass

    def _get_timestamp(self):
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def _create_output_file(self, output_folder, prefix):
        timestamp = self._get_timestamp()
        return os.path.join(output_folder, f"{prefix}_{timestamp}.txt")

    def _write_to_file(self, file_path, relative_path, content):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n# File: {relative_path}\n")
            f.write("```\n")
            f.write(content)
            f.write("\n```\n")