# BILLING

**Назначение команды**: Команда для выдачи награды игроку.

<details>
  <summary>Команды для выдачи наград игроку</summary>

Пример команды для одиночной выдачи:
```
/fort develop BILLING {"type": "newInvoice", "accountID": 10824, "product": [ { "type": "SCROLL", "typeId": 7 , "amount": 3 } ]}
```

Пример команды для выдачи списку аккаунтов (массовая рассылка):
```
/fort develop BILLING {"type":"newMultipleInvoice", "accountIds": [1234, 23456], "product":[{"type": "CURRENCY", "typeId": 2, "amount": 100 }]}
```

В поле `product` для каждого `type` есть еще и `typeId`:
* `type`: "CURRENCY" , `typeId`: ID_REAL=1, ID_SOFT=2, ID_HARD=3, ID_SCALE_POINT=4, ID_BATTLE_PASS_POINT = 5, ID_SCROLL_BOOK = 6
* `type`: "CARD" , `typeId`: id карточки
  [юнита](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=683969633),
  [здания](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=683969633)
* `type`: "EQUIPMENT" , `typeId`: id
  [экипировки светлых юнитов](https://docs.google.com/spreadsheets/d/1kdBQfDkRV__1Y-5IzBigfEN12qkJSjg1DAb7JhW6cMg/edit#gid=1326409349),
  [экипировки темных юнитов](https://docs.google.com/spreadsheets/d/1YFY6SqKDoo67wL8MB8A4Hwp0bbdZf8eL1_Brl6wTUDQ/edit#gid=172506499)
* `type`: "SCROLL" , `typeId`: id [свитка](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=43489479)
* `type`: "CHEST" , `typeId`:id [сундука](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=1763172340)
* `type`: AVATAR_ELEMENT, `typeId`:id [аватарки](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=1293473026)
* `type`: BATTERY, `typeId`:id [батареек](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=995187087)
* `type`: UNIVERSAL_REWARD, `typeId`:id наград
* `type`: FEATURE_PACK, `typeId`:id [фичапапка](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=1552980763)

**Результатами** выполнения запроса будут сообщение об успешно выполненном запросе и сама награда (карточка, сундук, свиток,
валюта и т. д.), которая будет отправлена на аккаунт.
</details>
<details>
  <summary>Награды для начисления</summary>

Награды начисляются либо через сообщения почти, как в рассылке так и в сообщении одному игроку, а так же напрямую через механизм реактивных наград с помощью команды BILLING.

Награды отправляются списком [] т.е. начислять можно сразу несколько типов наград. Внутри списка прописываются награды которые необходимо начислить.

Поля для начисления:

`type` - тип награды валюта, экипировка и т.д.
`typeId` - идентификатор начисляемой награды, берётся из справочников
`amount` - количество начисляемой награды
Команда начисления [валюты](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=1897456199):
```
/fort develop BILLING {"type":"newInvoice", "accountID": 6540, "product":[{"type": "CURRENCY", "typeId": 2, "amount": 100 }]}
```
* Команда начисления карточек [юнитов](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=683969633), [зданий](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=683969633):
```
/fort develop BILLING {"type": "newInvoice", "accountID": 6540, "product": [ { "type": "CARD", "typeId": 13, "amount": 1 } ]}
```
* Команда начисления [экипировки светлых юнитов](https://docs.google.com/spreadsheets/d/1kdBQfDkRV__1Y-5IzBigfEN12qkJSjg1DAb7JhW6cMg/edit#gid=1326409349), [экипировки темных юнитов](https://docs.google.com/spreadsheets/d/1YFY6SqKDoo67wL8MB8A4Hwp0bbdZf8eL1_Brl6wTUDQ/edit#gid=172506499):
```
/fort develop BILLING {"type": "newInvoice", "accountID": 6540, "product": [ { "type": "EQUIPMENT", "typeId": 1010001 , "amount": 1 } ]}
```
* Команда начисления [свитков](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=43489479):
```
/fort develop BILLING {"type": "newInvoice", "accountID": 6540, "product": [ { "type": "SCROLL", "typeId": 7 , "amount": 3 } ]}
```
* Команда начисления [сундуков](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=1763172340):
```
/fort develop BILLING {"type": "newInvoice", "accountID": 6540, "product": [ { "type": "CHEST", "typeId": 110101101, "amount": 1 } ]}
```
* Команда для выдачи списку аккаунтов (массовая рассылка):
```
/fort develop BILLING {"type":"newMultipleInvoice", "accountIds": [1234, 23456], "product":[{"type": "CURRENCY", "typeId": 2, "amount": 100 }]}
```

**Результатом** запроса будут сообщение об успешном выполнении и награда на аккаунте.
</details>
<details>
  <summary>Уменьшение количества валюты у игрока</summary>

Назначение команды: Уменьшает количество указанной валюты у игрока (но не меньше нуля).

Пример команды:
```
/fort develop BILLING {"type": "takeAway", "accountID": 21, "currencyID": 2, "amount": 100500}
```
* `accountID` - id аккаунта, на котором необходимо изменить количество валюты;
* `currencyID` - id валюты, количество которой необходимо уменьшить (ID_REAL=1, ID_SOFT=2, ID_HARD=3, ID_SCALE_POINT=4, ID_BATTLE_PASS_POINT = 5, ID_SCROLL_BOOK = 6, ID_ARENA_TICKET = 110, ID_ARENA_POINTS = 8);
* `amount` - количество валюты, которое необходимо забрать у игрока.
</details>
<details>
  <summary>Команда на порт для изменения количество энергии героев</summary>

Назначение команды: Уменьшает/увеличивает количество энергии героев у игрока

Пример команды:
```
/fort develop BILLING {"type": "changeHeroEnergy", "accountID": 21, "amount": 100500, "increaseEnergy": true}
```

* `accountID` - id аккаунта, на котором необходимо изменить количество валюты;
* `amount` - количество энергии героев на которое измениться значение у игрока
  Не должно быть отрицательным
* `increaseEnergy` - флаг отвечающий за увеличение/уменьшение энергии, true - увеличить, false - уменьшить

Команда не может уменьшить энергию меньше 0

Клиент уведомляется об изменении через сообщение SetHeroEnergy
</details>
