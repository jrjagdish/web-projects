# GitHub User Events Fetcher

## Overview
This Python program fetches and displays the latest events (such as commits, issues, starred repositories) of a given GitHub user. It retrieves data from GitHub's API and formats the output for easy readability.

## Features
- Fetches recent events of a GitHub user.
- Displays up to the latest 5 events.
- Supports event types like `CreateEvent`, `PushEvent`, `IssuesEvent`, and `WatchEvent` (starred).
- Handles invalid usernames gracefully with error messages.
- Includes unit tests to validate functionality.

## Installation
Ensure you have Python installed (>=3.6). Then, clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/yourusername/github-events-fetcher.git
cd github-events-fetcher

# Install dependencies
pip install -r requirements.txt
```

## Usage
Run the program by providing a GitHub username:

```bash
python main.py <github_username>
```

Example:
```bash
python main.py octocat
```

## File Structure
```
.
├── fetch.py        # Fetches events from GitHub API
├── display.py      # Formats and displays events
├── getname.py      # Parses command-line arguments
├── main.py         # Entry point of the program
├── test.py         # Unit tests for validation
├── requirements.txt # Required dependencies
├── README.md       # Documentation
```

## Error Handling
- If an invalid GitHub username is provided, the program displays an error.
- If the GitHub API request fails, it logs the error message.

## Testing
Run unit tests using:
```bash
python -m unittest test.py
```

## Contributing
Feel free to fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

---

Developed by [Jagdish]
