from huggingface_hub import HfApi, HfFolder, Repository
import os

# Set your token securely via GitHub Secrets or environment
token = os.getenv("HF_TOKEN")
repo_id = "pgajavalli95/superkart-model"

# Save model locally
os.makedirs("model", exist_ok=True)
with open("model/dummy_model.txt", "w") as f:
    f.write("This is a placeholder for your trained model.")

# Push to Hugging Face
api = HfApi()
api.create_repo(repo_id=repo_id, token=token, exist_ok=True)
repo = Repository(local_dir="model", clone_from=repo_id, use_auth_token=token)
repo.push_to_hub()
