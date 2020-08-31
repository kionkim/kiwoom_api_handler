class OrderType(object):
    """키움 OPEN API+ sendOrder의 orderType에 대응되는 주문"""

    TYPE = {
        1: "신규매수",
        2: "신규매도",
        3: "매수취소",
        4: "매도취소",
        5: "매수정정",
        6: "매도정정",
    }


class ChejanGubun(object):

    TYPE= {"0": "주문접수/주문체결", "1": "잔고통보", "3": "특이신호"}


class FidList(object):
    """ receiveChejanData() 이벤트 메서드로 전달되는 FID 목록 """

    ALL = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "9203": "ORDER_NO",  # 주문번호
        #"9205": "관리자사번",
        "9001": "TICKER",  # 종목코드
        "912": "주문업무분류",
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "302": "NAME",  # 종목명
        "900": "ORDER_QTY",  # 주문수량
        "901": "ORDER_PRICE",  # 주문가격
        "902": "UNEX_QTY",  # 미체결수량
        "903": "체결누계금액",
        "904": "ORIGINAL_ORDER_NO",
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "909": "TRAN_NO",  # 체결번호
        "910": "체결가",
        "911": "체결량",
        "10": "현재가",
        "27": "(최우선)매도호가",
        "28": "(최우선)매수호가",
        "914": "TRAN_PRICE",  # 단위체결가
        "915": "TRAN_QTY",  # 단위체결량
        "938": "당일매매수수료",
        "939": "당일매매세금",
        "919": "거부사유",
        "920": "화면번호",
        "921": "터미널신호",
        "922": "신용구분",
        "923": "대출일",
        "917": "신용구분",
        "916": "대출일",
        "930": "보유수량",
        "931": "매입단가",
        "932": "총매입가",
        "933": "주문가능수량",
        "945": "당일순매수수량",
        "946": "BUY_SELL_GUBUN",  # 매도/매수구분 (주문상태: 체결인 경우)
        "950": "당일총매도손익",
        "951": "예수금",
        "307": "기준가",
        "8019": "손익율",
        "957": "신용금액",
        "958": "신용이자",
        "959": "담보대출수량",
        "918": "만기일",
        "990": "당일실현손익(유가)",
        "991": "당일신현손익률(유가)",
        "992": "당일실현손익(신용)",
        "993": "당일실현손익률(신용)",
        "397": "파생상품거래단위",
        "305": "상한가",
        "306": "하한가",
    }

    # DB에 저장할 column은 key를 영어로 작성
    SUBMITTED = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "9203": "ORDER_NO",  # 주문번호
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "901": "ORDER_PRICE",  # 주문가격
        "900": "ORDER_QTY",  # 주문수량
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "904": "ORIGINAL_ORDER_NO",
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "9001": "TICKER",  # 종목코드
        "302": "NAME",  # 종목명
        "902": "UNEX_QTY",  # 미체결수량
    }
    CANCELLED = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "302": "NAME",  # 종목명
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "9203": "ORDER_NO",  # 주문번호
        "901": "ORDER_PRICE",  # 주문가격
        "900": "ORDER_QTY",  # 주문수량
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "904": "ORIGINAL_ORDER_NO",
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "9001": "TICKER",  # 종목코드
    }
    EXECUTED = {
        "9201": "ACCOUNT_NO",  # 계좌번호
        "9203": "ORDER_NO",  # 주문번호
        "9001": "TICKER",  # 종목코드
        "913": "ORDER_STATUS",  # 주문상태: "접수", "체결"
        "302": "NAME",  # 종목명
        "900": "ORDER_QTY",  # 주문수량
        "901": "ORDER_PRICE",  # 주문가격
        "902": "UNEX_QTY",  # 미체결수량
        "904": "ORIGINAL_ORDER_NO",
        "905": "ORDER_GUBUN",  # 주문구분: "+매수", "-매도", "매수취소" ..
        "906": "HOGA_TYPE",  # 매매구분: "보통", "시장가"..
        "907": "SELL_BUY_GUBUN",  # 매도수구분 : (1:매도, 2:매수, 주문상태; 접수인 경우)
        "908": "ORDER_TRAN_TIME",  # 주문/체결시간
        "909": "TRAN_NO",  # 체결번호
        "914": "TRAN_PRICE",  # 단위체결가
        "915": "TRAN_QTY",  # 단위체결량
    }
class ReturnCode(object):
    """ 키움 OpenApi+ 함수들이 반환하는 값 """

    OP_ERR_NONE = 0  # 정상처리
    OP_ERR_FAIL = -10  # 실패
    OP_ERR_LOGIN = -100  # 사용자정보교환실패
    OP_ERR_CONNECT = -101  # 서버접속실패
    OP_ERR_VERSION = -102  # 버전처리실패
    OP_ERR_FIREWALL = -103  # 개인방화벽실패
    OP_ERR_MEMORY = -104  # 메모리보호실패
    OP_ERR_INPUT = -105  # 함수입력값오류
    OP_ERR_SOCKET_CLOSED = -106  # 통신연결종료
    OP_ERR_SISE_OVERFLOW = -200  # 시세조회과부하
    OP_ERR_RQ_STRUCT_FAIL = -201  # 전문작성초기화실패
    OP_ERR_RQ_STRING_FAIL = -202  # 전문작성입력값오류
    OP_ERR_NO_DATA = -203  # 데이터없음
    OP_ERR_OVER_MAX_DATA = -204  # 조회가능한종목수초과
    OP_ERR_DATA_RCV_FAIL = -205  # 데이터수신실패
    OP_ERR_OVER_MAX_FID = -206  # 조회가능한FID수초과
    OP_ERR_REAL_CANCEL = -207  # 실시간해제오류
    OP_ERR_ORD_WRONG_INPUT = -300  # 입력값오류
    OP_ERR_ORD_WRONG_ACCTNO = -301  # 계좌비밀번호없음
    OP_ERR_OTHER_ACC_USE = -302  # 타인계좌사용오류
    OP_ERR_MIS_2BILL_EXC = -303  # 주문가격이20억원을초과
    OP_ERR_MIS_5BILL_EXC = -304  # 주문가격이50억원을초과
    OP_ERR_MIS_1PER_EXC = -305  # 주문수량이총발행주수의1%초과오류
    OP_ERR_MIS_3PER_EXC = -306  # 주문수량이총발행주수의3%초과오류
    OP_ERR_SEND_FAIL = -307  # 주문전송실패
    OP_ERR_ORD_OVERFLOW = -308  # 주문전송과부하
    OP_ERR_MIS_300CNT_EXC = -309  # 주문수량300계약초과
    OP_ERR_MIS_500CNT_EXC = -310  # 주문수량500계약초과
    OP_ERR_ORD_WRONG_ACCTINFO = -340  # 계좌정보없음
    OP_ERR_ORD_SYMCODE_EMPTY = -500  # 종목코드없음

    CAUSE = {
        0: "정상처리",
        -10: "실패",
        -100: "사용자정보교환실패",
        -102: "버전처리실패",
        -103: "개인방화벽실패",
        -104: "메모리보호실패",
        -105: "함수입력값오류",
        -106: "통신연결종료",
        -200: "시세조회과부하",
        -201: "전문작성초기화실패",
        -202: "전문작성입력값오류",
        -203: "데이터없음",
        -204: "조회가능한종목수초과",
        -205: "데이터수신실패",
        -206: "조회가능한FID수초과",
        -207: "실시간해제오류",
        -300: "입력값오류",
        -301: "계좌비밀번호없음",
        -302: "타인계좌사용오류",
        -303: "주문가격이20억원을초과",
        -304: "주문가격이50억원을초과",
        -305: "주문수량이총발행주수의1%초과오류",
        -306: "주문수량이총발행주수의3%초과오류",
        -307: "주문전송실패",
        -308: "주문전송과부하",
        -309: "주문수량300계약초과",
        -310: "주문수량500계약초과",
        -340: "계좌정보없음",
        -500: "종목코드없음",
    }


class TRName:
    OPT10001 = "주식기본정보요청"
    OPT10002 = "주식거래원요청"
    OPT10003 = "체결정보요청"
    OPT10004 = "주식호가요청"
    OPT10005 = "주식일주월시분요청"
    OPT10006 = "주식시분요청"
    OPT10014 = "공매도추이요청"
    OPT10016 = "신고가저가요청"
    OPT10019 = "가격급등락요청"
    OPT10023 = "거래량급증요청"
    OPT10031 = "전일거래량상위요청"
    OPT10059 = "종목별투자자기관별요청"
    OPT10072 = "일자별종목별실현손익요청"
    OPT10074 = "일자별실현손익요청"
    OPT10075 = "실시간미체결요청"
    OPT20002 = "업종별주가요청"
    OPT10080 = "주식분봉차트조회요청"
    OPTKWFID = "관심종목정보요청"
    OPW00001 = "예수금상세현황요청"
    OPW00004 = "계좌평가현황요청"
    OPW00007 = "계좌별주문체결내역상세요청"


class TRKeys(object):

    NOSIGNKEY = ["시가", "고가", "저가", "종가", "현재가"]  # +, - 기호 제거할 KEY

    OPT10001 = {
        "싱글데이터": [
            "종목코드",
            "종목명",
            "결산월",
            "액면가",
            "자본금",
            "상장주식",
            "신용비율",
            "연중최고",
            "연중최저",
            "시가총액",
            "시가총액비중",
            "외인소진률",
            "대용가",
            "PER",
            "EPS",
            "ROE",
            "PBR",
            "EV",
            "BPS",
            "매출액",
            "영업이익",
            "당기순이익",
            "250최고",
            "250최저",
            "시가",
            "고가",
            "저가",
            "상한가",
            "하한가",
            "기준가",
            "250최고가일",
            "250최고가대비율",
            "250최저가일",
            "250최저가대비율",
            "현재가",
            "대비기호",
            "전일대비",
            "등락율",
            "거래량",
            "거래대비",
            "액면가단위",
            "유통주식",
            "유통비율"
        ]
    }

    OPT10002 = {
        "멀티데이터": [
            "종목코드",
            "종목명",
            "현재가",
            "등락부호",
            "기준가",
            "전일대비",
            "등락율",
            "매도거래원명1",
            "매도거래원1",
            "매도거래량1",
            "매도거래원명2",
            "매도거래원2",
            "매도거래량2",
            "매도거래원명3",
            "매도거래원3",
            "매도거래량3",
            "매도거래원명4",
            "매도거래원4",
            "매도거래량4",
            "매도거래원명5",
            "매도거래원5",
            "매도거래량5"
        ]
    }

    OPT10003 = {
        "멀티데이터": [
            "시간",
            "현재가",
            "전일대비",
            "대비율",
            "우선매도호가단위",
            "우선매수호가단위",
            "체결거래량",
            "sign",
            "누적거래량",
            "누적거래대금",
            "체결강도"
        ]
    }

    OPT10004 = {
        "멀티데이터": [
            "호가잔량기준시간",
            # 매도호가 관련
            "매도최우선호가",
            "매도2차선호가",
            "매도3차선호가",
            "매도4차선호가",
            "매도5차선호가",
            "매도6차선호가",
            "매도7차선호가",
            "매도8차선호가",
            "매도9차선호가",
            "매도10차선호가",
            "매도최우선잔량",
            "매도2차선잔량",
            "매도3차선잔량",
            "매도4차선잔량",
            "매도5차선잔량",
            "매도6차선잔량",
            "매도7차선잔량",
            "매도8차선잔량",
            "매도9차선잔량",
            "매도10차선잔량",
            "매도1차선잔량대비",
            "매도2차선잔량대비",
            "매도3차선잔량대비",
            "매도4차선잔량대비",
            "매도5차선잔량대비",
            "매도6차선잔량대비",
            "매도7차선잔량대비",
            "매도8차선잔량대비",
            "매도9차선잔량대비",
            "매도10차선잔량대비",
            # 매수호가 관련
            "매수최우선호가",
            "매수2차선호가",
            "매수3차선호가",
            "매수4차선호가",
            "매수5차선호가",
            "매수6차선호가",
            "매수7차선호가",
            "매수8차선호가",
            "매수9차선호가",
            "매수10차선호가",
            "매수최우선잔량",
            "매수2차선잔량",
            "매수3차선잔량",
            "매수4차선잔량",
            "매수5차선잔량",
            "매수6차선잔량",
            "매수7차선잔량",
            "매수8차선잔량",
            "매수9차선잔량",
            "매수10차선잔량",
            "매수1차선잔량대비",
            "매수2차선잔량대비",
            "매수3차선잔량대비",
            "매수4차선잔량대비",
            "매수5차선잔량대비",
            "매수6차선잔량대비",
            "매수7차선잔량대비",
            "매수8차선잔량대비",
            "매수9차선잔량대비",
            "매수10차선잔량대비",
            # 총잔량
            "총매도잔량",
            "총매수잔량",
            "총매도잔량직전대비",
            "총매수잔량직전대비",
            # 시간외
            "시간외매도잔량",
            "시간외매수잔량",
            "시간외매도잔량대비",
            "시간외매수잔량대비",
        ]
    }

    OPT10005 = {
        "멀티데이터": [
            "날짜",
            "시가",
            "고가",
            "저가",
            "종가",
            "대비",
            "등락률",
            "거래량",
            "거래대금",
            "체결강도",
            "외인보유",
            "외인비중",
            "외인순매수",
            "기관순매수",
            "개인순매수",
            "외국계",
            "신용잔고율",
            "프로그램",
        ]
    }

    OPT10006= {
        "멀티데이터":[
            "날짜",
            "시가",
            "고가",
            "저가",
            "종가",
            "대비",
            "등락률",
            "거래량",
            "거래대금",
            "체결강도"
        ]
    }
    OPT10014 = {
        "멀티데이터": [
            "일자",
            "종가",
            "전일대비",
            "등락율",
            "거래량",
            "공매도량",
            "매매비중",
            "공매도거래대금",
            "공매도평균가"
        ]   
    }


    OPT10016 = {
        "멀티데이터": [
            "종목코드",
            "종목명",
            "현재가",
            "전일대비기호",
            "전일대비",
            "등락률",
            "거래량",
            "전일거래량대비율",
            "매도호가",
            "매수호가",
            "고가",
            "저가"
        ]
    }

    OPT10019 = {
        "멀티데이터": [
            "종목코드",
            "종목분류",
            "종목명",
            "전일대비기호",
            "전일대비",
            "등랄률",
            "기준가",
            "현재가",
            "기준대비",
            "거래량",
            "급등률"
        ]
    }

    OPT10023 = {
        "멀티데이터": [
            "종목코드",
            "종목명",
            "현재가",
            "전일대비",
            "전일대비기호",
            "등락률",
            "이전거래량",
            "현재거래량",
            "급증량",
            "급증률"
        ]
    }

    OPT10031 = {
        "멀티데이터": [
            "종목코드",
            "종목명",
            "현재가",
            "전일대비기호",
            "전일대비",
            "거래량"
        ]
    }

    OPT10059 = {
        "멀티데이터": [
            "일자",
            "현재가",
            "대비기호",
            "전일대비",
            "등락율",
            "누적거래량",
            "누적거래대금",
            "개인투자자",
            "기관계",
            "외국인투자자",
            "금융투자",
            "보험",
            "투신",
            "기타금융",
            "은행",
            "연기금등",
            "사모펀드",
            "국가",
            "기타법인",
            "내외국인",
        ]
    }

    OPT10072 = {
        "멀티데이터": [
            "일자", 
            "당일hts매도수수료",
            "종목명", 
            "체결량", 
            "매입단가", 
            "체결가", 
            "당일매도손익", 
            "손익율", 
            "종목코드", 
            "당일매매수수료", 
            "당일매매세금", 
            "인출가능금액",
            "대출일",
            "신용구분",
            "종목코드1",
            "당일매도손익1"
            ],
    }

    OPT10074 = {
        "싱글데이터": ["총매수금액", "총매도금액", "실현손익", "매매수수료", "매매세금"],
        "멀티데이터": ["일자", "매수금액", "매도금액", "당일매도손익", "당일매매수수료", "당일매매세금"],
    }

    OPT10075 = {
        "멀티데이터": [
            "계좌번호",
            "주문번호",
            "관리사번",
            "종목코드",
            "업무구분",
            "주문상태",
            "종목명",
            "주문수량",
            "주문가격",
            "미체결수량",
            "체결누계금액",
            "원구문번호",
            "주문구분",
            "매매구분",
            "시간",
            "체결번호",
            "체결가",
            "체결량",
            "현재가",
            "매도호가",
            "매수호가",
            "단위체결가",
            "단위체결량",
            "당일매매수수료",
            "당일매매세금",
            "개인투자자",
        ]
    }

    OPT20002 = {
        "멀티데이터": [
            "종목코드",
            "종목명",
            "현재가",
            "전일대비기호",
            "전일대비",
            "등락률",
            "현재거래량",
            "매도호가",
            "매수호가",
            "시가",
            "고가",
            "저가"
        ]
    }

    OPT10080 = {
        "멀티데이터": [
            "현재가",
            "거래량",
            "체결시간",
            "시가",
            "고가",
            "저가",
            "수정주가구분",
            "수정비율",
            "대업종구분",
            "소업종구분",
            "종목정보",
            "수정주가이벤트",
            "전일종가",
        ]
    }

    OPTKWFID = {
        "멀티데이터": [
            "종목코드",
            "종목명",
            "현재가",
            "기준가",
            "전일대비",  # 5
            "전일대비기호",
            "등락율",
            "거래량",
            "거래대금",
            "체결량",  # 10
            "체결강도",
            "전일거래량대비",
            "매도호가",
            "매수호가",
            "매도1차호가",  # 15
            "매도2차호가",
            "매도3차호가",
            "매도4차호가",
            "매도5차호가",
            "매수1차호가",  # 20
            "매수2차호가",
            "매수3차호가",
            "매수4차호가",
            "매수5차호가",
            "상한가",  # 25
            "하한가",
            "시가",
            "고가",
            "저가",
            "종가",  # 30
            "체결시간",
            "예상체결가",
            "예상체결량",
            "자본금",
            "액면가",  # 35
            "시가총액",
            "주식수",
            "호가시간",
            "일자",
            "우선매도잔량",  # 40
            "우선매수잔량",
            "우선매도건수",
            "우선매수건수",
            "총매도잔량",
            "총매수잔량",  # 45
            "총매도건수",
            "총매수건수",
            "패리티",
            "기어링",
            "손익분기",  # 50
            "잔본지지",
            "ELW행사가",
            "전환비율",
            "ELW만기일",
            "미결제약정",  # 55
            "미결제전일대비",
            "이론가",
            "내재변동성",
            "델타",
            "감마",  # 60
            "쎄타",
            "베가",
            "로",  # 63
        ]
    }

    OPW00001 = {
        "싱글데이터": [
            "예수금",
            "주식증거금현금",
            "수익증권증거금현금",
            "익일수익증권매도정산대금",
            "해외주식원화대용설정금",
            "신용보증금현금",
            "신용담보금현금",
            "추가담보금현금" "기타증거금",
            "미수확보금",
            "공매도대금",
            "신용설정평가금",
            "수표입금액",
            "기타수표입금액",
            "신용담보재사용",
            "코넥스기본예탁금",
            "ELW예탁평가금",
            "신용대주권리예정금액",
            "생계형가입금액",
            "생계형입금가능금액",
            "대용금평가금액(합계)",
            "잔고대용평가금액",
            "위탁대용잔고평가금액",
            "수익증권대용평가금액",
            "위탁증거금대용",
            "신용보증금대용",
            "신용담보금대용",
            "추가담보금대용",
            "권리대용금",
            "출금가능금액",
            "랩출금가능금액",
            "주문가능금액",
            "수익증권매수가능금액",
            "20%종목주문가능금액",
            "30%종목주문가능금액",
            "40%종목주문가능금액",
            "100%종목주문가능금액",
            "현금미수금",
            "현금미수연체료",
            "신용이자미납",
            "신용이자미납연체료",
            "신용이자미납합계",
            "기타대여금",
            "기타대여금연체료",
            "기타대여금합계",
            "미상환융자금",
            "융자금합계",
            "대주금합계",
            "신용담보비율",
            "중도이용료",
            "최소주문가능금액",
            "대출총평가금액",
            "예탁담보대출잔고",
            "매도담보대출잔고",
            "d+1추정예수금",
            "d+1매도매수정산금",
            "d+1매수정산금",
            "d+1미수변제소요금",
            "d+1매도정산금",
            "d+1출금가능금액",
            "d+2추정예수금",
            "d+2매도매수정산금",
            "d+2미수변제소요금",
            "d+2매도정산금",
            "d+2출금가능금액",
            "출력건수",
        ]
    }

    
    OPW00004 = {
        "싱글데이터": [
            "계좌명",
            "지점명",
            "예수금",
            "D+2추정예수금",
            "유가잔고평가액",
            "예탁자산평가액",
            "총매입금액",
            "추정예탁자산",
            "매도담보대출금",
            "당일투자원금",
            "당월투자원금",
            "누적투자원금",
            "당일투자손익",
            "당월투자손익",
            "누적투자손익",
            "당일손익율",
            "당월손익율",
            "누적손익율",
            "출력건수",
        ],
        "멀티데이터": [
            "종목코드",
            "종목명",
            "보유수량",
            "평균단가",
            "현재가",
            "평가금액",
            "손익금액",
            "손익율",
            "대출일",
            "매입금액",
            "결제잔고",
            "전일매수수량",
            "전일매도수량",
            "금일매수수량",
            "금일매도수량",
        ],
    }

    OPW00007 = {
        "싱글데이터": ["출력건수"],
        "멀티데이터": [
            "주문번호",
            "종목번호",
            "매매구분",
            "신용구분",
            "주문수량",
            "주문단가",
            "확인수량",
            "접수구분",
            "반대여부",
            "주문시간",
            "원주문",
            "종목명",
            "주문구분",
            "대출일",
            "체결수량",
            "체결단가",
            "주문잔량",
            "통신구분",
            "정정취소",
            "확인시간",
        ],
    }

    KOA_NORMAL_KP_CANCEL = {
        "싱글데이터": [
            "time",
            "orderNo",
            "rqName",
            "scrNo",
            "accNo",
            "orderType",
            "code",
            "qty",
            "price",
            "hogaType",
            "originOrderNo",
            "msg"
        ]
    }

    KOA_NORMAL_KP_MODIFY = {
        "싱글데이터": [
            "time",
            "orderNo",
            "rqName",
            "scrNo",
            "accNo",
            "orderType",
            "code",
            "qty",
            "price",
            "hogaType",
            "originOrderNo",
            "msg"
        ]
    }


    KOA_NORMAL_BUY_KP_ORD= {
        "싱글데이터": [
            "orderNo"
        ]
    }
