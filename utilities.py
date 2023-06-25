import json
from datetime import datetime


# general function to get html pages dynamically, takes page name in the arg
def get_html(page_name):
    html_page = open(page_name+".html")
    content = html_page.read()
    html_page.close()
    return content


def reading_stories(stories):
    """this function takes an array as a argument and return html list elements option

    """
    story_list = ""
    if stories == ['']:
        return "Nothing yet to show"

    for story in stories:
        # check if there is stories
        option = ' <option value="{}"  >{}</option>'.format(story, story)
        story_list += option
    return story_list


def get_data_from_file(file_name):
    """this function read a text file and return an array 
    each line of the text file represent element of the array 
    any empty line will be discarded 
    """
    file = open(file_name)
    content = file.read().strip()
    data = content.split("\n")
    file.close()

    return data


def write_data_in_file(file_name, data):
    """this function write data in a text file 
    the data is being separated with a new line on every call
     """
    file = open(file_name, "a")
    file.write("\n")
    file.write(data)


def reading_comments(comments):
    """this function reed an array of dictionaries in jason format and return an HTML  
     looping through an array of dictionaries in json format get there values and return
     a html element for each 
     """
    comment_list = ""

    for comment in comments:
        # check if there is comments
        if comments == ['']:
            return "Nothing yet to show"

        else:
            # converting each element of the array from the string format to an accessible dictionary type format
            comment_dic = json.loads(comment)
            button = user_login_button(
                comment_dic["name"], comment_dic["color"])
            date = '<span class="comment-date">{}</span>'.format(
                comment_dic["date"])
            text = comment_dic["comment"]

            comment_list += "<p class='comment-text' style=' border-top: 1px solid {}'> {} {} \n {}</p>".format(
                comment_dic["color"], button, text, date)

    return comment_list


# return an html radio button
def radio_button(value, color, name):
    button = '<label   class="radio-inline"> <input class="user" type="radio" name="user"  value={}  required> <span  class="btn-color" id={} style="background:{}">{}</span> </label>'.format(
        value, color, color, name)
    return button

# user_login_button returns a customized html button


def user_login_button(name, color):
    button = "<button class=\"btn-login btn-color \" style=\"background:{} \">{}</button>".format(
        color, name)
    return button


class AddComment():
    """this class takes 2 args ,used in html button values 
    return a button with customized values'color,value,content'
    """

    def __init__(self, name, color, text):
        self.name = name
        self.color = color
        self.text = text

    def get_date(self):
        self.date = datetime.now().strftime("%d/%m   %H:%M")

    def data(self):
        self.get_date()
        return {"name": self.name, "color": self.color, "comment": self.text, "date": self.date}
