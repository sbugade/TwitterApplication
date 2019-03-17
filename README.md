# TwitterApplication
Program to read the input file generated and get the value of the number of records to be displayed from the user and generates the output based on tweets and write them into separate files.

Twitter Application
Creating text file for given search pattern as below -
Script - tweeter.py
1. We need two inbuilt packages from python like tweepy and time
to use twitter inbuilt functions.
2. The program requires below inputs from user
• SEARCH string through which we can analyze the tweets
• From date and to date
• Access secret and token
• Consumer key and token
• Number of tweets that we want to retrieve
3. The program creates file with search pattern name as
SEARCH.txt
4. By passing consumer key and secret to tweeter authentication
handler, we can check for authentication
5. After authentication program require access key and secret to
access actual tweets.
6. The program calls tweeter API by passing all this authentication
information.
7. Now using above API information program fetch all tweets from
date to mentioned TO date with search string pattern and store
it in input file.

Now a program to read the file generated and should get the value of n
(the number of records to be displayed) from the user and generate the
following output and write them into separate files.
Script - tweeter_challenge.py
1. Provide Input file path
2. Number of records you want to fetch

You can also:
Import and save files from GitHub
