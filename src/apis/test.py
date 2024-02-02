from sqlalchemy.orm import Session
from crud import crud_test
from core.redis_config import redis_config
# redis 설정파일 불러오기

def test_index(db):
	something = crud_test.get_items(db)
	return something
	
# url이 /items/redis_test일 경우 실행되는 함수
async def redis_test():
	rd = redis_config()
	rd.set("juice", "orange") # set
	
	return {
	    "data": rd.get("juice") # get
	}