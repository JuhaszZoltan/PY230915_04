# listák
# összetett adatszerkezetek
# olyan kollekciók, melyekben több érték van
# a pythonban a listák alapvetően heterogének
# mi CSAK homogén listákkal fogunk foglalkozni

#                       0       1         2
allatok:list[str] = ['cica', 'kutya', 'kecske']

# lista adott elemére az indexével hivatkozunk
# ún. 'zero based indexing'
# van a programozásban alapértelmezetten

# adott elemet az ls_neve[index]-el érem el:

print(allatok[1])

# ha a print-nek átadom a lista nevét, kiírja rendre annak minden elemét
print(allatok)

# elem 'felülírása'
allatok[1] = 'pingvin'
print(allatok)

# append: a lst végére ad hozzá elemet
allatok.append('kutya')
print(allatok)

# insert: már létező helyre beszúrás
allatok.insert(0, 'csincsilla')
print(allatok)

# lista elemének eltávolítása érték alapján:
allatok.remove('cica')
print(allatok)

# lista bejárható for-al (de ezt már néztük)

