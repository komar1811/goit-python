dictionary = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'shch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ia', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
      'Ж':'Zh','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'Ch','Ш':'Sh','Щ':'Shch','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'Ya','ґ':'g','Ґ':'G',
      'Є':'E'}

def normalize(text):
      translated = []
      for letter in text:
            if letter in dictionary.keys():
                  translated.append(dictionary[letter])
            elif letter in set(['1','2','3','4','5','6','7','8','9','0']):
                  translated.append(letter)
            else:
                  translated.append('_')
      return ''.join(translated)






