from flask import Flask
from flask import request
from data import colors
import json
from utilities import *

app = Flask("story_builder")


@app.route("/new-user", methods=['GET', 'POST'])
def new_user():

    html_page = get_html("pages/new-user")

    if request.method == "POST":
        name = request.form['name']

        color = request.form['user']
        user = {"name": name, "color": color}
        write_data_in_file("data/users_db.txt", json.dumps(user))

    # as the user should  choose a color code for his profile ,
    # i have used a dynamic way to implement colors from the imported colors dictionary
    colors_arr = ""
    for name, value in colors.items():
        colors_arr += radio_button(value, value, name)
    return html_page.replace("$$chooseColors$$", colors_arr)


@app.route("/")
def login():
    html_page = get_html("index")

    users = get_data_from_file("data/users_db.txt")

    user_list = ""
    for user in users:
        # converting each element of the array from string to json so i can access it later as dictionary
        user_dic = json.loads(user)

        button = radio_button(
            user_dic["name"], user_dic["color"], user_dic["name"])
        user_list += button

    if users == ['']:
        user_list = "No users to show"
    return html_page.replace("$$users$$", user_list)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    html_page = get_html("pages/dashboard")
    story1 = get_data_from_file("data/stories/stories_db.txt")[0]
    story = request.args.get("story") or story1
    html_page = html_page.replace('"Story headline"', str(story).upper())

    comments = get_data_from_file("data/stories/{}.txt".format(story))
    comment_list = reading_comments(comments)
# reeding story list items  from  stories_db

    stories_data = get_data_from_file("data/stories/stories_db.txt")
    story_list = reading_stories(stories_data)

    html_page = html_page.replace("$$SelectOption$$", story_list)

    if request.method == "GET":

        # the list items in the html file "dashboard" with  id="stories" sends a value immediately once clicked , which i made it "default" to avoid refreshing the page in wrong way
        if (request.args.get("story") != "default"):
            story = request.args.get("story")
            if request.args.get("story") == None:
                story = story1
            comments = get_data_from_file("data/stories/{}.txt".format(story))
# printing comments to the screen
            comment_list = reading_comments(comments)
            html_page = html_page.replace(
                '"Story headline"', str(story).upper())


# - this section for creating a new story line *Comment* on the current story
    if request.method == "POST":
        name = request.form['comment-user-name']
        color = request.form['comment-user-color']

        comment = request.form['comment']

        new_comment = AddComment(name, color, comment)
        write_data_in_file("data/stories/{}.txt".format(story),
                           json.dumps(new_comment.data()))
# after adding the new comments we reopen and read the file again to update the UI
        comments = get_data_from_file("data/stories/{}.txt".format(story))
        comment_list = reading_comments(comments)

    return html_page.replace("$$comments$$", comment_list)

# adding a new story by creating a new file for the story and add the story from the data base


@app.route("/new-story", methods=['GET', 'POST'])
def new_story():
    html_page = get_html("pages/new-story")
    stories_data = get_data_from_file("data/stories/stories_db.txt")

    if request.method == "POST":
        name = request.form['name'].lower()
        if (name.lower() in stories_data):
            return html_page.replace("<p id='feedBack'></p>", "<p id='feedBack'>Story Already Exist!!</p>")
        else:
            write_data_in_file("data/stories/stories_db.txt", name)
            open('data/stories/{}.txt'.format(name), 'w')

        return html_page.replace("<p id='feedBack'></p>", "<p id='feedBack'>Story '{}' Have been created!</p>".format(name.capitalize()))
    return html_page


@app.route("/how-it-works")
def info():
    html_page = get_html("pages/info")

    return html_page
