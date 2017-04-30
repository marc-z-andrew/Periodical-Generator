#    Author: Marc Andrew

# Import the function for opening a web document given its URL.
from urllib import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression.
from re import findall

# Import a function for opening an HTML document in your operating
# system's default web browser.
from webbrowser import open as webopen

# Import a function for getting the current working directory/folder.
from os import getcwd

# Import a function for 'normalising' file paths.
from os.path import normpath

# Import the standard Tkinter functions.
from Tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date/time function.
from datetime import datetime

# Name of html file to be created
file_name = 'simply_news.html'

# Create a function for a business article to be scraped and laid out in html
def business():
    url = 'http://feeds.bbci.co.uk/news/business/rss.xml'  # Business RSS feed
    # Open the web page and save it as a string
    web_page = urlopen(url)
    html_code = web_page.read()
    web_page.close()
    # Scrape article information using regular expressions
    business_article_category = 'Business'
    business_article_title = findall('(?<=<title><!\[CDATA\[)(.*)(?=]])', html_code)
    business_article_image = findall('(?<=url=")(.*)(?=")', html_code)
    business_article_summary = findall('(?<=<description><!\[CDATA\[)(.*)(?=]])', html_code)
    business_article_time = findall('(?<=<pubDate>)(.*)(?=<)', html_code)
    # Create a global variable and record RSS url
    global business_url
    business_url = url
    # Create a global variable and record the time when the article is generated
    global business_time
    business_time = datetime.now()
    # Write the html for the article to the html file substituting data scraped from RSS site
    html_file.write(
        """<div style="width:60%; margin: auto; border-top: thick double #000000">
            <table style="border-collapse: collapse;">
                <tr>
                    <!--Show article category-->
                    <h3 style="text-align: left">""" + business_article_category + """</h3>
                </tr>
                <tr>
                    <!--Show article title-->
                   <h2 style="text-align: left">""" + business_article_title[1] + """</h2>
                </tr>
                <tr>
                    <!--Show summary of the article-->
                    <p style="text-align: left; font-size: 20px">
                        """+ business_article_summary[1] +"""
                    </p>
                </tr>
                <tr>
                    <!--Show article image-->
                    <img width="20%" style="margin: 0px auto;display:block; border: 3px solid #000000;" src=" """
                    + business_article_image[0] + """">
                </tr>
                <tr>
                    <!--Link the RSS feed data was scraped from and print the date the article was published-->
                    <p style="text-align: left">
                        Source:""" + business_url + """ <br>
                        Published:""" + business_article_time[0] + """
                    </p>
                </tr>
            </table>
        </div>"""
    )

# Create a function for a politics article to be scraped and laid out in html
def politics():
    url = 'http://feeds.bbci.co.uk/news/politics/rss.xml' # Politics RSS feed
    # Open the web page and save it as a string
    web_page = urlopen(url)
    html_code = web_page.read()
    web_page.close()
    # Scrape article information using regular expressions
    politics_article_category = 'Politics'
    politics_article_title = findall('(?<=<title><!\[CDATA\[)(.*)(?=]])', html_code)
    politics_article_image = findall('(?<=url=")(.*)(?=")', html_code)
    politics_article_summary = findall('(?<=<description><!\[CDATA\[)(.*)(?=]])', html_code)
    politics_article_time = findall('(?<=<pubDate>)(.*)(?=<)', html_code)
    # Create a global variable and record RSS url
    global politics_url
    politics_url = url
    # Create a global variable and record the time when the article is generated
    global politics_time
    politics_time = datetime.now()
    # Write the html for the article to the html file substituting data scraped from RSS site)
    html_file.write("""
        <div style="width:60%; margin: auto; border-top: thick double #000000">
            <table style="border-collapse: collapse;">
                <tr>
                    <!--Show the article category-->
                    <h3 style="text-align: left">""" + politics_article_category + """</h3>
                </tr>
                <tr>
                    <!--Show the title of the article-->
                    <h2 style="text-align: left">""" + politics_article_title[1] + """</h2>
                </tr>
                <tr>
                    <!--Show the summary of the article-->
                    <p style="text-align: left; font-size: 20px">
                    """ + politics_article_summary[1] + """
                    </p>
                </tr>
                <tr>
                    <!--Show the article image-->
                    <img width="20%" style="margin: 0px auto;display:block; border: 3px solid #000000;" src=" """
                    + politics_article_image[0] + """">
                </tr>
                <tr>
                    <!--Show the RSS feed the article was scraped from and show the date published-->
                    <p style="text-align: left">
                        Source:""" + politics_url + """ <br>
                        Published:""" + politics_article_time[0] + """
                    </p>
                </tr>
            </table>
        </div>"""
                    )

# Create a function for a technology article to be scraped and laid out in html
def technology():
    url = 'http://feeds.bbci.co.uk/news/technology/rss.xml' # Technology RSS feed
    # Open web page and save it as a string
    web_page = urlopen(url)
    html_code = web_page.read()
    web_page.close()
    # Scrape the article's data from the RSS feed using regular expressions
    technology_article_category = 'Technology'
    technology_article_title = findall('(?<=<title><!\[CDATA\[)(.*)(?=]])', html_code)
    technology_article_image = findall('(?<=url=")(.*)(?=")', html_code)
    technology_article_summary = findall('(?<=<description><!\[CDATA\[)(.*)(?=]])', html_code)
    technology_article_time = findall('(?<=<pubDate>)(.*)(?=<)', html_code)
    # Create a global variable and record RSS url
    global technology_url
    technology_url = url
    # Create a global variable and record the time when the article is generated
    global technology_time
    technology_time = datetime.now()
    # Write the html for the article to the html file substituting data scraped from RSS site
    html_file.write("""
        <div style="width:60%; margin: auto; border-top: thick double #000000">
            <table style="border-collapse: collapse;">
                <tr>
                    <!--Show the article category-->
                    <h3 style="text-align: left">""" + technology_article_category + """</h3>
                </tr>
                <tr>
                    <!--Show the article title-->
                    <h2 style="text-align: left">""" + technology_article_title[1] + """</h2>
                </tr>
                <tr>
                    <!--Show the article summary-->
                    <p style="text-align: left; font-size: 20px">
                    """ + technology_article_summary[1] + """
                    </p>
                </tr>
                <tr>
                    <!--Show the article image-->
                    <img width="20%" style="margin: 0px auto;display:block; border: 3px solid #000000;" src=" """
                    + technology_article_image[0] + """">
                </tr>
                <tr>
                    <!--Show the RSS feed source and the date published-->
                    <p style="text-align: left">
                        Source:""" + technology_url + """ <br>
                        Published:""" + technology_article_time[0] + """
                    </p>
                </tr>
            </table>
        </div>"""
    )

# Create a function for a science and environment article to be scraped and laid out in html
def science_and_environment():
    url = 'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml' # Science and environment RSS feed
    # Open the web page and save it as a string
    web_page = urlopen(url)
    html_code = web_page.read()
    web_page.close()
    # Scrape the article data using regular expressions
    science_article_category = 'Science and Environment'
    science_article_title = findall('(?<=<title><!\[CDATA\[)(.*)(?=]])', html_code)
    science_article_image = findall('(?<=url=")(.*)(?=")', html_code)
    science_article_summary = findall('(?<=<description><!\[CDATA\[)(.*)(?=]])', html_code)
    science_article_time = findall('(?<=<pubDate>)(.*)(?=<)', html_code)
    # Create a global variable and record RSS url
    global science_and_environment_url
    science_and_environment_url = url
    # Create a global variable and record the time when the article is generated
    global science_and_environment_time
    science_and_environment_time = datetime.now()
    # Write the html to the html file substituting the article data
    html_file.write("""
        <div style="width:60%; margin: auto; border-top: thick double #000000">
            <table style="border-collapse: collapse;">
                <tr>
                    <!--Show the article category-->
                    <h3 style="text-align: left">""" + science_article_category + """</h3>
                </tr>
                <tr>
                    <!--Show the article title-->
                    <h2 style="text-align: left">""" + science_article_title[1] + """</h2>
                </tr>
                <tr>
                    <!--Show the article summary-->
                    <p style="text-align: left; font-size: 20px">
                    """ + science_article_summary[1] + """
                    </p>
                </tr>
                <tr>
                    <!--Show the article image-->
                    <img width="20%" style="margin: 0px auto;display:block; border: 3px solid #000000;" src=" """
                    + science_article_image[0] + """">
                </tr>
                <tr>
                    <!--Show the RSS feed source and show the date published-->
                    <p style="text-align: left">
                        Source:""" + science_and_environment_url + """ <br>
                        Published:""" + science_article_time[0] + """
                    </p>
                </tr>
            </table>
        </div> """
    )

# Create a function that prints the selected articles
def print_selected_articles():
    # Create html file and open it
    file_name = 'simply_news.html'
    global html_file
    html_file = open(file_name, 'w')
    # Write the html for the masterhead to the html file
    html_file.write('''
        <html>
        <head>
            <!--Periodical title-->
            <title>Simply News</title>
            <style>
            </style>
            <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        </head>
        <body>
            <!--Periodical title-->
            <h1 style="font-size: 60; text-align: center">Simply News</h1>
            <!--Periodical logo-->
            <img style="margin: 0px auto;display:block" src="http://www.freeiconspng.com/uploads/news-icon-21.png" width="200" height="auto">
            <!--Person responsible-->
            <h2 style="text-align: center">Editor-in-Chief: Marc Andrew</h2>
                ''')
    # Clear progress window
    progress_window.delete(0, END)
    # Use if loops to check if the checkbutton is selected for a particular article
    if business_category.get() == 1:
        # Print the status showing the article being generated
        progress_window.insert(END, "Generating business article ...")
        the_window.update()
        # Call the function that generates the html for the article
        business()
        # Print the status showing that the article has finished generating
        progress_window.insert(END, "Done!")
        the_window.update()

    # Use if loops to check if the checkbutton is selected for a particular article
    if politics_category.get() == 1:
        # Print the status showing the article being generated
        progress_window.insert(END, "Generating politics article ...")
        the_window.update()
        # Call the function that generates the html for the article
        politics()
        # Print the status showing that the article has finished generating
        progress_window.insert(END, "Done!")
        the_window.update()

    if technology_category.get() == 1:
        # Print the status showing the article being generated
        progress_window.insert(END, "Generating technology article ...")
        the_window.update()
        # Call the function that generates the html for the article
        technology()
        # Print the status showing that the article has finished generating
        progress_window.insert(END, "Done!")
        the_window.update()

    if science_and_environment_category.get() == 1:
        # Print the status showing the article being generated
        progress_window.insert(END, "Generating science and environment article ...")
        the_window.update()
        # Call the function that generates the html for the article
        science_and_environment()
        # Print the status showing that the article has finished generating
        progress_window.insert(END, "Done!")
        the_window.update()
    # Print the status that all articles have finished generating
    progress_window.insert(END, "Finished generating news!")
    the_window.update()
    # Write the closing html tags
    html_file.write('''
        </body>
        </html>
        ''')
    # Close the html file so it can be opened in a browser
    html_file.close()
    progress_window.bindtags((progress_window, the_window, "all"))

# Function that closes the tkinter window when the "Close" button is clicked
def close_window():
    the_window.destroy()

# Function that opens the html file when the button is clicked
def open_news():
    path = "file:///" + getcwd() + '/' + 'simply_news.html'
    normalised_path = normpath(path)
    webopen(normalised_path)

# Function that logs activity
def log_activity():
    # Open connection to database
    connection = connect(database='internet_activity.db')
    # Crete a cursor object
    activity_db = connection.cursor()
    # Delete previous entries in SQL table
    activity_db.execute("DELETE FROM Recent_Downloads")
    # SQL statement to insert values into table
    sql_code = "INSERT INTO Recent_Downloads VALUES ('Date', 'URL')"
    # Check to see if a business article has been generated
    if business_category.get() == 1:
        # Replace strings in sql statement with time and url variables
        sql_statement = sql_code.replace('Date', str(business_time)).replace('URL', str(business_url))
        # Execute the sql statement
        activity_db.execute(sql_statement)
    # Check to see if a technology article has been generated
    if technology_category.get() == 1:
        # Replace strings in sql statement with time and url variables
        sql_statement = sql_code.replace('Date', str(technology_time)).replace('URL', str(technology_url))
        # Execute the sql statement
        activity_db.execute(sql_statement)
    # Check to see if a politics article has been generated
    if politics_category.get() == 1:
        # Replace strings in sql statement with time and url variables
        sql_statement = sql_code.replace('Date', str(politics_time)).replace('URL', str(politics_url))
        # Execute the sql statement
        activity_db.execute(sql_statement)
    # Check to see if a science and environment article has been generated
    if science_and_environment_category.get() == 1:
        # Replace strings in sql statement with time and url variables
        sql_statement = sql_code.replace('Date', str(science_and_environment_time))\
            .replace('URL', str(science_and_environment_url))
        # Execute the sql statement
        activity_db.execute(sql_statement)
    # Save the changes and close the connection
    connection.commit()
    activity_db.close()
    connection.close()
    progress_window.insert(END, "Activity has been logged.")

# Create GUI
# Create a window
the_window = Tk()

# Define the window title
the_window.title('Simply News')

# Create the main frame
frame = Frame(the_window)
frame.pack()

# Create a label telling the user what to do for the first step
var1 = StringVar()
step1 = Label(frame, textvariable=var1).grid(row=0, columnspan=2, sticky=W)
var1.set("1. Select the articles you wish to print.")

# Create the checkbutton variables and the checkbuttons
business_category = IntVar()
politics_category = IntVar()
technology_category = IntVar()
science_and_environment_category = IntVar()

business_checkbutton = Checkbutton(frame, text="Business", variable=business_category, onvalue=1, offvalue=0)
business_checkbutton.grid(row=1, column=0, sticky=W)

politics_checkbutton = Checkbutton(frame, text="Politics", variable=politics_category, onvalue=1, offvalue=0)
politics_checkbutton.grid(row=1, column=1, sticky=W)

technology_checkbutton = Checkbutton(frame, text="Technology", variable=technology_category, onvalue=1, offvalue=0)
technology_checkbutton.grid(row=2, column=0, sticky=W)

science_and_environment_checkbutton = Checkbutton(frame, text="Science and Environment",
                                                  variable=science_and_environment_category, onvalue=1, offvalue=0)

science_and_environment_checkbutton.grid(row=2, column=1, sticky=W)

# Create the print button
Button(frame, text="Print", command=print_selected_articles).grid(row=3, columnspan=2)

# Create a label telling the user what to do for the second step
var2 = StringVar()
step2 = Label(frame, textvariable=var2).grid(row=4, columnspan=2, sticky=W)
var2.set("2. See progress below.")

# Create the listbox where the status updates will be printed
progress_window = Listbox(frame, selectbackground='white', width=40)
progress_window.grid(row=5, columnspan=2)

# Create a label telling the user what to do for the third step
var3 = StringVar()
step3 = Label(frame, textvariable=var3).grid(row=6, columnspan=2, sticky=W)
var3.set("3. Open the periodical in your browser or close the window.")

# Create the button to close the window
Button(frame, text="Close", command=close_window).grid(row=7, column=1)

# Create the button to open the html file
Button(frame, text="Open Simply News", command=open_news).grid(row=7, column=0, sticky=E)

# Create a label telling the user what to do for the third step
var4 = StringVar()
step4 = Label(frame, textvariable=var4).grid(row=8, columnspan=2, sticky=W)
var4.set("4. Log the articles downloaded")

# Create the button to log the articles generated
Button(frame, text="Log", command=log_activity).grid(row=9, columnspan=2)

# Start the event loop to react to user inputs
the_window.mainloop()
