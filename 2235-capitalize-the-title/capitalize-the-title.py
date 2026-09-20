class Solution(object):
    def capitalizeTitle(self, title):
        l=[]
        title=title.split()
        for w in title:
            if len(w)<=2:
                l.append(w.lower())
            else:
                l.append(w[0].upper()+w[1:].lower())
        return " ".join(l)

        
        