# ✈️ Airplane Tracker (PostgreSQL + OpenSky API)

Проект для сбора, хранения и анализа данных о самолётах в реальном времени с использованием публичных API и PostgreSQL.

---

## 📌 Описание

Приложение получает данные о самолётах через API:

- OpenSky Network API (данные о самолётах)
- Nominatim OpenStreetMap API (геолокация стран)

Далее данные сохраняются в PostgreSQL и обрабатываются через класс `DBManager`.

---
## 🚀 Запуск проекта

### ⚙️ Установка
- git clone <https://github.com/vadimsemenov53-crypto/PostgreSQL_Jobs_Widget>
- poetry install
- Для работы с базой данных необходимо создать файл .envс параметрами доступа к базе данных PostgresSQL. Пример сравнения файла:
```
POSTGRES_HOST=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_PORT=5432
```


### ▶️ Запуск
```bash
python3 main.py
```
---

## 🌍 Функционал

Программа работает с 10 странами:

- France
- Germany
- Italy
- Spain
- Sweden
- Poland
- Greece
- Portugal
- Netherlands
- Austria

---

## ⚙️ Возможности

### 📊 Аналитика через DBManager:

- `get_info_countries_and_planes()` — количество самолётов по странам
- `get_all_planes()` — список всех самолётов с характеристиками
- `get_avg_height()` — средняя высота полёта
- `get_max_height()` — самолёты выше средней высоты
- `get_planes_by_countries()` — фильтрация по странам

---

## 🏗 Архитектура проекта

Проект разделён на слои:

- `API layer` — получение данных (requests)
- `Repository layer` — работа с PostgreSQL (psycopg2)
- `DBManager` — аналитика данных
- `Interface` — CLI взаимодействие с пользователем

---

## 🗄 База данных

Используется PostgreSQL.

### Таблицы:

#### airplanes
- icao24 (PK)
- callsign
- origin_country
- time_position
- last_contact
- longitude / latitude
- baro_altitude
- on_ground
- velocity
- true_track
- vertical_rate
- geo_altitude
- squawk
- spi
- position_source
- created_at

#### country
- place_id (PK)
- osm_type
- osm_id
- lat
- lon
- class
- type
- place_rank
- importance
- addresstype
- name
- display_name

---
### ⏱ Особенности

- API-запросы выполняются с задержкой (2 сек) для избежания rate limit
- Данные обновляются в реальном времени
- Используется типизация (mypy)

---

### 🧠 Используемые технологии
- Python 3.14+
- PostgreSQL
- psycopg2
- requests
- OpenSky API
- OpenStreetMap API
- mypy (static typing)

---

#### 📎 Автор
Учебный проект: Airplane Tracker (PostgreSQL + OpenSky API)
Разработал: Vadim Semenov

