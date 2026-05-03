import os
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def get_git_command(user_input):
    user_input = user_input.lower()

    if "push" in user_input:
        return "push"
    elif "pull" in user_input:
        return "pull"
    elif "status" in user_input:
        return "status"
    elif "clone" in user_input:
        return "clone"
    elif "branch" in user_input:
        return "branch"
    else:
        return "unknown"

def git_assistant():
    print("=== AI Git Assistant ===")
    user_input = input("Enter your Git request: ")

    action = get_git_command(user_input)

    if action == "push":
        repo_url = input("Enter GitHub Repository URL: ")
        commit_msg = input("Enter Commit Message: ")

        # Check if Git is initialized
        if not os.path.exists(".git"):
            run_command("git init")

        # Add all files
        run_command("git add .")

        # Commit files
        run_command(f'git commit -m "{commit_msg}"')

        # Set main branch
        run_command("git branch -M main")

        # Add remote only if not already added
        result = subprocess.run("git remote", shell=True, text=True, capture_output=True)
        if "origin" not in result.stdout:
            run_command(f"git remote add origin {repo_url}")
        else:
            print("Remote origin already exists.")

        # Push project
        run_command("git push -u origin main")

    elif action == "pull":
        run_command("git pull")

    elif action == "status":
        run_command("git status")

    elif action == "clone":
        repo_url = input("Enter Repository URL: ")
        run_command(f"git clone {repo_url}")

    elif action == "branch":
        branch_name = input("Enter Branch Name: ")
        run_command(f"git checkout -b {branch_name}")

    else:
        print("Command not recognized!")

if __name__ == "__main__":
    git_assistant()