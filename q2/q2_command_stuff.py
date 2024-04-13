class FuncStuff:
    def __init__(self, soup):
        self.soup = soup

    def _get_data_list(self):
        link_l, title_l, author_l = [], [], []
        grand = self.soup.find_all('div', class_="r-ent")
        for i in grand:
            tag_title = i.find('div', class_="title").find('a')
            link = tag_title.get('href')
            author = i.find("div", class_='meta').find("div", class_='author')
            if tag_title.string:
                link_l.append(link)
                title_l.append(tag_title.string)
            else:
                link_l.append('Deleted')
                title_l.append(tag_title.string)
            author_l.append(author.string)

        return link_l, title_l, author_l

    def print_out(self):
        link, time, author = self._get_data_list()
        loop_time = len(link)

        for i in range(loop_time):
            print(link[i])
            print(time[i])
            print(author[i])
            print("----------------------------------------------")
