import redis

r = redis.Redis(host='127.0.0.1', port= 6379)
#string
r.set('python', 'hello python', )
r.setex('java', 'hello java', 10)
r.mset({'name1':'zhangsan', 'name2' : 'lisi'})

print(r.get('name'))
print(r.mget('name1', 'name2'))
#hash
r.hset('programer', 'name', 'wangdianyong')
print(r.hget('programer', 'name'))

student = {'name':'jack', 'age': 16, 'grade':'junior'}
r.hmset('jack', student)
print(r.hmget('jack','name', 'age', 'grade'))
print(r.hlen('jack'))
print(r.hkeys('jack'))
print(r.hvals('jack'))
print(r.hexists('jack', 'jack'))
r.hdel('jack', 'grade')
print(r.hmget('jack', 'name', 'age', 'grade'))

#List
# r.lpush('my_list', 1, 2, 3, 4)
# r.rpush('my_list', 1, 2, 3, 4)
print(r.lrange('my_list',0 , -1))
r.lpop('my_list')
print(r.llen('my_list'))
r.lpush('list4', 1, 3, 5)
r.lpush('list5', 1, 3, 5)

print(r.blpop(['list4', 'list5'], timeout=0))
print(r.lrange('list4', 0, -1), r.lrange('list5', 0, -1))
#Set
# r.sadd('my_set', 'aa', 'bb')
print(r.smembers('my_set'))
r.sadd('my_set', 'aa')
print(r.smembers('my_set'))
print('my_set size:', r.scard('my_set'))
print(r.sismember('my_set', 'cc'))
print(r.spop('my_set'))
#zset
r.zadd('my_zset', 'a1', 6, 'a2', 3, 'a3', 7)
print(r.zcard('my_zset'))
#分数在[min, max]之间的个数
print(r.zcount('my_zset', 1, 6))
print(r.zincrby('my_zset', 'a1', amount=2))

print(r.zrange('my_zset', 0, 3, False, True, score_cast_func=float))
print(r.zrevrange('my_zset', 0, 2, True))
print(r.zrank('my_zset', 'a1'))
print(r.zrank('my_zset', 'a2'))
print(r.zrank('my_zset', 'a3'))
print(r.zscore('my_zset', 'a1'))
print(r.zrem('my_zset', 'a1'))
print(r.zscore('my_zset', 'a1'))