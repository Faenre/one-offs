## json_pretty.py

This converts a blob of ugly json data into something organized and human readable.

Consider the json dump for the [Rails repo](https://api.github.com/repos/rails/rails):

```json
{ "id": 8514, "node_id": "MDEwOlJlcG9zaXRvcnk4NTE0", "name": "rails", "full_name": "rails/rails", "private": false, "owner": { "login": "rails", "id": 4223, "node_id": "MDEyOk9yZ2FuaXphdGlvbjQyMjM=", "avatar_url": "https://avatars.githubusercontent.com/u/4223?v=4", "gravatar_id": "", "url": "https://api.github.com/users/rails", "html_url": "https://github.com/rails", ...
  ```

This very simple script sorts the content alphabetically and adds whitespacing, via JSON.stringify.

```json
{
  "archive_url": "https://api.github.com/repos/rails/rails/{archive_format}{/ref}",
  "archived": false,
  "assignees_url": "https://api.github.com/repos/rails/rails/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/rails/rails/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/rails/rails/branches{/branch}",
  "clone_url": "https://github.com/rails/rails.git",
  "collaborators_url": "https://api.github.com/repos/rails/rails/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/rails/rails/comments{/number}",
  "commits_url": "https://api.github.com/repos/rails/rails/commits{/sha}",
  "compare_url": "https://api.github.com/repos/rails/rails/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/rails/rails/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/rails/rails/contributors",
  "created_at": "2008-04-11T02:19:47Z",
  "default_branch": "main",
  "deployments_url": "https://api.github.com/repos/rails/rails/deployments",
  "description": "Ruby on Rails",
  "disabled": false,
  ...
}
```

Usage:

- From command line, `python /path/to/json_pretty.py some_file.json`

- Or, if you `chmod +x json_pretty.py` the shell will run it in python

- Use it in SublimeText3 as a custom build system, and you can just "run" your JSON dump  for it to quickly prettify.

SublimeText3 build-file (update your path, e.g. to `/usr/local/bin/` or wherever else):

```json
{
  "cmd": ["python", "/Users/nicole/Code/One-Offs/json_pretty.py", "$file"],
  "file_regex": "^(...*?):([0-9]*):?([0-9]*)",
  "selector": "source.json",
  "file_patterns": ["*.json"]
}
```
