import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    reco_movie_list=[]
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=d838f386c11255ef5f578f676243694f&query={title}'
    response = requests.get(URL).json()

    if response['results']==[]:
        return None
    for i in response['results'][0]:
        if i=='id':
            movie_id=response['results'][0][i]
    reco=f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=d838f386c11255ef5f578f676243694f&query='
    reco_response = requests.get(reco).json()
    for i in reco_response['results']:
        for j in i:
            if j=='title':
                reco_movie_list.append(i[j])
    if len(reco_movie_list)==0:
        return []
    else:
        return reco_movie_list
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
