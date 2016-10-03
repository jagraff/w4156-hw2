#Homework 2 - Toy Project

*Group Members:*
Jacob Graff
Andrew Feather

Github Repository: [https://github.com/jagraff/w4156-hw2]

**Overview:**

We are one-half of one of the JP Morgan teams, so for this homework, we decided to try to build the bones of our semester project.

We set up a basic Flask application with a set of HTML templates that helped generate a few basic pages. Next, we added a Postgresql database and tied it to the application, so we could create usernames and hashed passwords to secure users’ login information.

As of now, the app takes the user to a register/login page by default. From there, the user can create a username or enter one if they already have one. Then the user is redirected to a page that greets them to let them know they are successfully logged in. To have the correct greeting, we also built in STUFF ABOUT SESSION HERE

**Technologies:**

_Python 2.7_

Python installed without any issue. We setup a virtual environment, so that we could make sure we maintain the same version of various packages across all of our machines even if we need to update the local packages or environments associated with other projects. This allowed us also to generate a list of requirements that we can tap into when setting up machines in the future.

_Flask_

We had both worked with Flask previously, so it did not take us long to set it up. The trickiest part was figuring out which module we should use to link to the database so that we could have a set of persistent information.

Flask quickly generated the pages from our HTML templates and returned information to the user. It played well with the Python logic we were putting together, and we only had a few minor issues tying everything together - mostly regarding syntax.

_HTML Templates

The HTML templates worked well with Flask. We did not try anything too fancy with them, but they passed the variables we wanted to move back and forth without any issue.

_Postgresql

The database was our most challenging project. After toying with running the database from the command line for awhile, we finally opted to use the desktop app available at postgresql.org to launch our database. Once we started it up, we began inserting some information manually from the command line, so that we could test it in the app. This all worked as it should. However, as mentioned earlier, the first tie-ins between Python and Postgresql were our biggest issues.

**Conclusion**

Overall we had very few issues. The biggest challenge will be making sure that the system is consistent and easy to set up on all of our team members' computers. We look forward to building some great software with our platform.
