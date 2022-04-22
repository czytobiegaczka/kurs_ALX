def formatuj(*args, **kwargs):

    napis = '\n'.join(args)
    for key, item in kwargs.items():
       napis = napis.replace('$'+key, str(item))

    # for kwarg in kwargs:
    #     napis = napis.replace('$' + kwarg, str(kwargs[kwarg]))

    return napis


print(formatuj('koszt $cena PLN', 'kwota $cena BRUTTO', cena = 10))