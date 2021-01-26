# Git Helper

Git Helper is a python shell that provides some extra capabilities to your Github local repo.

## Installation

Currently, I don't have an executable but you can clone my repo.

```bash
git clone https://github.com/saurav0705/Git-Helper.git
```

set up the alias to trigger the script so that it can be triggered from anywhere. 

```
alias git-helper="python3 <path-to-repo>/driver_file.py"
```

## Methods/Commands

### clean_repo
Usually, when we develop a new feature our local repo gets cluttered with a lot of feature branches that then we have to delete but that's a lot of pain usually what I did is make a command which deletes all the feature branches because I don't want to delete branches that I normally use for me that were **master** and **production**.

So what this method does is if you run this in your local GitHub repo it will find all the branches that it has and will delete them for you and you can change the branches that you don't want to delete by going into configs and editing it.

**Note:** It will also not delete the branch that you are currently on.

```
(Git Helper) $ clean_repo
```

### pull_branch
pulling a branch is also another trivial thing that this repo does suppose you are working on a branch and suddenly you have to switch to a new feature branch but before switching to this new feature branch you have to take the pull from the base branch so it this command makes it easy just run pull_branch and it will stash your changes and will ask you for the branch you want to update and will pull latest of the branch and will revert to your feature branch and will pop the stashed changes so that you have the same working environment.

**Note:** It will only pull its latest if the branch already exists in your local otherwise it will not work.

```
(Git Helper) $ pull_branch
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.