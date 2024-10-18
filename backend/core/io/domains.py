from enum import Enum, auto


class categories(Enum):
    Commercial = auto()
    Education = auto()
    GovernmentAndNonProfit = auto()
    Technology = auto()
    Entertainment = auto()
    Adult = auto()
    LifeStyle = auto()
    Travel = auto()
    Health = auto()
    Food = auto()
    RealEstate = auto()


c_domains = {
    categories.Commercial: [
        ".com",
        ".biz",
        ".trade",
        ".store",
        ".market",
        ".bargains",
        ".business",
        ".bank",
        ".loan",
        ".accountant",
        ".accountants",
        ".agency",
        ".coop",
        ".inc",
        ".pro",
        ".ventures",
        ".rich"
    ],
    categories.Education: [
        ".edu",
        ".college",
        ".cancerresearch",
        ".shiksha",
        ".academy",
        ".research institutes"
    ],
    categories.GovernmentAndNonProfit: [
        ".gov",
        ".org",
        ".ong",
        ".mil",
        ".int",
        ".gop"
    ],
    categories.Technology: [
        ".net",
        ".tech",
        ".dev",
        ".cloud",
        ".codes",
        ".support",
        ".engineering",
        ".computer",
        ".network"
    ],
    categories.Entertainment: [
        ".art",
        ".music",
        ".dance",
        ".video",
        ".game",
        ".hiphop",
        ".lol",
    ],
    categories.Adult: [
        ".adult",
        ".xxx"
    ],
    categories.LifeStyle: [
        ".life",
        ".club",
        ".community",
        ".dating",
        ".meet",
        ".party",
        ".lgbt",
        ".mom"
    ],
    categories.Travel: [
        ".travel",
        ".aero",
        ".city",
        ".country",
        ".region",
        ".world",
        ".lat",
        ".africa",
        ".asia"
    ],
    categories.Health: [
        ".health",
        ".med",
        ".pharmacy",
        ".life",
        ".wellness",
        ".hiv"
    ],
    categories.Food: [
        ".coffee",
        ".restaurant",
        ".pizza",
        ".food",
        ".cooking",
        ".diet"
    ],
    categories.RealEstate: [
        ".property",
        ".house",
        ".land"
    ]

}