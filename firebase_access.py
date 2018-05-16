import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


certificate_path=r"C:\Users\dell\Desktop\books-db-1016e-firebase-adminsdk-8bkjt-44b915ea1a.json"
database_url="https://books-db-1016e.firebaseio.com/"
cred = credentials.Certificate(certificate_path)
firebase_admin.initialize_app(cred,{r'databaseURL': database_url})
ref = db.reference('books')
attribute_path = {'book name': 'book/name',
                  'publication name':'book/publication/name',
                  'publication address':'book/publication/adress',
                  'publication accuracy':'book/publication/accuracy',
                  'book field': 'book/subject/field',
                  'book resource' : 'book/resource/name',
                  'book accessibility': 'book/resource/accessibility',
                  'book author': 'book/author/name',
                  'book publication':'book/publication/name',
                  'book subject':'book/subject/name',
                  'author name':'book/author/name',
                  'book view':'book/resource/type',
                  'author bet midrash':'book/author/bet_midrash',
                  'author country':'book/author/country',
                  'author rav':'book/author/rav',
                  'author generation':'book/author/age'}



def books_by_parameter(path,parameter):
    return  ref.order_by_child(path).equal_to(parameter).get()

'''
def books_by_2_parameters(path1,parameter1,path2,parameter2):
    data1=books_by_parameter(path1,parameter1)
    data2=books_by_parameter(path2,parameter2)
    intersectional = set(data1.keys()) & set(data2.keys())
    result = []
    for item in data1.items():
        if item[0] in intersectional:
            result.append(item)
    return result
'''

def value_by_parameter_1st(path,parameter,val_path1):
    mybooks = books_by_parameter(path,parameter)
    values = mybooks.values()
    result = []
    for item in values:
        result.append(item['book'][val_path1])
    return list(set(result))


def value_by_2_parameters_1st(path1,parameter1,path2,parameter2,val_path1):
    mybooks1 = books_by_parameter(path1,parameter1)
    mybooks2 = books_by_parameter(path2, parameter2)
    intersectional = set(mybooks1.keys()) & set(mybooks2.keys())
    result = []
    for item in mybooks1.items():
        if item[0] in intersectional:
            result.append(item[1]['book'][val_path1])
    return list(set(result))


def value_by_parameter_2nd(path,parameter,val_path1,val_path2):
    mybooks = books_by_parameter(path,parameter)
    values = mybooks.values()
    result = []
    for item in values:
        result.append(item['book'][val_path1][val_path2])
    return list(set(result))


def value_by_2_parameters_2nd(path1,parameter1,path2,parameter2,val_path1,val_path2):
    mybooks1 = books_by_parameter(path1,parameter1)
    mybooks2 = books_by_parameter( path2, parameter2)
    intersectional = set(mybooks1.keys()) & set(mybooks2.keys())
    result = []
    for item in mybooks1.items():
        if item[0] in intersectional:
            result.append(item[1]['book'][val_path1][val_path2])
    return list(set(result))


def books_by_field(field):
    return value_by_parameter_1st('book/subject/field',field,'name')


def books_by_author(author):
    return value_by_parameter_1st('book/author/name',author,'name')


def books_by_resource(resource):
    return value_by_parameter_1st('book/resource/name',resource,'name')


def books_by_publication(publication):
    return value_by_parameter_1st('book/publication/name',publication,'name')


def free_accessible_books():
    return value_by_parameter_1st('book/resource/accessibility','free','name')


def in_charge_accessible_books():
    return value_by_parameter_1st('book/resource/accessibility','payment','name')


def pdf_formatted_books():
    return value_by_parameter_1st('book/resource/type','pdf','name')


def txt_formatted_books():
    return value_by_parameter_1st('book/resource/type','txt','name')


def books_by_subject(subject):
    return value_by_parameter_1st('book/subject/name',subject,'name')


def books_by_accessibility_and_format( accessibility, view):
    return value_by_2_parameters_1st('book/resource/accessibility',accessibility,'book/resource/type',view,'name')


def publications_by_address(address):
    return value_by_parameter_2nd('book/publication/adress',address,'publication','name')


def publications_by_accuracy(accuracy):
    return value_by_parameter_2nd( 'book/publication/accuracy', accuracy, 'publication', 'name')


def publications_by_address_and_accuracy(address,accuracy):
    return  value_by_2_parameters_2nd('book/publication/adress',address,'book/publication/accuracy',accuracy,'publication','name')


def author_by_country(country):
    return value_by_parameter_2nd( 'book/author/country', country, 'author', 'name')


def author_by_rav(rav):
    return value_by_parameter_2nd( 'book/author/rav', rav, 'author', 'name')


def author_by_age(age):
    return value_by_parameter_2nd( 'book/author/age', age, 'author', 'name')


def author_by_bet_midrash(bet_midrash):
    return value_by_parameter_2nd( 'book/author/bet_midrash', bet_midrash, 'author', 'name')


def author_by_bet_midrash_and_rav(bet_midrash,rav):
    return value_by_2_parameters_2nd( 'book/author/bet_midrash', bet_midrash,'book/author/rav', rav, 'author', 'name')


def author_by_country_and_rav(country,rav):
    return value_by_2_parameters_2nd( 'book/author/country', country,'book/author/rav', rav, 'author', 'name')


def author_by_country_and_age(country,age):
    return value_by_2_parameters_2nd( 'book/author/country', country,'book/author/age', age, 'author', 'name')


def author_by_country_and_bet_midrash(country,bet_midrash):
    return value_by_2_parameters_2nd( 'book/author/country', country,'book/author/bet_midrash', bet_midrash, 'author', 'name')


def author_by_age_and_bet_midrash(age,bet_midrash):
    return value_by_2_parameters_2nd( 'book/author/age', age,'book/author/bet_midrash', bet_midrash, 'author', 'name')


def handle_gui_requests(request,entries):
    entries_num = len(entries)
    if request=='book':
        if entries_num ==1:
            key=entries[0][0]
            value=entries[0][1]
            if key=='book name':
                pass
            elif key=='book field':
                return books_by_field(value)
            elif key=='book resource':
                return books_by_resource(value)
            elif key=='book accessibility':
                pass
            elif key=='book author':
                return  books_by_author(value)
            elif key=='book publication':
                return books_by_publication(value)
            elif key=='book subject':
                pass
            elif key=='book view':
                pass
            else:
                return ['Error - query not supported']
        elif entries_num==2:
            key1=entries[0][0]
            value1=entries[0][1]
            key2=entries[1][0]
            value2=entries[1][1]
            if key1 == 'book accessibility' and key2 =='book view':
                return books_by_accessibility_and_format(value1,value2)
            elif key2 == 'book accessibility' and key1 =='book view':
                return books_by_accessibility_and_format(value2,value1)
            else:
                return ['Error - query not supported']
        else:
            return ['Error - you can use maximum 2 arguments']
    elif request=='publication':
        if entries_num ==1:
            key=entries[0][0]
            value=entries[0][1]
            if key=='publication name':
                pass
            elif key=='publication address':
                return publications_by_address(value)
            elif key== 'publication accuracy':
                return publications_by_accuracy(value)
            else:
                return ['Error - query not supported']
        elif entries_num==2:
            key1=entries[0][0]
            value1=entries[0][1]
            key2=entries[1][0]
            value2=entries[1][1]
            if key1 == 'publication address' and key2 =='publication accuracy':
                return publications_by_address_and_accuracy(value1,value2)
            elif key2 == 'publication address' and key1 =='publication accuracy':
                return publications_by_address_and_accuracy(value2,value1)
            else:
                return ['Error - query not supported']
        else:
            return ['Error - you can use maximum 2 arguments']
    elif request=='author':
        if entries_num ==1:
            key=entries[0][0]
            value=entries[0][1]
            if key=='author name':
                pass
            elif key=='author bet midrash':
                return author_by_bet_midrash(value)
            elif key=='author country':
                return author_by_country(value)
            elif key=='author rav':
                return author_by_rav(value)
            elif key=='author generation':
                return author_by_age(value)
            return ['Error - query not supported']
        elif entries_num==2:
            key1=entries[0][0]
            value1=entries[0][1]
            key2=entries[1][0]
            value2=entries[1][1]
            if 'author country' in [key1,key2]:
                if 'author rav' in [key1,key2]:
                    if key1 == 'author country' and key2 == 'author rav':
                        return author_by_country_and_rav(value1, value2)
                    elif key2 == 'author country' and key1 == 'author rav':
                        return author_by_country_and_rav(value2, value1)
                    else:
                        return ['Error - query not supported']
                elif 'author generation' in [key1,key2]:
                    if key1 == 'author country' and key2 == 'author generation':
                        return author_by_country_and_age(value1, value2)
                    elif key2 == 'author country' and key1 == 'author generation':
                        return author_by_country_and_age(value2, value1)
                    else:
                        return ['Error - query not supported']
                elif 'author bet midrash' in [key1,key2]:
                    if key1 == 'author country' and key2 == 'author bet midrash':
                        return author_by_country_and_age(value1, value2)
                    elif key2 == 'author country' and key1 == 'author bet midrash':
                        return author_by_country_and_age(value2, value1)
                    else:
                        return ['Error - query not supported']
                else:
                    return ['Error - query not supported']
            elif key1 == 'author generation' and key2 == 'author bet midrash':
                return author_by_age_and_bet_midrash(value1, value2)
            elif key2 == 'author generation' and key1 == 'author bet midrash':
                return author_by_age_and_bet_midrash(value2, value1)
            else:
                return ['Error - query not supported']

        else:
            return ['Error - you can use maximum 2 arguments']
    return ["Unknown error"]

'''
attribute_path = {'book name': 'book/name',
                  'book field': 'book/subject/field',
                  'book resource' : 'book/resource/name',
                  'book accessibility': 'book/resource/accessibility',
                  'book author': 'book/author/name',
                  'book publication':'book/publication/name',
                  'book subject':'book/subject/name',
                  'author name':'book/author/name',
                  'book view':'book/resource/type',
                  'publication name':'book/publication/name',
                  'publication address':'book/publication/adress',
                  'publication accuracy':'book/publication/accuracy',
                  'author bet midrash':'book/author/bet_midrash',
                  'author country':'book/author/country',
                  'author rav':'book/author/rav',
                  'author generation':'book/author/age'}
                    
'''
def list_print(list):
    for l in list:
        print l
