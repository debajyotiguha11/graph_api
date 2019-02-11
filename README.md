# graph_api
Using Facebook Graph API to find users with similar interes : https://developers.facebook.com/docs/graph-api

## Screenshots
<p align="center">
  <img src="https://github.com/debajyotiguha11/graph_api/blob/master/img/img1.png" >
  <img src="https://github.com/debajyotiguha11/graph_api/blob/master/img/img2.png" >
  <img src="https://github.com/debajyotiguha11/graph_api/blob/master/img/img2.png" >
 </p>
 
 ## Steps
 1. Create a Developers in Facebook http://developers.facebook.com/
 2. Generate your accesstoken to test the app : https://developers.facebook.com/tools/explorer/
 3. Since API doesn't provide search from it's >2.0V we need to collect user information through the app.
 4. Create your business app and publish it with all Permissions needed.
 5. Through the app we can collect nessesary information about the user and store it in DB.
 6. Using full text searching find similar interests amoung users.
 
 ### Requirements
    Python >= 3.x
    Flask
    PyMySQL

## Installation

1. Clone and navigate to graph_api directory.

2. Run the Server (XAMPP/LAMPP).<br>
   for linux goto lampp directory and do-
    ```bash
    sudo ./xampp start
    ```
3. Run the python script.
    ```bash
    python3 app.py
    ```
    OR
   ```bash
    python3 cli.py
    ```
4. You're all done :)
5. To quit ctrl+c.

## Contribute

Want to work on the project? Any kind of contribution is welcome!

Follow these steps:
- Fork the project.
- Create a new branch.
- Make your changes and write tests when practical.
- Commit your changes to the new branch.
- Send a pull request.

- drop a mail to me for database file at debajyotiguha11@gmail.com

## Authors

***[Debjyoti Guha](https://github.com/debajyotiguha11/)***
