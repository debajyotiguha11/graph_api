import facebook

token = input("enter your access token: ")
graph = facebook.GraphAPI(access_token=token)
post = graph.get_object(id='me', fields='id,name,posts,hometown')
col = ['id', 'name', 'hometown', 'posts ']
row = [post['id'], post['name'], post['hometown']['name']]

print(post['id'])
for message in post['posts']['data']:
    try:
        row.append(message['message'])
    except KeyError:
        pass
print(row)

