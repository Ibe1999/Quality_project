from github import Github
import matplotlib.pyplot as plt
import os

# Get GitHub token from environment variable
token = os.getenv('GITHUB_TOKEN')

# List of repositories to analyze
repositories = ["gilito11/BetterHealth4"]

# Authenticate with GitHub API
g = Github(token)

def count_labels(repo):
    """Count the number of issues for each label in a repository."""
    labels_count = {}
    for issue in repo.get_issues(state="all"):
        for label in issue.labels:
            labels_count[label.name] = labels_count.get(label.name, 0) + 1
    return labels_count

def generate_plot(repo_name, labels_count):
    """Generate and save a histogram of issue labels."""
    if not labels_count:
        print(f"No labeled issues found in {repo_name}.")
        return None  

    plt.figure(figsize=(10, 6))
    plt.bar(labels_count.keys(), labels_count.values(), color='b')
    plt.ylabel('Number of Issues')
    plt.xlabel('Labels')
    plt.title(f'Histogram of Issues by Label - {repo_name}')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()

    filename = f"{repo_name.replace('/', '_')}_histogram.png"
    plt.savefig(filename)
    print(f"Histogram saved as {filename}")
    return filename  

def main():
    for repo_name in repositories:
        try:
            repo = g.get_repo(repo_name)
            print(f"Processing repository: {repo_name}")
            labels_count = count_labels(repo)
            filename = generate_plot(repo_name, labels_count)
            if filename:
                print(f"Histogram file created: {filename}")
        except Exception as e:
            print(f"Error processing {repo_name}: {e}")

if __name__ == '__main__':
    main()
