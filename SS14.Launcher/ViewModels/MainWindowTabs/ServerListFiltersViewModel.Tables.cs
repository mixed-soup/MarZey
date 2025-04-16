using System.Collections.Generic;
using static SS14.Launcher.Api.ServerApi;

namespace SS14.Launcher.ViewModels.MainWindowTabs;

public sealed partial class ServerListFiltersViewModel
{
    private static readonly Dictionary<string, string> RegionNamesEnglish = new()
    {
        // @formatter:off
        { Tags.RegionAfricaCentral,       "Центральная Африка"      },
        { Tags.RegionAfricaNorth,         "Северная Африка"         },
        { Tags.RegionAfricaSouth,         "Южная Африка"            },
        { Tags.RegionAntarctica,          "Антарктида"              },
        { Tags.RegionAsiaEast,            "Восточная Азия"          },
        { Tags.RegionAsiaNorth,           "Северная Азия"           },
        { Tags.RegionAsiaSouthEast,       "Юго-Восточная Азия"      },
        { Tags.RegionCentralAmerica,      "Центральная Америка"     },
        { Tags.RegionEuropeEast,          "Восточная Европа"        },
        { Tags.RegionEuropeWest,          "Западная Европа"         },
        { Tags.RegionGreenland,           "Гренландия"              },
        { Tags.RegionIndia,               "Индия"                   },
        { Tags.RegionMiddleEast,          "Ближний Восток"          },
        { Tags.RegionMoon,                "Луна"                    },
        { Tags.RegionNorthAmericaCentral, "Центральная Северная Америка" },
        { Tags.RegionNorthAmericaEast,    "Восточная Северная Америка"   },
        { Tags.RegionNorthAmericaWest,    "Западная Северная Америка"    },
        { Tags.RegionOceania,             "Океания"                 },
        { Tags.RegionSouthAmericaEast,    "Восточная Южная Америка" },
        { Tags.RegionSouthAmericaSouth,   "Южная Южная Америка"     },
        { Tags.RegionSouthAmericaWest,    "Западная Южная Америка"  },
        // @formatter:on
    };

    private static readonly Dictionary<string, string> RegionNamesShortEnglish = new()
    {
        // @formatter:off
        { Tags.RegionAfricaCentral,       "Центр. Африка"  },
        { Tags.RegionAfricaNorth,         "Сев. Африка"    },
        { Tags.RegionAfricaSouth,         "Южн. Африка"    },
        { Tags.RegionAntarctica,          "Антарктида"     },
        { Tags.RegionAsiaEast,            "Вост. Азия"     },
        { Tags.RegionAsiaNorth,           "Сев. Азия"      },
        { Tags.RegionAsiaSouthEast,       "Ю-В Азия"       },
        { Tags.RegionCentralAmerica,      "Центр. Америка" },
        { Tags.RegionEuropeEast,          "Вост. Европа"   },
        { Tags.RegionEuropeWest,          "Зап. Европа"    },
        { Tags.RegionGreenland,           "Гренландия"     },
        { Tags.RegionIndia,               "Индия"          },
        { Tags.RegionMiddleEast,          "Бл. Восток"     },
        { Tags.RegionMoon,                "Луна"           },
        { Tags.RegionNorthAmericaCentral, "СА Центр"       },
        { Tags.RegionNorthAmericaEast,    "СА Восток"      },
        { Tags.RegionNorthAmericaWest,    "СА Запад"       },
        { Tags.RegionOceania,             "Океания"        },
        { Tags.RegionSouthAmericaEast,    "ЮА Восток"      },
        { Tags.RegionSouthAmericaSouth,   "ЮА Юг"          },
        { Tags.RegionSouthAmericaWest,    "ЮА Запад"       },
        // @formatter:on
    };

    private static readonly Dictionary<string, string> RolePlayNames = new()
    {
        // @formatter:off
        { Tags.RolePlayNone,   "Нет"       },
        { Tags.RolePlayLow,    "Низкий"    },
        { Tags.RolePlayMedium, "Средний"   },
        { Tags.RolePlayHigh,   "Высокий"   },
        // @formatter:on
    };

    private static readonly Dictionary<string, int> RolePlaySortOrder = new()
    {
        // @formatter:off
        { Tags.RolePlayNone,   0 },
        { Tags.RolePlayLow,    1 },
        { Tags.RolePlayMedium, 2 },
        { Tags.RolePlayHigh,   3 },
        // @formatter:on
    };
}
