import re


#1 
def is_vowel(char):
    if re.findall(r'[^aeiou]*[aeiuo]', char):
        return True
    else:
        return False

#2
def is_valid_user_name(the_name):
    #starts with lowercase letter
    #only has lowercase letters
    #no longer than 32 chars    
    if (re.search('^[a-z]+[a-z0-9-_]$', the_name) and len(the_name) < 32):
        return True
    else:
        return False
                
        
#3 
def format_phone(the_number):
    # 3 consecutive digits, 
    # followed by 3 consecutive digits,
    # followed by 4 consecutive digits is all thats important
    three = re.findall('\d{3}', the_number)
    four = re.findall('\d{4}', the_number)
    
    if len(three) < 3:
        return three[0] + four[0]
    else:
        return three[0] + three[1] + four[0]

#4
def format_date(the_date):
    date = re.findall('\d{2}', the_date)   
    return '20' + date[2] + "-" +  date[1] + '-' + date[0]
    


#5 
def extract_log_file():
    return 0
    
    
    
    





