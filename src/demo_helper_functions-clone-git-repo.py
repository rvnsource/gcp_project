# TODO in ipynb: pip install gitpython magika

import os
import shutil
from pathlib import Path
import git
import magika

m = magika.Magika()

def clone_repo(repo_url, repo_dir):
    """Clone a GitHub repository."""
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)         # rm -rf <dir>

    os.makedirs(repo_dir)
    git.Repo.clone_from(repo_url, repo_dir)


def extract_code(repo_dir):
    """Create code index and extract the content of source files from a GitHub repository."""
    code_index = []
    code_text = ""
    for root, dirs, files in os.walk(repo_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, repo_dir)
            code_index.append(relative_path)

            file_type = m.identify_path(Path(file_path))
            if file_type.output.group in ("text", "code"):
                try:
                    with open(file_path, "r") as f:
                        code_text += f"----- File: {relative_path} -----\n"
                        code_text += f.read()
                        code_text += "\n-------------------------\n"
                except Exception:
                    pass

    return code_index, code_text

def get_code_prompt(question):
    """Generates a prompt to a code related question."""

    prompt = f"""
    Questions: {question}

    Context:
    - The entire codebase is provided below.
    - Here is an index of all of the files in the codebase:
      \n\n{code_index}\n\n.
    - Then each of the files is concatenated together. You will find all of the code you need:
      \n\n{code_text}\n\n

    Answer:
  """

    return prompt

if __name__ == "__main__":
    # GitHub repo url
    repo_url = "https://github.com/GoogleCloudPlatform/microservices-demo"

    # Location to clone the above git repo.
    repo_dir = "./repo"

    # clone_repo(repo_url, repo_dir)

    code_index, code_text = extract_code(repo_dir)


    prompt = get_code_prompt("Provide a getting started guide to onboard new developers to the codebase ")


    print("Done")
