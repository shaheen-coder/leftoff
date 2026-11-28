'''
                                agent_fn.py
                    Needle Agent Tool calling functions
                            
    
'''

from pathlib import Path
import json
from functools import lru_cache
import needle


from leftoff.needle_agent.utils import create_leftoff_dir

def json_parser(json_path : Path  ) -> dict :

    return json.load(open(json_path))

@lru_cache(maxsize=2)
def find_project(project_name: str):
    """Find a project by name, ignoring case."""
    data = json_parser(create_leftoff_dir())
    for project in data["projects"]:
        if project.get("name", "").lower() == project_name.lower():
            return project
    return None

def projects_count() -> int:
    """ Count for all the projects """

    data = json_parser(create_leftoff_dir())

    return len(data)
    
# -----------------------------
# Tools
# -----------------------------

@needle.tool
def get_project_info(project_name: str) -> str:
    """Get the description and basic information of a project. 
    for the questions like what is the project project_name info ?
    """

    project = find_project(project_name)

    if project:
        return (
            f"Project: {project['name']}\n"
            f"Version: {project['version']}\n"
            f"Description: {project['description']}\n"
            f"Issues: {project['issue_count']}\n"
            f"Features: {project['feature_count']}"
        )

    return f"Project `{project_name}` was not found."


@needle.tool
def get_project_count() -> int:
    """Get the total number of projects."""

    return projects_count()


@needle.tool
def get_project_version(project_name: str) -> str:
    """Get the version of a specific project."""

    project = find_project(project_name)

    if project:
        return f"{project['name']} version: {project['version']}"

    return f"Project `{project_name}` was not found."


@needle.tool
def get_project_issue_count(project_name: str) -> str:
    """Get the number of issues in a specific project."""

    project = find_project(project_name)

    if project:
        return (
            f"Project issue count for "
            f"{project['name']}: {project['issue_count']}"
        )

    return f"Project `{project_name}` was not found."


@needle.tool
def get_project_feature_count(project_name: str) -> str:
    """Get the number of features in a specific project."""

    project = find_project(project_name)

    if project:
        return (
            f"Project feature count for "
            f"{project['name']}: {project['feature_count']}"
        )

    return f"Project `{project_name}` was not found."


@needle.tool
def list_projects() -> str:
    """List all available project names."""
    data = json_parser(create_leftoff_dir())
    projects = [
        project["name"]
        for project in data["projects"]
    ]

    return "\n".join(projects)


@needle.tool
def get_project_path(project_name: str) -> str:
    """Get the filesystem path of a specific project."""

    project = find_project(project_name)

    if project:
        return f"{project['name']} path: {project['path']}"

    return f"Project `{project_name}` was not found."


@needle.tool
def get_python_version() -> str:
    """Get the Python version used by the project-management environment."""

    return "v3.12"


def get_all_tools() -> list :
    return [
        get_project_count,
        get_project_feature_count,
        get_project_info,
        get_project_issue_count,
        get_project_path,
        get_project_version,
        get_python_version,
        list_projects,
    ]
