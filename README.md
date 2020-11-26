# Blog Cookiecutter
This is a cookiecutter template to quickly generate a Jekyll blog
with an Energize Andover theme.

The theme is based on Cayman. It has the following modifications:
- Changed font from Open Sans to Roboto
- Changed `index.md` to display all blog posts

The [post_gen_project.py] script will set up the project similarly to `jekyll new`,
running `bundle install`.
It also sets up the project under Git and creates the first commit for you.

## First-time Setup
### Pre-requisites:
- `cookiecutter` (install using `pip`)
- `jekyll` (view [installation](https://jekyllrb.com/docs/installation/))
- `git` (install using your package manager)
- A Github account

### 1. Create the project from the template
Run `cookiecutter gh:Energize-Andover/blog-cookiecutter`.

### 2. Create the repository on Github
Go to https://github.com/new to create your repository.
Name it `github_username`.github.io,
replacing `github_username` with your own username.

### 3. Push your project files to Github
Follow the instructions under
"...or push an existing repository from the command line".
 