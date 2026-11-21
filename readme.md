
```
# GitHub MCP Server

A Model Context Protocol (MCP) server that integrates with the GitHub REST API to retrieve repository information, issues, and pull requests through MCP tools.

## 1. Project Architecture

The project follows a simple client-server architecture where an MCP client communicates with the GitHub MCP server, and the server interacts with the GitHub REST API.

## 2. Project Workflow

1. Initialize the MCP server using FastMCP.
2. Load environment variables from the `.env` file.
3. Define GitHub API request headers.
4. Register GitHub operations as MCP tools.
5. Receive tool requests from the MCP client.
6. Execute asynchronous HTTP requests using HTTPX.
7. Retrieve JSON responses from the GitHub REST API.
8. Process the API responses and return structured results to the MCP client.

## 3. Use Cases

The GitHub MCP server allows AI applications to access GitHub information through a standardized tool interface.

Practical use cases include:

- **Repository Exploration:** Ask an AI assistant to list your public repositories.
- **Repository Analysis:** Retrieve repository statistics, programming languages, stars, and forks.
- **Issue Tracking:** Identify open or closed issues in a repository.
- **Pull Request Monitoring:** Retrieve pull requests and their current states.
- **Developer Productivity:** Access GitHub information through natural-language interactions with an MCP-compatible client.
```
```
## 4. Project Structure
Github_MCP/
│
├── github_mcp.py          # Main MCP server implementation
├── pyproject.toml         # Project configuration
├── uv.lock                # Locked dependency versions
├── .gitignore             # Git ignored files
├── .env.example           # Environment variable template
├── readme.md              # Project documentation

```
```
## 5. Environment Configuration

Create a `.env` file in the project root directory.

GITHUB_USERNAME=your_github_username
GITHUB_API=https://api.github.com
GEMINI_API_KEY=
```

Note: The current implementation accesses public repository endpoints without an authentication token. Private repository access and authenticated requests are not implemented. The Gemini API key is loaded but not currently used.
```
## 6. Installation and Execution

### Prerequisites

- Python 3.11+
- GitHub account
- uv package manager
- Node.js and npm

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```
```
### Step 2: Navigate to the Project

```bash
cd Github_MCP
```
```
### Step 3: Create a Virtual Environment

```bash
uv venv
```
```
### Step 4: Install Dependencies

```bash
uv sync
```
```
### Step 5: Configure Environment Variables

Create a `.env` file in the project root and configure the required GitHub username and API URL.

### Step 6: Run MCP Inspector

Execute the following command to launch MCP Inspector and connect your GitHub MCP server:

```powershell
npx -y @modelcontextprotocol/inspector@0.16.2 "<PYTHON_EXECUTABLE_PATH>" "<PROJECT_PATH>\github_mcp.py"
```
```
Replace the placeholders:

- `<PYTHON_EXECUTABLE_PATH>`: Path to `.venv\Scripts\python.exe`.
- `<PROJECT_PATH>`: Absolute path to your GitHub_MCP project directory.

The MCP Inspector UI will open in your browser.

### Step 7: Test MCP Tools

1. Connect to the GitHub MCP server.
2. Navigate to the Tools section.
3. Select a tool and provide the required arguments.
4. Click Run Tool to execute.
5. Inspect the returned response.

## 7. Expected Output

The MCP server exposes four tools:

1. `list_my_public_repositories`
2. `get_repo_info`
3. `list_issues`
4. `list_pull_requests`

### Example Output: Repository Information

```json
{
    "name": "username/repository",
    "description": "Example GitHub project",
    "stars": 10,
    "forks": 2,
    "language": "Python",
    "open_issues": 3,
    "url": "https://github.com/username/repository"
}
```
```
*Example response structure for get_repo_info. Actual values depend on the selected repository.*

## 8. Application Screenshot

**Screenshot Description:**

The screenshot demonstrates the GitHub MCP server connected through MCP Inspector, displaying the registered tools and an example tool execution with a structured response from the GitHub API.
```
<img width="947" height="402" alt="Screenshot 2026-11-21 134643" src="https://github.com/user-attachments/assets/e58b821e-30d8-4a7e-bf4a-597f1b968d60" />


<img width="928" height="390" alt="Screenshot 2026-11-21 134616" src="https://github.com/user-attachments/assets/6ed9638a-0686-46f0-9a18-c49fc41ad900" />
```
## Conclusion

This project demonstrates how to integrate GitHub REST API functionality with the Model Context Protocol (MCP).

By exposing GitHub operations as MCP tools, AI applications can interact with repository information, issues, and pull requests through a standardized interface.
```

