cijferICOR = 6
cijferCSN = 7
cijferPROG = 6
gemiddelde = ((cijferCSN + cijferICOR + cijferPROG) / 3)
beloning = (cijferPROG + cijferICOR + cijferCSN) * 30
lst = ('mijn cijfers, gemiddeld een ' + str(gemiddelde) + ' leveren een beloning van: ' + str(beloning) + ' op')
print(lst)