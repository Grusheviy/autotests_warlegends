# ACTION
<details>
  <summary>Изменения сообщения в чате саппорта</summary>
Редактирование сообщения саппорта в чате поддержки

**Назначение команды:**  редактирование сообщения саппорта в чате поддержки
Пример команды:
```
/fort develop ACTION {"type":"editMessageFromSupport","receiverId":123123,"messageId":130260,"newText":"War Legends.","agentId":1,"agentLogin":"@smazurenko","messageIds":[1,2,3],"templateId":0,"themeId":0,"duration":107,"editCount":0}
```

* `receiverId` - id аккаунта получателя
* `messageId` - сообщение, которое будет отредактировано
* `newText` - текст отредактированного сообщения
* `agentId`- id саппорта
* `agentLogin` - логин саппорта
* `messageIds`  - массив айдишников на которые будет ответ
* `templateId`  - id темплейта сообщения от саппорта
* `themeId`  - id темы саппорта
* `duration`  - скорость ответа саппорта в секундах
* `editCount`  - кол-во исправлений данного сообщения саппортом

**Примечание:** поля receiverId, messageId и newText обязательные, а остальные опциональные

**Результатом** выполнения запроса будет изменено сообщение от саппорта в чате саппорта
   
</details>
<details>
         <summary>Удаление сообщения в чате саппорта</summary>

**Назначение команды:**  удаление сообщения от саппорта в чате поддержки

Пример команды:
```
/fort develop ACTION {"type":"removeMessageFromSupport","messageId":130260,"receiverId":123123}
```

* `receiverId` - id аккаунта получателя
* `messageId` - id сообщения, которое нужно удалить
  **Примечание:** все поля должны быть заполнены

**Результатом** выполнения запроса будет удаление сообщения от саппорта в чате саппорта

</details>
<details>
         <summary>Отправка сообщения от саппорта</summary>

**Назначение команды:**  ответ саппорта в чате поддержки

Пример команды:
```
/fort develop ACTION {"type":"sendMessageFromSupport","receiverId":130260,"message":"War Legends.","role":"PLAYER","playerIpHost":"192.186.20.21:1233","playerName":"Wasya","agentId":1,"agentLogin":"@smazurenko","messageIds":[1,2,3],"templateId":0,"themeId":0,"duration":107,"editCount":0}
```

* `receiverId` - id аккаунта получателя
* `role` - роль получателя
* `playerIpHost` - ip получателя
* `playerName` - никнейм получателя
* `message` - сообщение, которое будет отправлено игроку
* `agentId` - id саппорта
* `agentLogin` - логин саппорта
* `messageIds`  - массив айдишников на которые будет ответ
* `templateId`  - id темплейта сообщения от саппорта
* `themeId`  - id темы саппорта
* `duration`  - скорость ответа саппорта в секундах
* `editCount`  - кол-во исправлений данного сообщения саппортом
  **Примечание:** поля receiverId и message обязательные, а остальные опциональные

**Результатом** выполнения запроса будет отправлено сообщение игроку в чат саппорта

   </details>
<details>
   <summary>Изменение шкал ежедневных наград</summary>
      <details>
         <summary>Позволяет перейти на следующий день по шкале</summary>
      
Пример команды:
```
/fort develop ACTION {"type":"skipOneDayOfEntrance", "accountId": 1 , "entranceEnum": "ENTRANCE_30"}
```

* `accountId` - id аккаунта, который нужно перенести день в шкале на следующий.
* `entranceEnum` - Тип шкалы. (ENTRANCE_7, ENTRANCE_14, ENTRANCE_30)

**Примечание:** Все поля должны быть указаны. Для ENTRANCE_7 и ENTRANCE_14 должна быть забрана текущая награда, чтобы
перейти на следующий день.
   </details>
      <details>
<summary>Позволяет полностью обновить шкалу</summary>

Пример команды:
```
/fort develop ACTION {"type":"updateEntrance", "accountId": 1 , "entranceEnum": "ENTRANCE_30"}
```

* `accountId` - id аккаунта, которому нужно обновить шкалу.
* `entranceEnum` - Тип шкалы. (ENTRANCE_7, ENTRANCE_14, ENTRANCE_30)
  **Примечание:** Все поля должны быть указаны.
</details>
</details>
<details>
         <summary>Получение ID аккаунта</summary>
   <details>
      <summary>Позволяет получить ID аккаунта игрока по его имени или сессии.</summary>

Пример команды:

* Получение ID аккаунта игрока по его имени:
```
/fort develop ACTION {"type":"getProfileIdByName","name":"test"}
```

Вместо `develop` можно поставить `alpha, beta, feature`.

**Примечание:** Имя аккаунта игрока в игре указано слева сверху рядом с аватаркой.

**Результатом** выполнения запроса будет требуемый ID аккаунта игрока.

* Получение ID аккаунта игрока по его сессии:
```
/fort develop ACTION {"type":"getProfileIdBySession","sessionID":"a1b2c3d4e5f6"}
```

Вместо `develop` можно поставить `alpha, beta, feature`.
Примечание: `sessionID` можно узнать
[выполнив шаги 1-7 из Способа №3](https://yt.gearwap.ru/articles/FORT-A-936/Poluchenie-ID-boya-igroka#%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1-%E2%84%963)

**Результатом** выполнения запроса будет требуемый ID аккаунта игрока.
   </details>
</details>
<details>
         <summary>Смена типа аккаунта</summary>

**Назначение команд:** Позволяет изменить роль у аккаунта

Пример команды:
<details>
<summary>Изменить роль на PLAYER (Сделать аккаунт "нетестерским", т.е. обычным лишенным дебажных кнопок)</summary>

```
/fort develop ACTION {"type":"setRole","accountID": 1,"typeRole": "PLAYER"}
```

`typeRole` - тип роли;

**Результатом** выполнения запроса будет изменение роли аккаунта на PLAYER
</details>
<details>
<summary>Изменить роль на QA (добавляет наличие дебажных кнопок)</summary>

```
/fort develop ACTION {"type":"setRole","accountID": 1,"typeRole": "QA"}
```

**Результатом** выполнения запроса будет изменение роли аккаунта на QA

Текущие роли описаны [тут](https://yt.gearwap.ru/articles/FORT-A-924/Roli-akkauntov)
</details>
</details>
<details>
         <summary>Бан аккаунта</summary>

**Назначение команды:** Позволяет забанить игрока. Если игрок постарается войти, ему будет создан новый аккаунт.

Пример команды:

```
/fort develop ACTION {"type":"banAccount","accountID": 1000302}
```

Вместо `develop` можно поставить `balance, mr, mr2, mr3`.

**Результатом** выполнения запроса будет получение бана аккаунтом. При следующем входе будет получено сообщение
о бане аккаунта, и будет создан новый.
</details>
<details>
         <summary>Генерация профилей ботов</summary>

**Назначение команды:** Позволяет создать n-ное количество профилей ботов.

Пример команды:

```
/fort develop ACTION {"type":"createBotProfiles","amount": 1, "league": 1, "botType": "BOT_PVP_RANDOM"}
```

* `amount` - количество ботов;
* `botType` - тип бота, может быть BOT_PVP_RANDOM или BOT_PVP_NOT_RANDOM
* `league` - лига бота, может быть от 1 до 7, по которой генерируются случайный визуальный рейтинг в диапазоне этой лиги
  Вместо `develop` можно поставить `alpha, beta, feature`.

**Результатом** выполнения запроса будет создание в бд профилей ботов с рандомным ником, аваторкой и статистикой боев
   </details>
<details>
         <summary>Бан аккаунта в общем чате</summary>

**Назначение команды:** Позволяет забанить игрока в общем чате.

Команда в [GitLab](https://gitlab.gearwap.ru/fort/server/-/tree/develop)

Пример команды:
```
/fort develop ACTION {"type":"banUserInChat", "accountId": 1 , "expirationTime": "1", "timeUnit": "HOURS", "reasons": "1,2,3"}
```

* `accountId` - id аккаунта, который нужно забанить в чате.
* `expirationTime` - время, на которое будет забанен пользователь. Максимальный срок бана - 365 дней, если прописать срок
  больше, то он автоматически сократиться до максимального. Если прописать MAX, то пользователь будет забанен на 365 дней,
  независимо от того, какой указан timeUnit. Может принимать следующие значения: Число (в кавычках), "MAX".
* `reasons` - причины(а), по которым будет забанен игрок.

[Список причин](https://gitlab.gearwap.ru/fort/server/-/blob/develop/player/src/main/java/com/geargames/fort/model/profile/enums/ChatBanReason.java):

AGGRESSION_OR_SWEARING(1) — Агрессия или нецензурная брань

TROLLING(2) — Троллинг (любая провокация, в том числе политика, религия)

FLOODING(3) — Флуд (просто бессмысленный спам)

RACISM_OR_SEXISM(4) — Расизм, сексизм (именно как hate speech)

ADVERTING(5) — Реклама (других игр, сайтов)

ACCOUNT_SELLING(6) — Продажа аккаунта (всё что расцениваем как призыв)

SABOTAGING(7) — Саботаж (удалить игру, не играть, не донатить)

* `timeUnit` - единица измерения времени. Варианты: NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS;

**Примечание:** Все поля должны быть указаны.

**Результатом** выполнения запроса будет добавлено в профиле новое ChatInfo с причиной и сроком бана, пользователь будет забанен в чате.

**Примеры использования команды:**
* ```
  /fort develop ACTION {"type":"banUserInChat", "accountId": 1 , "expirationTime": "10", "timeUnit": "HOURS", "reasons": "1,2,3"}
  ```
**В результате выполнения** пользователь будет забанен в чате на 10 часов за то, что он агрессивно себя вёл, троллил, флудил.
* ```
  /fort develop ACTION {"type":"banUserInChat", "accountId": 1 , "expirationTime": "MAX", "timeUnit": "SECONDS", "reasons": "5"}
  ```
**В результате выполнения** команды пользователь будет забанен в чате на 365 дней за рекламу.

   </details>
<details>
         <summary>Получение информации о бане в общем чате</summary>

**Назначение команды:** Позволяет получить информацию о последних 10 банах пользователя в чате

Команда в [GitLab](https://gitlab.gearwap.ru/fort/server/-/tree/develop)

```
/fort develop ACTION {"type":"checkUserBanInfoInChat", "accountId": 1}
```

* `accountId` - id аккаунта того, чью информацию о банах хотим получить.

**Результатом** выполнения запроса будет получение списка о последних 10 банах в общем чате.
</details>
<details>
         <summary>Изменение бана в общем чате</summary>

**Назначение команды:** Позволяет изменить текущий бан в общем чате у игрока.

Команда в [GitLab](https://gitlab.gearwap.ru/fort/server/-/tree/develop)

Пример команды:
```
/fort develop ACTION {"type":"changeUserBanInfoInChat", "accountId": 1 , "expirationTime": "-10", "timeUnit": "HOURS", "reasons": "1,2,3", "composeChangeDuration": true, "composeChangeReasons": true }
```

* `accountId` - id аккаунта, который нужно забанить в чате.
* `expirationTime` - время, на которое будет забанен пользователь. Максимальный срок бана - 365 дней, если прописать срок
  больше, то он автоматически сократиться до максимального. Если прописать MAX, то пользователь будет забанен на 365 дней,
  независимо от того, какой указан timeUnit. Может принимать следующие значения: Число (в кавычках), "MAX". Также можно
  прописать "-MAX" и пользователь будет разбанен в чате.
* `timeUnit` - единица измерения времени. Варианты: NANOSECONDS, MICROSECONDS, MILLISECONDS, SECONDS, MINUTES, HOURS, DAYS;
* `composeChangeDuration` - true/false параметр, который обозначает добавление/уменьшение текущего времени бана
  (`composeChangeDuration: true`), или полную перезапись текущего времени (`composeChangeDuration: false`)
* `reasons` - причины(а), по которым будет забанен игрок. Список причин.
* `composeChangeReasons` - true/false параметр, который обозначает добавление к текущим причинам бана
  (`composeChangeReasons: true`), или полную перезапись текущих причин на новые (`composeChangeReasons: false`)

Примечание:

1. Можно указать все параметры.
2. Указать только параметры изменения времени бана:
   `accountId, experationTime, timeUnit (Если experationTime не указан как "MAX"), composeChangeDuration.`
3. Указать только параметры изменения причин бана:
   `accountId, reasons, composeChangeReasons`

**Результатом** выполнения запроса будет изменение последнего `chatBanInfo` у профиля.

Примеры использования команды:

1. **Условие:** пользователь уже забанен на 10 часов по причине `TROLLING(2)`
* ```
  /fort develop ACTION {"type":"changeUserBanInfoInChat", "accountId": 1 , "expirationTime": "-5", "timeUnit": "HOURS", "composeChangeDuration": true, "reasons": "", "composeChangeReasons": true }
  ```
**В результате выполнения** у пользователя будет изменена продолжительность бана в чате на 5 часов, причина останется такая же.

2. **Условие:** пользователь уже забанен на 10 часов по причине `TROLLING(2)`
* ```
  /fort develop ACTION {"type":"changeUserBanInfoInChat", "accountId": 1 , "expirationTime": "", "timeUnit": "HOURS", "composeChangeDuration": true, "reasons": "1,3", "composeChangeReasons": true }
  ```
**В результате выполнения** пользователь будет забанен также на 10 часов, с причинами AGGRESSION_OR_SWEARING(1), TROLLING(2), FLOODING(3).

3. **Условие:** пользователь уже забанен на 10 часов по причине `TROLLING(2)`
* ```
  /fort develop ACTION {"type":"changeUserBanInfoInChat", "accountId": 1 , "expirationTime": "MAX", "timeUnit": "HOURS", "IsComposeChangeDuration": false, "reasons": "1,3", "IsComposeChangeReasons": false }
  ```
**В результате выполнения** пользователь будет на 365 с текущего момента (то есть без учёта уже проведённого времени в
бане), с причинами AGGRESSION_OR_SWEARING(1), FLOODING(3).

4. **Условие:** пользователь уже забанен на 10 часов по причине `TROLLING(2)`
* ```
  /fort develop ACTION {"type":"changeUserBanInfoInChat", "accountId": 1 , "expirationTime": "-100000", "timeUnit": "HOURS", "composeChangeDuration": false, "reasons": "", "composeChangeReasons": false }
  ```
**В результате выполнения** пользователь будет разбанен.

   </details>
