# GitHub Trending Repositories CLI

A Python command-line tool that interacts with the GitHub REST API to fetch and display popular GitHub repositories based on their creation date.

Users can select a time range (day, week, month, or year) and specify the number of repositories they want to retrieve.

## Features

- Fetch repositories using the GitHub REST API.
- Filter repositories by creation date.
- Support four time ranges: day, week, month, and year.
- Sort repositories by star count.
- Customize the number of results.
- Display repository names and star counts.
- Basic API error handling.

## Technologies Used

- Python
- Requests
- Argparse
- Datetime
- GitHub REST API

## Project Structure

```text
github-trending/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/github-trending.git
```

**2. Navigate to the project directory**

```bash
cd github-trending
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**5. Install dependencies**

```bash
pip install requests
```

## Usage

Run the application using:

```bash
python main.py
```

### Specify a duration

```bash
python main.py --duration day
```

Supported durations:

| Argument | Description |
|---|---|
| `day` | Last 1 day |
| `week` | Last 7 days |
| `month` | Last 30 days |
| `year` | Last 365 days |

### Specify the number of repositories

```bash
python main.py --limit 20
```

### Combine arguments

```bash
python main.py --duration month --limit 20
```

Default values:

- Duration: week
- Limit: 10

## Example Output

```text
repo: developer/project-one
stars: 1500
----------------------------------------

repo: developer/project-two
stars: 1200
----------------------------------------
```

## How It Works

1. The user provides command-line arguments.
2. Argparse extracts the selected duration and result limit.
3. Python's datetime module calculates the starting date.
4. The application constructs a GitHub repository search query.
5. Requests sends an HTTP GET request to the GitHub REST API.
6. The API returns repository information in JSON format.
7. Python extracts and displays the repository names and star counts.

## API Reference

GitHub Search Repositories API:

https://docs.github.com/en/rest/search/search#search-repositories

## Important Note

This project filters repositories by their creation date and sorts them by total stars.

It identifies popular recently created repositories, rather than measuring the number of stars gained during the selected period.

## Roadmap URL

https://roadmap.sh/projects/github-trending-cli

## Future Improvements

- Add programming language filters.
- Display repository descriptions and GitHub URLs.
- Add pagination.
- Improve API exception handling.
- Add GitHub API authentication.
- Add unit tests.
- Improve terminal output formatting.

## License

This project is licensed under the MIT License.
