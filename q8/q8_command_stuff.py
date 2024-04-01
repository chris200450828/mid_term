def get_data(data, pop=None):
    title_list = []
    authors_list = []
    link_list = []
    publisher_list = []
    publishedDate_list = []

    if 'items' in data:
        for item in data['items']:
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', 'Unknown Title')
            link = item.get('selfLink')
            authors = volume_info.get('authors')[0]
            publishDate = volume_info.get('publishedDate')
            publisher = volume_info.get('publisher')

            title_list.append(title)
            authors_list.append(authors)
            link_list.append(link)
            publisher_list.append(publisher)
            publishedDate_list.append(publishDate)

    if pop is True:
        print(title_list)
        print(authors_list)
        print(link_list)
        print(publisher_list)
        print(publishedDate_list)

    return title_list, authors_list, link_list, publisher_list, publishedDate_list


def merge(first, second):
    result = first + second
    return result


