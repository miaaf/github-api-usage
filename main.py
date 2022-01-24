#github.com/miaaf

from asyncio.windows_events import NULL
from venv import create
import pprint
from github import Github

p = pprint.PrettyPrinter()
g = Github("") #your access token key here

# https://github.com/settings/tokens you must give all permissions.



#by github.com/miaaf


def get_repos(user): #Gets all of the user's repositories and shows us.
    data = g.get_user(user)

    for repo in data.get_repos():
        p.pprint(repo)

def get_current_user(): #Gets current github account.
    user = g.get_user()
    print(user.login)

def get_count_of_stars(repo): #Gets all the stars of the given repository.
    data = g.get_repo(repo)
    print(data.stargazers_count)

def get_topics(repo): #Gets all the topics of the given repository.
    data = g.get_repo(repo)

    if not data.get_topics():
        print("This repository has no topic.")
    else:
        p.pprint(data.get_topics())

def get_contents(repo): #Get all of the contents of the root directory of the repository
    data = g.get_repo(repo)

    contents = data.get_contents("")
    for content_file in contents:
        p.pprint(content_file)

def create_file(repo): #Create a new file in the repository
    data = g.get_repo(repo)
    data.create_file("test.txt", "your commit", "your text") #file_name, commits, text
    print("File created!")

def update_file(repo): #Update a file in the repository
    data = g.get_repo(repo)

    contents = data.get_contents("test.txt")
    data.update_file(contents.path, "your commit", "your text", contents.sha) #commits, text
    print("File updated!")

def delete_file(repo): #Delete a file in the repository
    data = g.get_repo(repo)

    contents = data.get_contents("test.txt")
    data.delete_file(contents.path, "your commit", contents.sha) #commits
    print("File deleted!")

def search_repos_by_language(language, count): #Searches as many repositories as the given number and language.
    data = g.search_repositories(query='language:' + language)

    number = 1
    for repo in data:
        p.pprint(repo)
        if number != count:
            number = number + 1
        else:
            break

def close_all_issues(repo): #Closes all issues.
    data = g.get_repo(repo)

    open_issues = data.get_issues(state="open")
    
    for issue in open_issues:
        p.pprint(issue)
        issue.edit(state="closed")

    print("All issues has been closed.")


def count_all_stars(user): #Gets all stars of user.
    data = g.get_user(user)
    x = 0
    for repo in data.get_repos():
        x += repo.stargazers_count
    print(x)


#get_repos("farajyeet")
#get_count_of_stars("username/project")
#get_topics("farajyeet/webserver")
#search_repos_by_language("cpp", 10)
#create_file("username/project")
#update_file("username/project")
#delete_file("username/project")
#get_contents("farajyeet/webserver")
#get_current_user()
#close_all_issues("username/project")
#count_all_stars("farajyeet")