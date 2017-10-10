def lang_genoeg():
    lengte = int(input('hoe lang ben je?: '))
    if lengte >= 140:
        return 'je bent lang genoeg!'
    else:
        return 'je bent nog niet lang genoeg!'

print(lang_genoeg())
