import pusher

pusher_client = pusher.Pusher(
    app_id='',
    key='',
    secret='',
    cluster=''
)


if __name__ == '__main__':
    pusher_client.trigger(channels='', event_name='notification',
                          data=dict(title='Test Title', body='test Body'))
