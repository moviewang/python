import redis


r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.set('hello', 'world')
print(r.get('hello').decode('utf-8'))