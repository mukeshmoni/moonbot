#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sys import version_info
from .db import db
import git

__all__ = [
    "modules_help",
    "requirements_list",
    "python_version",
    "prefix",
    "gitrepo",
    "userbot_version",
]


modules_help = {}
requirements_list = []

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

prefix = db.get("core.main", "prefix", ".")

try:
    gitrepo = git.Repo(".")
except git.exc.InvalidGitRepositoryError:
    repo = git.Repo.init()
    origin = repo.create_remote(
        "origin", "https://github.com/The-MoonTg-project/Moon-Userbot"
    )
    origin.fetch()
    repo.create_head("main", origin.refs.main)
    repo.heads.main.set_tracking_branch(origin.refs.main)
    repo.heads.main.checkout(True)
    gitrepo = git.Repo(".")

if len(gitrepo.tags) > 0:
    commits_since_tag = list(gitrepo.iter_commits(f"{gitrepo.tags[-1].name}..HEAD"))
else:
    commits_since_tag = []
userbot_version = f"2.5.{len(commits_since_tag)}"
