# LAB 27: Django Models

## Problem Domain:

build out a project with one model and wire up that model using Django Views.

### Feature Tasks and Requirements

- create `blog_project` project
- create `blog` app
- migrate data
- create `Post` model

    - add `title` as a CharField with maximum length of 64 characters.
    - add `author` ForeignKey related to Django's built in user model with CASCADE delete option.
    - add `body` TextField
- add model to admin
- modify `Post` model have user friendly display in admin
- create migrations and migrate data
- create a super user
- Add a few posts via Admin panel
- Add`templates` folder in root of project
  - register `templates` folder in project settings
- create `HomePageView`
  - extend `ListView`
  - give a template of `home.html`
  - associate `Post` model
- create `home.html` template
  - use `Django Templating Language` to display each post's title
- create `base.html` ancestor template
  - add main html document
  - use `Django Templating Language` to allow child templates to insert content
- update url patterns for app and project
- view home page and confirm posts showing properly
- add detail view
  - link `post_detail.html` template
  - associate `Post` model
- create `post_detail.html` template
  - template should extend base
  - content should display post title and body
- update app urlpatterns to handle detail view
  - account for primary key in url
- add link in home page template to related post detail page

## Implementation Notes

- The instructions are becoming more conceptual. 
- All the concepts listed relate to key Django steps covered in the demo.
- If there is confusion about what, exactly, is required then ask the client (aka the instructors.)
- **TLDR** - make your lab project like the demo project.

### User Acceptance Tests

- Test `HomePageViewTest`
  - verify status code
  - verify correct template use
  - use url *name* instead of hard coded path

### time:

- starting time: 1:30 pm
- Finish time: 3:30 pm

## Links:

PR Link :[lab27](https://github.com/baselatalla/django-models/pull/1)
