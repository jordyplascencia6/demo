from flask import Flask
import sys
import logging
import json


App = Flask(__name__)
@App.route('/palindrome/<word>', methods = ['GET'])
def palindrome(word):
    response = {'message': 'success'}
    logging.info("Word received: [" + str(word) + "]")
    jsonResponse = buildJSON(word)
    logging.info("JSON obtained: {" + jsonResponse + "}")

    return jsonResponse


def buildJSON(word):
    def voltearPal(x):
      return x[::-1]
    palindromo = {}
    palabras = {}
    dct = {}
        # palindromo = str(input("Please type the string: "))
    palindromo = word
        # print(palindromo)
        
    cant = len (palindromo) 
    palabras = voltearPal(palindromo)
    for i in palindromo:
        if i in dct:
            dct[i] +=1
        else:
            dct[i] =1

    if (palindromo == palabras):
        falsePal = True
        x = {
            "name": palindromo,
            "palindrome": falsePal,
            "sorted": dct,
            "length": cant
            }
        
        y = json.dumps(x)
        # jsonFile = open("data.json", "w")
        # jsonFile.write(y)
        # jsonFile.close()
        
        print(y)
        
    else:
        truePal = False
        j = {
            "name": palindromo,
            "palindrome": truePal
            }

        y = json.dumps(j)
        print(y)
    return y


if __name__ == "__main__":
    App.run(host='0.0.0.0', debug=True, port=8080)
