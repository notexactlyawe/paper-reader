# -*- coding: utf-8 -*-
import pdb
import sqlite3
import wikipedia
from wikipedia.exceptions import PageError, DisambiguationError

class Wiki:
    def __init__(self):
        self.conn = sqlite3.connect("wiki.db")
        self.curs = self.conn.cursor()

    def get_for_concept(self, concept):
        try:
            page = wikipedia.page(concept)
        except PageError:
            return "Concept doesn't exist"
        link = "http://en.wikipedia.org/wiki/{}".format(concept)
        subs = self.get_subs(page)
        return [page.summary, link, subs]

    def get_subs(self, page):
        links_sq = []
        # Get links of links
        for link in page.links:
            page = self.get_page(link)
            if page:
                links_sq.append(page.links)
        # compute matrix of links
        links_mat = []
        for links in links_sq:
            temp_row = []
            for links2 in links_sq:
                if links == links2:
                    temp_row.append(0)
                else:
                    temp_row.append(len([elem for elem in links if elem in links2]))
            links_mat.append(temp_row)
        # get largest summed list and index
        mat_sum = [sum(i) for i in links_mat]
        top_idx = mat_sum.index(max(mat_sum))
        # return top few links from that list
        links_sorted = sorted(links_mat[top_idx], reverse=True)[:10]
        indexes = map(lambda x: links_mat[top_idx].index(x), links_sorted)
        return map(lambda x: page.links[x], indexes)

    def get_page(self, name):
        self.curs.execute(u"SELECT * FROM pages WHERE name = ?", (name, ))
        row = self.curs.fetchone()
        if row:
            return PageDuckClass(row[0], row[1].split(';'), row[2])
        try:
            page = wikipedia.page(name)
            self.curs.execute(u"INSERT INTO pages VALUES (?, ?, ?)", (name, ';'.join(page.links), page.summary))
            self.conn.commit()
        except PageError:
            return None
        except DisambiguationError:
            return None

class PageDuckClass():
    def __init__(self, name, links, summary):
        self.title = name
        self.summary = summary
        self.links = links

if __name__ == "__main__":
    w = Wiki()
    print w.get_for_concept("Bananas")
    w.conn.close()
