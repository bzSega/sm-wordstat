# sm-wordstat

Yandex Wordstat API — статистика поисковых запросов: топ, динамика, регионы. Без браузера и капчи.

## Возможности

- **Топ запросов** — список поисковых фраз с частотами показов
- **Динамика** — изменения частоты запроса по месяцам
- **Регионы** — распределение показов по регионам России

## Установка

Навык для AI-ассистентов (Jeeves, OpenClaw, Claude Code). Скрипт работает standalone — нужен только Python 3.10+ и ключ Yandex Cloud.

## Настройка

1. Получите API-ключ в Yandex Cloud (сервис Search API)
2. Установите переменные окружения: `WORDSTAT_API_KEY` и `WORDSTAT_FOLDER_ID`
3. Запустите: `python skills/sm-wordstat/scripts/wordstat.py top "песня на 1 сентября"`

## Структура

```
skills/sm-wordstat/
├── SKILL.md              # Инструкция для AI-ассистента
└── scripts/
    └── wordstat.py       # Готовый Python-скрипт
```

## Лицензия

MIT
