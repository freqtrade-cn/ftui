strategies_config = {
    "HourBasedStrategy":{
        "name": "HourBasedStrategy",
        "description": "HourBasedStrategy is a strategy that uses the hour based indicator to trade the market.",
        "author": "Robert Roman",
        "timeframe": "1h",
        "roi": {
            "0": 0.528,
            "169": 0.113,
            "528": 0.089,
            "1837": 0
        },
        "stoploss": -0.10,
        "port":8081
    },
    "Bandtastic":{
        "name": "Bandtastic",
        "description": "Bandtastic is a strategy that uses the bandtastic indicator to trade the market.",
        "author": "Robert Roman",
        "timeframe": "15m",
        "roi": {
            "0": 0.162,
            "69": 0.097,
            "229": 0.061,
            "566": 0
        },
        "stoploss": -0.345,
        "port":8082
    },
    "BreakEven":{
        "name": "BreakEven",
        "description": "BreakEven is a strategy that uses the break even indicator to trade the market.",
        "author": "lenik",
        "timeframe": "5m",
        "roi": {
            "0": 0.01,
            "10": 0
        },
        "stoploss": -0.05,
        "port":8083
    },
    "CustomStoplossWithPSAR":{
        "name": "CustomStoplossWithPSAR",
        "description": "CustomStoplossWithPSAR is a strategy that uses the custom stoploss with psar indicator to trade the market.",
        "author": "lenik",
        "timeframe": "1h",
        "port":8084
    },
    "Diamond":{
        "name":"Diamond",
        "description": "CustomStoplossWithPSAR is a strategy that uses the custom stoploss with psar indicator to trade the market.",
        "author": "Mablue",
        "roi" :{
            "0": 0.242,
            "13": 0.044,
            "51": 0.02,
            "170": 0
        },
        "stoploss" :-0.271,
        "timeframe": "5m",
        "port":8085
    },
    "FixedRiskRewardLoss":{
        "name": "FixedRiskRewardLoss",
        "description": "FixedRiskRewardLoss is a strategy that uses the fixed risk reward loss indicator to trade the market.",
        "author": "lenik",
        "timeframe": "1h",
        "stoploss":-0.9,
        "port":8086
    },
    "GodStra":{
        "name": "GodStra",
        "description": "GodStra is a strategy that uses the godstra indicator to trade the market.",
        "author": "Mablue",
        "roi" :{
            "0": 0.3556,
            "4818": 0.21275,
            "6395": 0.09024,
            "22372": 0
        },
        "stoploss":-0.34549,
        "timeframe": "12h",
        "port":8087
    },
    "Heracles":{
        "name": "Heracles",
        "description": "Heracles is a strategy that uses the heracles indicator to trade the market.",
        "author": "Mablue",
        "timeframe": "4h",
        "roi":{
            "0": 0.598,
            "644": 0.166,
            "3269": 0.115,
            "7289": 0
        },
        "stoploss":-0.256,
        "port":8088
    },
    "hlhb":{
        "name": "hlhb",
        "description": "hlhb is a strategy that uses the hlhb indicator to trade the market.",
        "author": "Mablue",
        "timeframe": "4h",
        "roi":{
            "0": 0.6225,
            "703": 0.2187,
            "2849": 0.0363,
            "5520": 0
        },
        "stoploss":-0.3211,
        "port":8089
    },
    "mabStra":{
        "name":"mabStra",
        "description":"",
        "author":"",
        "timeframe":"4h",
        "roi":{
            "0": 0.598,
            "644": 0.166,
            "3269": 0.115,
            "7289": 0
        },
        "stoploss":-0.128,
        "port":8090
    },
    "multi_tf":{
        "name":"multi_tf",
        "description":"",
        "author":"",
        "timeframe":"5m",
        "roi":{
            "0": 0.2
        },
        "stoploss":-0.1,
        "port":8091
    },
    "MultiMa":{
        "name":"MultiMa",
        "description":"",
        "author":"",
        "timeframe":"4h",
        "roi":{
            "0": 0.523,
            "1553": 0.123,
            "2332": 0.076,
            "3169": 0
        },
        "stoploss":-0.345,
        "port":8092
    },
    "PatternRecognition":{
        "name":"PatternRecognition",
        "description":"",
        "author":"",
        "timeframe":"1d",
        "roi":{
            "0": 0.936,
            "5271": 0.332,
            "18147": 0.086,
            "48152": 0
        },
        "port":8093
    },
    "PowerTower":{
        "name":"PowerTower",
        "description":"",
        "author":"",
        "timeframe":"5m",
        "roi":{
            "0": 0.213,
            "39": 0.048,
            "56": 0.029,
            "159": 0
        },
        "stoploss":-0.288,
        "port":8094
    },
    "Supertrend":{
        "name":"Supertrend",
        "description":"",
        "author":"",
        "timeframe":"5m",
        "roi":{
            "0": 0.213,
            "372": 0.058,
            "861": 0.029,
            "2221": 0
        },
        "stoploss":-0.265,
        "port":8095
    },
    "SwingHighToSky":{
        "name":"SwingHighToSky",
        "description":"",
        "author":"",
        "timeframe":"15m",
        "roi":{
            "0": 0.27058,
            "33": 0.0853,
            "64": 0.04093,
            "244": 0
        },
        "stoploss":-0.34338,
        "port":8096
    },
    "UniversalMACD":{
        "name":"UniversalMACD",
        "description":"",
        "author":"",
        "timeframe":"5m",
        "roi":{
            "0": 0.213,
            "27": 0.099,
            "60": 0.03,
            "164": 0
        },
        "stoploss":-0.265,
        "port":8097
    }
}

for strategy in strategies_config:
    print(strategy)
    print(strategies_config[strategy])
    print("--------------------------------")

    # 生成 server 配置
    with open('config.yaml', 'w') as f:
        f.write('---\nservers:\n\n')
        for strategy in strategies_config:
            f.write(f'    - name        : "{strategies_config[strategy]["name"]}{strategies_config[strategy]["port"]}"\n')
            f.write('      username    : "freqtrader"\n')
            f.write('      password    : "123456"\n') 
            f.write('      ip          : 127.0.0.1\n')
            f.write(f'      port        : {strategies_config[strategy]["port"]}\n\n')
        
        f.write('debug: False\n\n')
        f.write('# only uncomment these options if you are receiving urllib warnings about connection pool full\n')
        f.write('# pool_connections: 30\n')
        f.write('# pool_maxsize: 20\n')
