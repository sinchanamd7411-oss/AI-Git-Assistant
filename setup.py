from setuptools import setup, find_packages

setup(
    name="push-this-project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "push-this-project=ai_git_assistant.main:git_assistant",
        ],
    },
    author="Sinchana",
    description="Natural Language Git Automation Tool",
)