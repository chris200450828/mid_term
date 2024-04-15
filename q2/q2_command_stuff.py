class FuncStuff:
    def __init__(self, soup):
        self.soup = soup

    def _get_data_list(self):
        link_l, title_l, author_l = [], [], []
        grand = self.soup.find_all('div', class_="r-ent")
        for i in grand:
            try:
                tag_title = i.find('div', class_="title").find('a')
                title_l.append(tag_title.string)
            except AttributeError as DeletedObject:
                tag_title = i.find('div', class_="title")
                title_l.append(tag_title.string)
            try:
                link = tag_title.get('href')
                link_l.append(link)
            except AttributeError as DeletedObject:
                link = "Deleted"
                link_l.append(link)
            author = i.find("div", class_='meta').find("div", class_='author')
            author_l.append(author.string)

        return link_l, title_l, author_l

    def print_out(self):
        link, title, author = self._get_data_list()
        loop_time = len(author)

        for i in range(loop_time):
            print(link[i])
            print(title[i])
            print(author[i])
            print("----------------------------------------------")
