import os
import sqlite3
import operator
from collections import OrderedDict
import csv

def readHistory_getURLs(path, output):
    # querying the db
    c = sqlite3.connect(path)
    cursor = c.cursor()
    select_statement = "SELECT urls.url FROM urls WHERE urls.url LIKE '%https://www.youtube.com/watch%' AND urls.visit_count > 2;"
    cursor.execute(select_statement)
    results = cursor.fetchall() #tuple
    
    # write to file
    result_list = []
    for x in results:
        if(len(x[0]) == 43):
            result_list.append( x[0] )

    with open(output, 'w') as myfile:
        for x in result_list:
            myfile.write(x + "\n")
    
    return myfile