# Python code to serve a html page with the requested video, if available. Otherwise to download it from the main server.
# IC202-A 1
# 2020
# Andres Stolk 500683339, Yasin Tas 500816623, Süleyman Günay 500806009, Daniël van Apeldoorn 500825388, Mert Gökseli 500819528



# Modules to work with the POST method and to scan the filesystem.
import urllib.parse as urlparse
import sys
import os, fnmatch

# This function looks to see if a certain file 'zoek' exists in path 'path', if it does it returns True.
def find(path, zoek):
    for root, dirs, files in os.walk(path):
        for bestand in files:
            if fnmatch.fnmatch(bestand, zoek):
                return True

# This function is a placeholder for function 'find'. If the name is the same as the one in the function, it returns ...
# ... True. Used for testing until 'find' function works.
def find2(movieName):
    if movieName == "alita.mp4":
        return True

# Create function called application which serves html code to browser according to the input from the previous ...
# ... website using the POST method.
def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)

    # This is the html code that the browser will see.
    html = ''
    html += '<!DOCTYPE html> \n'
    html += '<html> \n'
    html += '<head> \n'
    html += '  <title>SecurityFlix</title> \n'
    html += '  <meta charset="utf-8"> \n'
    html += '  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> \n'
    html += '  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous"> \n'
    html += '  <link rel="stylesheet" href="../css/bootstrap.css" type="text/css"> \n'
    html += '</head> \n'
    html += '<body> \n'



    # This code gets the POST value and saves it in a variable called 'name2'.
    environmentVars = ['REQUEST_METHOD', 'REQUEST_URI', 'QUERY_STRING', 'SCRIPT_NAME', 'HTTP_REFERER']
    method = environ.get('REQUEST_METHOD', '')
    params = {}
    if method == 'GET':
        params = urlparse.parse_qs(environ['QUERY_STRING'])
    elif method == 'POST':
        input = environ['wsgi.input'].read().decode()
        params = urlparse.parse_qs(input)
    name2 = str(params.get('inputName'))

    # The brackets and apostrophes are removed from variable 'name2' and this value is stored in name. Then the code...
    # ... checks if the value corresponds to a name from the list of movies; if it does: the corresponding full name...
    # ... is assigned to another variable for the user to see the correct name on their browser.
    name = str(name2[2:-2])
    fullName = " "
    movies = ['alita', 'john', 'broly', 'godfather', 'howl', 'interstellar', 'tenet', 'bumblebee']
    moviesFullName = ['Alita', 'John Wick 3', 'Dragon Ball Z Broly', 'The Godfather', 'Howl\'s moving Castle', 'Interstellar', 'Tenet', 'Bumblebee']

    for i in range(len(movies)):
       if name == movies[i]:
           name = str(movies[i])
           fullName = str(moviesFullName[i])
           break

    # Regular html code
    html += '  <nav class="navbar navbar-expand-lg navbar-dark bg-primary"> \n'
    html += '    <a class="navbar-brand" href="index.py"> \n'
    html += '      <img src="../image/logo.png" width="30" height="30" alt="" loading="lazy"> \n'
    html += '    </a> \n'
    html += '    <a class="navbar-brand" href="index.py">Navbar</a> \n'
    html += '    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> \n'
    html += '      <span class="navbar-toggler-icon"></span> \n'
    html += '    </button> \n'
    html += '    <div class="collapse navbar-collapse" id="navbarSupportedContent"> \n'
    html += '      <ul class="navbar-nav mr-auto"> \n'
    html += '        <li class="nav-item active"> \n'
    html += '          <a class="nav-link" href="index.py">Home <span class="sr-only">(current)</span></a> \n'
    html += '        </li> \n'
    html += '      </ul> \n'
    html += '    </div> \n'
    html += '  </nav> \n'
    html += '   <h1> \n'


    # The name in the list is only the name of the movie, not with the format. So we add ".mp4" to it so the 'find'...
    # ... function can find it in the filesystem.
    name = name+".mp4"

    # The if(find(path, name)) should return True if the movie is available. Because this function is not finished ...
    # ... yet, we use another function called 'find2'.

    #if find('../video/', name):

    # Function 'find2' searches the filesystem for the requested movie. If it is found the player is added to the ...
    # ... html code so the user can watch the movie. If not, the else part runs. Here the else part only tells the ...
    # ... user that their video (with the full name) is being prepared. If the download code works this goes in the ...
    # ... else part.
    if find2(name):
        insertMovie = "<source src=\"../video/" + name + ".mp4\" type=\"video/mp4\"> \n"
        html += '  <div class="embed-responsive embed-responsive-16by9"> \n'
        html += '    <video height="inherit" width="inherit" controls> \n'
        html += insertMovie
        html += '    </video> \n'
        html += '    </<div> \n'
    else:
        html += '  Your movie ' + fullName + ' is being prepared. Thank you for your patience \n'

    html += '   </h1> \n'
    html += '  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script> \n'
    html += '  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script> \n'
    html += '  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script> \n'
    html += '</body> \n'
    html += '</html> \n'


    # If function is called, return the specified values.
    return [bytes(html, 'utf-8')]

# Call function if condition is met.

if __name__ == '__main__':
    application({}, print)

