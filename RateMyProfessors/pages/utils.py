def getErrorMessage(form):
    emailErr = False
    userNameErr = False
    imgErr = False
    
    message = ''
            
    for field in form:
        if field.errors:
            if field.name == 'email':
                emailErr = True
            if field.name == 'username':
                userNameErr = True
            if field.name == 'image':
                imgErr = True
    
    
    if emailErr and userNameErr:
        message = 'Account with this Email and Username already exists'
    elif emailErr:
        message = 'Account with this Email address already exists.'
    elif userNameErr:
        message = 'Account with this Username address already exists.'
    elif imgErr:
        message = 'Invalid file format'
    
    return message
            
    
