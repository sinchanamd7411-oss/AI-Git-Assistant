import os
import subprocess

# Run terminal commands safely
def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        if e.stderr:
            print("Error:", e.stderr)
        return False

# Detect user intent
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

# Check if Git is installed
def check_git_installed():
    try:
        subprocess.run(
            "git --version",
            shell=True,
            check=True,
            capture_output=True
        )
        return True
    except:
        print("Git is not installed.")
        return False

# Main AI Git Assistant
def git_assistant():
    if not check_git_installed():
        return

    print("=== AI Git Assistant ===")
    user_input = input("Enter your Git request: ")

    action = get_git_command(user_input)

    # PUSH PROJECT
    if action == "push":
        repo_url = input("Enter GitHub Repository URL: ").strip()
        commit_msg = input("Enter Commit Message: ").strip()

        # Validate URL
        if not repo_url.startswith("https://github.com/"):
            print("Invalid GitHub URL.")
            return

        # Auto-fix missing .git
        if not repo_url.endswith(".git"):
            repo_url += ".git"

        # Default commit message
        if not commit_msg:
            commit_msg = "Auto Commit"

        # Initialize repo if missing
        if not os.path.exists(".git"):
            print("Initializing Git repository...")
            if not run_command("git init"):
                return

        # Add .gitignore if missing
        if not os.path.exists(".gitignore"):
            with open(".gitignore", "w") as file:
                file.write(".env\n__pycache__/\n")
            print(".gitignore created.")

        # Stage files
        if not run_command("git add ."):
            return

        # Commit changes
        commit_success = run_command(f'git commit -m "{commit_msg}"')

        # If no changes, continue push
        if not commit_success:
            print("No new changes or commit issue. Continuing...")

        # Rename branch
        run_command("git branch -M main")

        # Check remote
        result = subprocess.run(
            "git remote",
            shell=True,
            text=True,
            capture_output=True
        )

        # Replace old remote automatically
        if "origin" in result.stdout:
            print("Updating existing remote origin...")
            run_command("git remote remove origin")

        # Add new remote
        if not run_command(f"git remote add origin {repo_url}"):
            return

        # Push project
        print("Pushing project to GitHub...")
        if not run_command("git push -u origin main"):
            print("Push failed. Check repository, internet, or authentication.")
            return

        print("Project pushed successfully!")

    # PULL PROJECT
    elif action == "pull":
        if not os.path.exists(".git"):
            print("Not a Git repository.")
            return
        run_command("git pull")

    # STATUS
    elif action == "status":
        if not os.path.exists(".git"):
            print("Not a Git repository. Initializing now...")
            run_command("git init")
        run_command("git status")

    # CLONE
    elif action == "clone":
        repo_url = input("Enter Repository URL: ").strip()

        if not repo_url:
            print("Repository URL required.")
            return

        if not repo_url.endswith(".git"):
            repo_url += ".git"

        run_command(f"git clone {repo_url}")

    # BRANCH
    elif action == "branch":
        if not os.path.exists(".git"):
            print("Not a Git repository.")
            return

        branch_name = input("Enter Branch Name: ").strip()

        if not branch_name:
            print("Branch name required.")
            return

        run_command(f"git checkout -b {branch_name}")

    # UNKNOWN
    else:
        print("Command not recognized!")
        print("Try: push, pull, status, clone, branch")

# Run app
if __name__ == "__main__":
    git_assistant()