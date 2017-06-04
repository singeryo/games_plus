# games_plus

#### Brief description
games_plus is a Django project containing a games review web site (games_review) in wich you can ... well ... review games.

## Games review
### Contains
 - Authentication system
 - Comments

### What technologies are used
#### Back-end:
- Python using Django 1.11
- SQLite 3 database

#### Front-end:
- Bootstrap 3
- JQuery 3.2
- Font Awesome 4.7


### Working with games_review
#### Views:
- Index: root page of the web site. Establishes a paginated list of games and displays their links. Search field to filter by name.
- Game: Game description in wich you can post comments if authenticated. Game types are links back to index with type filter parameter.

#### Model:
- Game -> Name, Release date, author, types, slug
- Type -> Name, slug
- Comment -> Body, author, game, date

#### Forms:
- CommentForm: Textarea
