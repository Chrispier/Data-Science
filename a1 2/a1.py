"""
Module for Currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Author: Mr. Park
"""
from urllib.request import urlopen
import json

def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return(s[0:s.find(" ")])


def after_space(s):
    """
    Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    return(s[s.find(" ")+1:])


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that 
    delimits it.  We typically use single quotes (') to delimit a 
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C', 
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes
    """
    startIndex = s.find('"')
    endIndex = s.find('"',startIndex+1)
    return s[startIndex + 1:endIndex]

def get_lhs(json):
    """
    Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
        
    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    lhsIndex = json.find('lhs')
    searchIndex = lhsIndex + 4
    return first_inside_quotes(json[searchIndex:])    


def get_rhs(json):
    """
    Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the 
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'

    then this function returns '19995.85429186 Euros' (not 
    '"38781.518240835 Euros"').  

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    rhsIndex = json.find('rhs')
    searchIndex = rhsIndex + 4
    return first_inside_quotes(json[searchIndex:])  


def currency_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the 
    currency dst. The response should be a string of the form    

    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value 
    and name for the original and new currencies. If the query is 
    invalid, both old-amount and new-amount will be empty, while 
    "ok" will be followed by the value false (and "err" will have 
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string with no spaces or non-letters
        
    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string with no spaces or non-letters
        
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    import urllib.request
    page = urllib.request.urlopen('http://cs1110.cs.cornell.edu/2023fa/a1?src='+src + '&dst=' + dst + '&amt=' + str(amt))
    return (str(page.read()))
    

def exchange(old, new, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency 
    old to the currency new. The value returned represents the 
    amount in currency new.

    The value returned has type float.

    Parameter old: the currency on hand
    Precondition: old is a string for a valid currency code
        
    Parameter new: the currency to convert to
    Precondition: new is a string for a valid currency code
        
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    json = currency_response(old, new, amt)
    return(get_rhs(json))
    



def query_website(old, new, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency old to the 
    currency new. The response should be a string of the form    

    '{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value 
    and name for the old and new currencies. If the query is 
    invalid, both old-amount and new-amount will be empty, while 
    "err" will have an error message.

    Parameter old: the currency on hand
    Precondition: old is a string with no spaces or non-letters
        
    Parameter new: the currency to convert to
    Precondition: new is a string with no spaces or non-letters
        
    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    response = urlopen("http://cs1110.cs.cornell.edu/2022fa/a1/?"+"")
    data_json = json.loads(response.read())