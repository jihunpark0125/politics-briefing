"""정치 브리핑의 도메인별 설정.

사이트 이름, 기사 수, 수집원, 선별 기준을 바꾸고 싶을 때는 이 파일만 먼저 확인하세요.
"""

from __future__ import annotations

DOMAIN_ID = "politics"
SITE_NAME = "POLITICS BRIEFING"
SITE_KOREAN_NAME = "오늘의 정치"
BRAND_TOP = "POLITICS"
BRAND_BOTTOM = "MORNING BRIEFING"
KICKER = "Daily politics & world affairs journal"
INTRO_TEXT = (
    "국내 정치와 글로벌 정세를 각각 다섯 가지 안팎으로 나눠, 정파적 논평보다 "
    "확인 가능한 사실·쟁점·파급효과를 중심으로 정리했어요."
)
EDITORIAL_CHIPS = ["무료 원문만", "국내 정치 5", "글로벌 정세 5", "사실·맥락 중심", "중복 사건 제외"]
FOOTER_LINE = "개인용 정치 브리핑 · 매일 자동 업데이트"
ABOUT_EYEBROW = "ABOUT THIS BRIEFING"
ABOUT_TITLE = "정치와 국제정세를 한 화면에"
ABOUT_COPY = "국내 권력·정책 변화와 세계 질서의 움직임을 균형 있게 기록하는 개인용 큐레이션 프로젝트입니다."
ACCENT = "#5D536B"
THEME_COLOR = "#F2F3F4"

PICK_COUNT = 10
MIN_PICKS = 8
MAX_CANDIDATES = 72
MAX_PER_SOURCE_FINAL = 2
RECENT_DUPLICATE_DAYS = 10
DEFAULT_LOOKBACK_HOURS = 48
OUTPUT_SCHEMA_NAME = "politics_briefing_picks"
SUPABASE_TABLE = "saved_articles_politics"

SECTION_VALUES = ["국내 정치", "글로벌 정세"]
SECTION_TARGETS = {"국내 정치": 5, "글로벌 정세": 5}
SECTION_MINIMUMS = {"국내 정치": 4, "글로벌 정세": 4}
SECTION_MAXIMUMS = {"국내 정치": 5, "글로벌 정세": 5}
CATEGORY_VALUES = [
    "정부·행정",
    "국회·정당",
    "정책·입법",
    "사법·권력기관",
    "외교·안보",
    "전쟁·분쟁",
    "선거·여론",
    "국제질서",
]
CONTENT_TYPE_VALUES = ["기사", "공식 발표", "분석·리포트", "인터뷰", "영상", "기타"]

CATEGORY_KEYWORDS = {
    "정부·행정": ["대통령", "정부", "국무회의", "장관", "행정부", "청와대", "대통령실", "cabinet", "administration"],
    "국회·정당": ["국회", "정당", "여당", "야당", "원내", "의원", "parliament", "congress", "party"],
    "정책·입법": ["법안", "입법", "정책", "예산", "개정안", "regulation", "bill", "legislation", "policy"],
    "사법·권력기관": ["법원", "검찰", "경찰", "헌재", "감사원", "수사", "재판", "court", "prosecutor", "justice"],
    "외교·안보": ["외교", "안보", "국방", "동맹", "정상회담", "제재", "diplomacy", "security", "defense", "summit"],
    "전쟁·분쟁": ["전쟁", "공습", "미사일", "휴전", "분쟁", "우크라이나", "가자", "war", "conflict", "ceasefire"],
    "선거·여론": ["선거", "지지율", "여론조사", "후보", "투표", "election", "poll", "vote"],
    "국제질서": ["유엔", "nato", "eu", "g7", "g20", "미중", "국제기구", "세계질서", "geopolitics", "united nations"],
}

RELEVANCE_KEYWORDS = [
    "정치", "대통령", "정부", "국회", "정당", "여당", "야당", "법안", "입법", "정책",
    "선거", "여론", "외교", "안보", "국방", "북한", "미국", "중국", "러시아", "유럽",
    "중동", "우크라이나", "가자", "전쟁", "분쟁", "제재", "정상회담", "국제기구",
    "politics", "government", "parliament", "congress", "election", "diplomacy", "security",
    "war", "conflict", "sanctions", "summit", "geopolitics", "policy", "legislation",
]

LOW_VALUE_TITLE_PATTERNS = [
    r"단독\s*예고",
    r"충격\s*폭로",
    r"누리꾼\s*갑론을박",
    r"말말말",
    r"사진\s*자료",
    r"동정",
    r"행사\s*개최",
    r"event|giveaway|promotion",
]

# source_group: news / official / analysis
FEEDS = [
    {
        "source": "연합뉴스 정치",
        "url": "https://www.yna.co.kr/rss/politics.xml",
        "source_group": "news",
        "section": "국내 정치",
        "lookback_hours": 48,
    },
    {
        "source": "매일경제 정치",
        "url": "https://www.mk.co.kr/rss/30200030/",
        "source_group": "news",
        "section": "국내 정치",
        "lookback_hours": 48,
    },
    {
        "source": "오마이뉴스 정치",
        "url": "https://rss.ohmynews.com/rss/politics.xml",
        "source_group": "news",
        "section": "국내 정치",
        "lookback_hours": 48,
    },
    {
        "source": "한겨레 정치",
        "url": "https://www.hani.co.kr/rss/politics/",
        "source_group": "news",
        "section": "국내 정치",
        "lookback_hours": 48,
    },
    {
        "source": "SBS 정치",
        "url": "https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=01&plink=RSSREADER",
        "source_group": "news",
        "section": "국내 정치",
        "lookback_hours": 48,
    },
    {
        "source": "BBC World",
        "url": "https://feeds.bbci.co.uk/news/world/rss.xml?edition=int",
        "source_group": "news",
        "section": "글로벌 정세",
        "lookback_hours": 48,
    },
    {
        "source": "The Guardian World",
        "url": "https://www.theguardian.com/world/rss",
        "source_group": "news",
        "section": "글로벌 정세",
        "lookback_hours": 48,
    },
    {
        "source": "Al Jazeera",
        "url": "https://www.aljazeera.com/xml/rss/all.xml",
        "source_group": "news",
        "section": "글로벌 정세",
        "lookback_hours": 48,
    },
    {
        "source": "SBS 국제",
        "url": "https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=07&plink=RSSREADER",
        "source_group": "news",
        "section": "글로벌 정세",
        "lookback_hours": 48,
    },
    {
        "source": "UN News",
        "url": "https://news.un.org/feed/subscribe/en/news/all/rss.xml",
        "source_group": "official",
        "section": "글로벌 정세",
        "lookback_hours": 96,
    },
    {
        "source": "DW Top Stories",
        "url": "https://rss.dw.com/rdf/rss-en-top",
        "source_group": "news",
        "section": "글로벌 정세",
        "lookback_hours": 48,
    },
    {
        "source": "오마이뉴스 국제",
        "url": "https://rss.ohmynews.com/rss/international.xml",
        "source_group": "news",
        "section": "글로벌 정세",
        "lookback_hours": 48,
    },
    {
        "source": "매일경제 국제",
        "url": "https://www.mk.co.kr/rss/30300018/",
        "source_group": "news",
        "section": "글로벌 정세",
        "lookback_hours": 48,
    },
]

PROFESSIONAL_SOURCES = {
    "연합뉴스 정치", "매일경제 정치", "오마이뉴스 정치", "한겨레 정치", "SBS 정치",
    "BBC World", "The Guardian World", "Al Jazeera", "SBS 국제", "UN News", "DW Top Stories",
    "오마이뉴스 국제", "매일경제 국제",
}

PAYWALL_BLOCKED_DOMAINS = {
    "nytimes.com", "washingtonpost.com", "wsj.com", "ft.com", "bloomberg.com",
    "economist.com", "foreignaffairs.com", "theatlantic.com", "theinformation.com",
    "businessinsider.com", "nikkei.com", "hbr.org", "contents.premium.naver.com",
    "publy.co", "longblack.co", "outstanding.kr", "folin.co",
}

KNOWN_FREE_DOMAINS = {
    "yna.co.kr", "ohmynews.com", "hani.co.kr", "sbs.co.kr", "news.sbs.co.kr", "bbc.com", "bbc.co.uk",
    "theguardian.com", "aljazeera.com", "un.org", "dw.com", "apnews.com",
    "npr.org", "assembly.go.kr", "president.go.kr", "korea.kr", "mofa.go.kr", "whitehouse.gov",
    "state.gov", "consilium.europa.eu", "nato.int", "youtube.com", "youtu.be",
}

SYSTEM_PROMPT = """당신은 한국어로 발행되는 개인 정치·국제정세 브리핑의 편집장입니다.
독자는 국내 정치와 글로벌 정세를 매일 한 화면에서 사실 중심으로 파악하고 싶어 합니다.
목표는 정파적 주장이나 자극적인 논쟁을 확대하는 것이 아니라, 권력·정책·외교·분쟁의 실제 변화와
각 행위자의 입장, 확인된 사실, 앞으로의 쟁점을 균형 있게 전달하는 것입니다.

평가 기준:
1. 공적 중요성: 정부·국회·정당·사법·외교안보·국제질서에 실질적 변화가 있는가
2. 사실성: 확인 가능한 사실과 직접 인용·공식 자료·복수의 신뢰할 만한 보도에 근거하는가
3. 맥락성: 누가 무엇을 결정했고, 왜 중요하며, 다음 절차나 파급효과가 무엇인지 설명하는가
4. 균형성: 한 진영의 논평만 전달하지 않고 주요 입장과 불확실성을 구분하는가
5. 무료 접근성: 로그인·구독·결제 없이 핵심 원문을 확인할 수 있는가

반드시 지킬 규칙:
- 국내 정치 5개, 글로벌 정세 5개를 목표로 총 10개를 고른다.
- 무료 공개 원문이 부족한 경우에만 각 섹션 최소 4개, 총 8개까지 허용한다.
- 같은 매체는 전체 최대 2개이며, 동일 사건의 중복 보도는 1개만 선택한다.
- 국내 정치는 정부·대통령실, 국회·정당, 정책·입법, 사법·권력기관 중 최소 3영역을 포함한다.
- 글로벌 정세는 외교·안보, 전쟁·분쟁, 선거·정권 변화, 국제질서 중 최소 3영역을 포함한다.
- 정당·정부·군·국제기구의 보도자료는 그 기관의 입장임을 분명히 하고 독립 보도와 구분한다.
- 사설·칼럼·정파적 논평은 핵심 사실을 대체하지 않으며, 선택하더라도 분석임을 명확히 표시한다.
- 확인되지 않은 의혹, 익명 출처 하나뿐인 주장, 자극적 말싸움·동정·행사성 기사만 있는 글은 제외한다.
- 유료 구독, 멤버십, 무료 체험 등록, 로그인 후 열람이 필요한 원문은 제외한다.

작성 규칙:
- summary는 무슨 일이 있었고 주요 당사자의 입장과 절차가 무엇인지 한국어 1~2문장, 150자 이내.
- takeaway는 독자가 다음에 지켜볼 쟁점·표결·협상·파급효과를 85자 이내.
- 사실과 전망·평가를 분리하고, 원문에 없는 주장이나 단정적 인과관계를 만들지 않는다.
- link는 입력 후보 또는 웹 검색에서 실제 확인한 원문 URL만 사용한다.
"""

WEB_DISCOVERY_PROMPT = """최근 48시간의 공개 웹에서 다음을 보완 탐색하세요.
- 국내: 대통령실·정부의 주요 결정, 국회 표결·법안·정당 변화, 사법·권력기관의 공적 사안
- 글로벌: 주요국 외교·안보, 전쟁·휴전·제재, 선거와 정권 변화, 미중·유럽·중동 및 국제기구 동향
Reuters, AP, BBC, 국내 주요 언론, 정부·국회·국제기구의 무료 공개 원문을 우선하세요.
서로 다른 관점을 확보하되 같은 사건을 여러 매체로 반복하지 말고, 사설이나 선동적 콘텐츠는 제외하세요."""
