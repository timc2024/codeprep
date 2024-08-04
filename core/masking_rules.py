class MaskingRules:
    def __init__(self):
        self.rules = []

    def load_from_file(self, file_path):
        self.rules = []
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('->')
                if len(parts) == 2:
                    original = parts[0].strip()
                    masked = parts[1].strip()
                    self.rules.append((original, masked))

    def apply_masking(self, content):
        for original, masked in self.rules:
            content = content.replace(original, masked)
        return content