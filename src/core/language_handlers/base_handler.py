from abc import ABC, abstractmethod
import os
from datetime import datetime

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