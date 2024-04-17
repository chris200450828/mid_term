class FuncStuff:
    def __init__(self, soup):    #初始化類別,接受一個變數,通常為soup
        self.soup = soup

    def _get_data_list(self):    #抓取資料函式,通常而言不會在main裡call到這個函式
        link_l, title_l, author_l = [], [], []
        grand = self.soup.find_all('div', class_="r-ent")    #先抓取最上層連結
        for i in grand:    #用迴圈遍歷
            try:
                tag_title = i.find('div', class_="title").find('a')    #標題抓取
                title_l.append(tag_title.string)
            except AttributeError as DeletedObject:    #如果遇到None則執行下方
                tag_title = i.find('div', class_="title")
                title_l.append(tag_title.string)
            try:
                link = tag_title.get('href')    #同上
                link_l.append(link)
            except AttributeError as DeletedObject:    #同上
                link = "Deleted"
                link_l.append(link)
            author = i.find("div", class_='meta').find("div", class_='author')
            author_l.append(author.string)

        return link_l, title_l, author_l    #回傳變數

    def print_out(self):    #打印出變數
        link, title, author = self._get_data_list()    #於print_out內部呼叫_get_data_list
        loop_time = len(author)    #取得迴圈執行次數

        for i in range(loop_time):    #用迴圈遍歷
            print(link[i])
            print(title[i])
            print(author[i])
            print("----------------------------------------------")
