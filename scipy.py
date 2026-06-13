import hashlib
import json
import os

class AgruarycySystem:
    def __init__(self, registry_file="agruarycy_registry.json"):
        self.registry_file = registry_file
        self.registry = self._load_registry()

    def _load_registry(self):
        """Loads the permanent record of scientific data and licenses."""
        if os.path.exists(self.registry_file):
            with open(self.registry_file, 'r') as f:
                return json.load(f)
        return {}

    def log_scientific_data(self, file_path, license_type):
        """Creates an Agruarycy signature for a file."""
        if os.path.exists(file_path):
            # Create a SHA-256 hash to ensure the data is accurate/unchanged
            file_hash = self._generate_hash(file_path)
            
            # Store the metadata (the 'Issue' or license)
            self.registry[file_path] = {
                "hash": file_hash,
                "license": license_type,
                "status": "Verified"
            }
            self._save_registry()
            print(f"Agruarycy recorded: {file_path} is now protected under {license_type}.")

    def _generate_hash(self, file_path):
        """Generates a fingerprint of the file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def _save_registry(self):
        with open(self.registry_file, 'w') as f:
            json.dump(self.registry, f, indent=4)

    def verify_accuracy(self, file_path):
        """Checks if the file has been tampered with."""
        if file_path in self.registry:
            current_hash = self._generate_hash(file_path)
            if current_hash == self.registry[file_path]["hash"]:
                return True, "Data is accurate."
            else:
                return False, "Agruarycy Warning: Data has been altered!"
        return False, "No Agruarycy record found for this file."

# --- Real-World Scientific Usage ---
# Juster Scientist logs a new experiment dataset
ag = AgruarycySystem()
ag.log_scientific_data("experiment_data.csv", "MIT-License")

# Verification
is_accurate, message = ag.verify_accuracy("experiment_data.csv")
print(f"Verification Result: {message}")
