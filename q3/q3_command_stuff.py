from urllib.parse import urljoin
import pandas


class FuncStart:
    def __init__(self, soup, history_soup):
        self.soup = soup
        self.history_soup = history_soup

    def _get_data(self):
        currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l = [], [], [], [], []
        table = self.soup.find("table", {"title": "牌告匯率"}).find("tbody")
        for row in table.find_all("tr"):
            cells = row.find_all("td")

            currency = cells[0].text.strip()
            cash_buy = cells[1].text.strip()
            cash_sell = cells[2].text.strip()
            spot_buy = cells[3].text.strip()
            spot_sell = cells[4].text.strip()

            cash_buy_l.append(cash_buy)
            cash_sell_l.append(cash_sell)
            currency_l.append(currency)
            spot_buy_l.append(spot_buy)
            spot_sell_l.append(spot_sell)

        return currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l

    def print_out(self):
        currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l = self._get_data()
        loop_time = len(currency_l)
        for i in range(loop_time):
            print(currency_l[i])
            print(cash_buy_l[i])
            print(cash_sell_l[i])
            print(spot_buy_l[i])
            print(spot_sell_l[i])

    def _history_data(self):
        table = self.history_soup.find("table", {"title": "歷史匯率收盤價"}).find("tbody")
        currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l = [], [], [], [], []

        for row in table.find_all("tr"):
            cells = row.find_all("td")

            currency = cells[0].text.strip()
            cash_buy = cells[1].text.strip()
            cash_sell = cells[2].text.strip()
            spot_buy = cells[3].text.strip()
            spot_sell = cells[4].text.strip()

            cash_buy_l.append(cash_buy)
            cash_sell_l.append(cash_sell)
            currency_l.append(currency)
            spot_buy_l.append(spot_buy)
            spot_sell_l.append(spot_sell)

        return currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l

    def print_out_history(self):
        currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l = self._history_data()
        loop_time = len(currency_l)
        for i in range(loop_time):
            print(currency_l[i])
            print(cash_buy_l[i])
            print(cash_sell_l[i])
            print(spot_buy_l[i])
            print(spot_sell_l[i])

    def get_forward_url(self):
        table = self.soup.find("table", {"title": "牌告匯率"}).find("tbody")
        forward_l = []
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            forward = cells[5].find('a')
            forward_l.append(forward.get('href'))
        return forward_l

    def dealed_url(self):
        base_url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
        forward_l = self.get_forward_url()
        result_forward = []
        for forward in forward_l:
            result_forward.append(urljoin(base_url, forward))

        return result_forward

    def get_forward_data(self, forward_soup):
        date_l, buy_l, sell_l = [], [], []
        forward_soup = forward_soup
        title = forward_soup.find('th', class_='currency').find('div').find('div').find('div', class_='hidden-phone')
        table_rows = forward_soup.find("table", {"title": "遠期匯率"}).find("tbody").find_all('tr')
        for i in table_rows:
            cells = i.find_all('td')
            date = cells[0].text.strip()
            buy_in = cells[1].text.strip()
            sell_out = cells[2].text.strip()
            result = title.text.strip() + '-' + date
            date_l.append(result)
            buy_l.append(buy_in)
            sell_l.append(sell_out)

        return date_l, buy_l, sell_l

    def save_csv(self, opt=None):
        currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l = self._get_data()
        h_currency_l, h_cash_buy_l, h_cash_sell_l, h_spot_buy_l, h_spot_sell_l = self._history_data()
        if opt is True:
            print("saving current rate and history rate in different csv file")
            current_result = zip(currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l)
            history_result = zip(h_currency_l, h_cash_buy_l, h_cash_sell_l, h_spot_buy_l, h_spot_sell_l)

            df = pandas.DataFrame(current_result,
                                  columns=['幣別', '現今本行買入', '現今本行賣出', '即期匯率-本行買入',
                                           ' 即期匯率-本行賣出'])
            hist_df = pandas.DataFrame(history_result,
                                       columns=['歷史-幣別', '歷史-現今本行買入', '歷史-現今本行賣出',
                                                '歷史-即期匯率-本行買入',
                                                ' 歷史-即期匯率-本行賣出'])

            df.to_csv('bank.csv', index=False, encoding='utf-8-sig')
            hist_df.to_csv('history_bank.csv', index=False, encoding='utf-8-sig')

        else:
            print("saving current rate and history rate in different csv file")
            result = zip(currency_l, cash_buy_l, cash_sell_l, spot_buy_l, spot_sell_l, h_currency_l, h_cash_buy_l,
                         h_cash_sell_l, h_spot_buy_l, h_spot_sell_l)

            df = pandas.DataFrame(result,
                                  columns=['幣別', '現今本行買入', '現今本行賣出', '即期匯率-本行買入',
                                           ' 即期匯率-本行賣出', '歷史-幣別', '歷史-現今本行買入', '歷史-現今本行賣出',
                                           '歷史-即期匯率-本行買入',
                                           ' 歷史-即期匯率-本行賣出'])

            df.to_csv('bank', index=False, encoding='utf-8-sig')

    def to_forward_csv(self, filename, result):
        result = result
        df = pandas.DataFrame(result, columns=['時間', '本行買入匯率', '本行賣出匯率'])
        filename = filename + '_forward_rate.csv'
        df.to_csv(filename, index=False, encoding='utf-8-sig')
