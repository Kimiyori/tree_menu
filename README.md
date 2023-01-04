# About

Django tree menu app

# How deploy

Run the following command:

```
git clone https://github.com/Kimiyori/tree_menu.git
cd tree_menu
docker-compose up --build
```
App will be available at http://localhost:8000

# Description solution

The best solution was to use the MPTT library, which allowed the most efficient 
creation of tree-like menu queries through one query, as opposed to
the standard parent/child relationship through foreignkey

The database consists of 2 models - Menu (which stores the menu name)
and Item (where all child menu items are stored)