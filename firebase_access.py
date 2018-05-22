import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


certificate_path=r"C:\Users\dell\PycharmProjects\firebase_project\final\books-db-1016e-firebase-adminsdk-8bkjt-44b915ea1a.json"
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

def books_by_parameter_2(path,parameter):
    return  ref.order_by_child(path).start_at(parameter).end_at(parameter+"zzzzz").get()

def value_by_n_parameters(parameters, val):
    #path for the value
    my_path = attribute_path[val]
    path_list = my_path.split('/')
    val_length = len(path_list) - 1
    #get all the books by parameters
    print parameters
    mybooks=[]
    for parrram in parameters:
        param_path=attribute_path[parrram[0]]
        mybooks.append(books_by_parameter_2(param_path,parrram[1]))
    #get intesection from the results
    intersectional = set(mybooks[0].keys())
    if len(mybooks)>1:
        for item in mybooks:
            intersectional= intersectional & set(item.keys())
    #extract the value
    result = []
    if val_length == 1:
        for item in mybooks[0].items():
            if item[0] in intersectional:
                result.append(item[1]['book'][path_list[1]])
    elif val_length == 2:
        for item in mybooks[0].items():
            if item[0] in intersectional:
                result.append(item[1]['book'][path_list[1]][path_list[2]])
    return list(set(result))



def handle_gui_requests(request,entries):
    if request=='book':
        return value_by_n_parameters(entries,'book name')
    elif request == 'publication':
        return value_by_n_parameters(entries, 'publication name')
    elif request=='author':
        return value_by_n_parameters(entries,'author name')
    else:
        return ["Unknown request"]

def list_print(list):
    for l in list:
        print l

