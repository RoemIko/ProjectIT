# Python code to serve the homepage for the website
# IC202-A 1
# 2020
# Andres Stolk 500683339, Yasin Tas 500816623, Süleyman Günay 500806009, Daniël van Apeldoorn 500825388, Mert Gökseli 500819528



# Create function called application which serves html code to browser

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
    html += '  <div class="container"> \n'
    html += '    <div class="row"> \n'


    # The next part is for all the movies with their POST methods respectively.

    # Movie Alita
    html += '      <div class="col-sm"> \n'
    html += '        <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/Alita.png" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="alita" class="btn2">  Watch Alita </button> \n'
    html += '        </form> \n'
    html += '      </div> \n'

    # Movie John Wick
    html += '      <div class="col-sm"> \n'
    html += '      <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/John.jpg" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="john" class="btn2"> Watch John Wick </button> \n'
    html += '        </form> \n '
    html += '      </div> \n'

    # Movie Dragon Ball Z Broly
    html += '      <div class="col-sm"> \n'
    html += '      <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/Broly.jpg" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="broly" class="btn2"> Watch Dragon Ball Z Broly </button> \n'
    html += '        </form> \n '
    html += '      </div> \n'

    # Movie The Godfather
    html += '      <div class="col-sm"> \n'
    html += '      <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/Godfather.jpg" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="godfather" class="btn2"> Watch The Godfather </button> \n'
    html += '        </form> \n '
    html += '      </div> \n'

    html += '    </div> \n'
    html += '    <div class="row"> \n'

    # Movie Howl's Moving Castle
    html += '      <div class="col-sm"> \n'
    html += '    <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/Howl.jpg" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="howl" class="btn2"> Watch Howl\'s Moving Castle </button> \n'
    html += '        </form> \n '
    html += '      </div> \n'

    # Movie Interstellar
    html += '      <div class="col-sm"> \n'
    html += '      <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/interstellar.jpg" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="interstellar" class="btn2"> Watch Interstellar </button> \n'
    html += '        </form> \n '
    html += '      </div> \n'

    # Movie Tenet
    html += '      <div class="col-sm"> \n'
    html += '      <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/tenet.jpg" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="tenet" class="btn2"> Watch Tenet </button> \n'
    html += '        </form> \n '
    html += '      </div> \n'

    # Movie Bumblebee
    html += '      <div class="col-sm"> \n'
    html += '      <form action="tussenSite.py" method="POST"> \n'
    html += '        <img src="../image/bumblebee.jpg" width="250px" height="370px"></img> \n'
    html += '        <button type="submit" name="inputName" value="bumblebee" class="btn2"> Watch Bumblebee </button> \n'
    html += '        </form> \n '
    html += '      </div> \n'

    html += '    </div> \n'
    html += '  </div> \n'
    html += '  </div> \n'
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

