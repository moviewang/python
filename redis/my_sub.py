from spider.redis.RedisHelper import RedisHelper

obj = RedisHelper()
sub = obj.subscribe()

while True:
    msg = sub.parse_response()
    print('msg:', msg.decode('utf-8'))
