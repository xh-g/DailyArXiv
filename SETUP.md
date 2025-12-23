# DailyArXiv Setup Guide

## Overview

DailyArXiv is an automated tool that fetches the latest research papers from arXiv based on your specified keywords and generates a formatted README with the results. The project is designed to run automatically via GitHub Actions, but can also be run manually.

## Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git (for version control)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/xh-g/DailyArXiv.git
   cd DailyArXiv
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   The project requires:
   - `easydict` - For easy dictionary access
   - `feedparser` - For parsing arXiv API responses
   - `pytz` - For timezone handling

3. **Verify your setup** (optional)
   ```bash
   python verify_setup.py
   ```
   
   This script will check that all dependencies are installed and files are in place.

### Configuration

Before running the project, you need to customize the keywords to match your research interests.

1. **Edit `main.py`** to set your keywords (line 25):
   ```python
   keywords = ["Time Series", "Trajectory", "Graph Neural Networks"]
   ```

2. **Optional configurations** in `main.py`:
   - `max_result` (line 27): Maximum papers to fetch per keyword (default: 200)
   - `issues_result` (line 28): Maximum papers in GitHub issue (default: 20)
   - `column_names` (line 33): Columns to display in the output

### Running the Project

#### Manual Execution

Run the script to fetch papers and update the README:

```bash
python main.py
```

This will:
1. Fetch the latest papers from arXiv for each keyword
2. Generate a formatted markdown table
3. Update `README.md` with the results
4. Update `.github/ISSUE_TEMPLATE.md` with a summary

**Note:** The script backs up existing `README.md` and `ISSUE_TEMPLATE.md` files before updating them.

#### Automated Execution (GitHub Actions)

The project includes a GitHub Actions workflow (`.github/workflows/update.yaml`) that automatically:
- Runs every weekday at 00:30 Beijing time (16:30 UTC, Monday-Friday)
- Fetches new papers
- Updates the repository
- Creates an issue to notify about updates

**To enable automated execution:**
1. Ensure the workflow file has proper permissions
2. The workflow is already configured in `.github/workflows/update.yaml`
3. No additional setup is needed - it will run automatically

## How It Works

### Keyword Search

The project searches for papers on arXiv using the following logic:
- **Multi-word keywords**: Uses OR logic (papers containing the keyword in title OR abstract)
- **Single-word keywords**: Uses AND logic (papers containing the keyword in both title AND abstract)

### Paper Filtering

- Only papers in Computer Science (`cs.*`) and Statistics (`stat.*`) fields are included
- Papers are sorted by last update date (most recent first)
- Up to `max_result` papers per keyword are fetched

### Output Format

The generated `README.md` includes:
- **Title** (linked to arXiv)
- **Date** (last update date)
- **Abstract** (collapsed, click to expand)
- **Comment** (if available)

Papers are organized by keyword section.

## File Structure

```
DailyArXiv/
├── main.py                          # Main script
├── utils.py                         # Utility functions
├── requirements.txt                 # Python dependencies
├── README.md                        # Auto-generated paper list
├── .github/
│   ├── workflows/
│   │   └── update.yaml             # GitHub Actions workflow
│   └── ISSUE_TEMPLATE.md           # Auto-generated issue template
└── SETUP.md                         # This setup guide
```

## Customization

### Adding More Keywords

Edit `main.py` and add your keywords to the list:
```python
keywords = [
    "Time Series",
    "Trajectory",
    "Graph Neural Networks",
    "Your New Keyword",
    "Another Keyword"
]
```

### Changing Display Columns

Modify `column_names` in `main.py`:
```python
# Available columns: Title, Authors, Abstract, Link, Tags, Comment, Date
column_names = ["Title", "Link", "Date", "Comment"]
```

### Adjusting Paper Limits

```python
max_result = 200      # Papers to fetch per keyword
issues_result = 20    # Papers to show in GitHub issues
```

### Changing Update Schedule

Edit `.github/workflows/update.yaml`:
```yaml
schedule:
  - cron: '30 16 * * 0-4'  # Modify this cron expression
```

## Troubleshooting

### Verify Your Setup

Before troubleshooting, run the verification script to check your setup:
```bash
python verify_setup.py
```

This will help identify any missing dependencies or configuration issues.

### Common Issues

1. **ModuleNotFoundError**: Run `pip install -r requirements.txt`

2. **Network errors when fetching papers**: 
   - The arXiv API may be temporarily unavailable
   - The script includes retry logic with 30-minute waits
   - Check your internet connection

3. **Empty paper list returned**:
   - The arXiv API occasionally returns empty results
   - The script automatically retries up to 6 times
   - Try running the script again later

4. **GitHub Actions not running**:
   - Check repository permissions (Settings > Actions > General)
   - Verify the workflow file is in `.github/workflows/`
   - Check the Actions tab for error logs

### Getting Help

If you encounter issues:
1. Check the error messages in the console or GitHub Actions logs
2. Verify all dependencies are installed correctly
3. Ensure your Python version is 3.9 or higher
4. Review the arXiv API documentation: https://arxiv.org/help/api/

## Advanced Usage

### Running with Custom Date

The script uses Beijing timezone (Asia/Shanghai) by default. To modify:

Edit `main.py` line 10:
```python
beijing_timezone = pytz.timezone('Your/Timezone')
```

### Backup and Restore

The script automatically backs up files before updating:
- `README.md` → `README.md.bk`
- `.github/ISSUE_TEMPLATE.md` → `.github/ISSUE_TEMPLATE.md.bk`

If the script fails, it automatically restores from backups.

### Manual Backup Removal

After a successful run, backups are automatically removed. If you need to manually clean up:
```bash
rm README.md.bk .github/ISSUE_TEMPLATE.md.bk
```

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

Please check the repository for license information.

## Credits

Original project structure inspired by research paper tracking needs in the machine learning community.
