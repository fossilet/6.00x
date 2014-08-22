def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    templates = ('[ADJ]', '[VERB]', '[NOUN]')
    words = madLibsForm.split()
    return [word for word in words if word in templates]
