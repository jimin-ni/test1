#** 카카오 로그인을 위한 예외처리 

class SocialLoginException(Exception):
    pass


class KakaoException(Exception):
    pass

class GithubException(Exception):
    pass