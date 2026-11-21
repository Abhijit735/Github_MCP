import os
from pathlib import Path
from dotenv import load_dotenv
import httpx
from mcp.server.fastmcp import FastMCP

#initialise MCP server 
mcp = FastMCP("GitHub MCP Server")

#load the API keys
load_dotenv()
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_API = os.getenv("GITHUB_API")


def get_headers():
    return {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

#Define the tools
@mcp.tool()
async def list_my_public_repositories() -> list:
    """
    List public repositories owned by the configured GitHub user.
    """

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            f"{GITHUB_API}/users/{GITHUB_USERNAME}/repos",
            params={
                "type": "owner",
                "sort": "updated",
                "per_page": 100
            },
            headers=get_headers()
        )

        response.raise_for_status()
        repositories = response.json()

    return [
        {
            "name": repo["name"],
            "full_name": repo["full_name"],
            "description": repo["description"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "language": repo["language"],
            "url": repo["html_url"]
        }
        for repo in repositories
        if not repo["private"]
    ]


@mcp.tool()
async def get_repo_info(owner: str, repo: str) -> dict:
    """
    Get details of a public GitHub repository.
    """

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            f"{GITHUB_API}/repos/{owner}/{repo}",
            headers=get_headers()
        )

        response.raise_for_status()
        data = response.json()

    if data["private"]:
        raise ValueError("Private repositories are not supported.")

    return {
        "name": data["full_name"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data["language"],
        "open_issues": data["open_issues_count"],
        "url": data["html_url"]
    }


@mcp.tool()
async def list_issues(
    owner: str,
    repo: str,
    state: str = "open"
) -> list:
    """
    List issues from a public GitHub repository.
    State can be open, closed, or all.
    """

    if state not in ["open", "closed", "all"]:
        raise ValueError("State must be open, closed, or all.")

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            f"{GITHUB_API}/repos/{owner}/{repo}/issues",
            params={
                "state": state,
                "per_page": 20
            },
            headers=get_headers()
        )

        response.raise_for_status()
        data = response.json()

    # GitHub issues endpoint also returns pull requests.
    return [
        {
            "number": item["number"],
            "title": item["title"],
            "state": item["state"],
            "url": item["html_url"]
        }
        for item in data
        if "pull_request" not in item
    ]


@mcp.tool()
async def list_pull_requests(
    owner: str,
    repo: str,
    state: str = "open"
) -> list:
    """
    List pull requests from a public GitHub repository.
    """

    if state not in ["open", "closed", "all"]:
        raise ValueError("State must be open, closed, or all.")

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(
            f"{GITHUB_API}/repos/{owner}/{repo}/pulls",
            params={
                "state": state,
                "per_page": 20
            },
            headers=get_headers()
        )

        response.raise_for_status()
        data = response.json()

    return [
        {
            "number": item["number"],
            "title": item["title"],
            "state": item["state"],
            "url": item["html_url"]
        }
        for item in data
    ]


if __name__ == "__main__":
    mcp.run(transport="stdio")
