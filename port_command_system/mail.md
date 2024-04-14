# MAIL

**Назначение команды:** Команда для создания личных писем от администрации игроку. Письма могут содержать как текстовые уведомления, так и какие-либо сущности (валюту, сундуки, карточки и т. д.).
<details>
<summary>Пример:</summary>

```
/fort develop MAIL {"type": "addLetter", "accountID": 7143, "message": {"category": "COMMON", "caption": "Social Networks", "description": "Join us in internet", "spriteName": "SpriteTest", "buttonsInfo": [ { "url": "https://www.facebook.com/", "labelName": "string", "spriteName": "icon_facebook"}], "products": [ { "type": "CURRENCY", "typeId": 2, "amount": 10 } ]}}
```
Вместо `develop` можно поставить `alpha, beta, feature`

* `"category": "COMMON"` //обязательное поле. Варианты: COMMON, SERVICE, IMPORTANT
* `"caption": "string"`  //обязательное поле
* `"description": "string"`  //обязательное поле
* `"spriteName": "string"`  //обязательное поле
* `"buttonsInfo": [ { "url": "string", "labelName": "string", "spriteName": "string" }`
* `"products": [ { "type": "CURRENCY", "typeId": 3, "amount": 10 } ]` - основное поле для передачи ресурсов, валюты и т.д.

В поле `product` для каждого `type` есть еще и `typeId`:

* `type`: "CURRENCY", `typeid`: ID_SOFT=2, ID_HARD=3, ID_BATTLE_PASS_POINT=5
* `type`: "CARD", `typeid`: id карточки [юнита](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=683969633), [здания](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=683969633)
* `type`: "EQUIPMENT", `typeid`: id [экипировки светлых юнитов](https://docs.google.com/spreadsheets/d/1kdBQfDkRV__1Y-5IzBigfEN12qkJSjg1DAb7JhW6cMg/edit#gid=1326409349), [экипировки темных юнитов](https://docs.google.com/spreadsheets/d/1YFY6SqKDoo67wL8MB8A4Hwp0bbdZf8eL1_Brl6wTUDQ/edit#gid=172506499)
* `type`: "SCROLL", `typeid`: id [свитка](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=43489479)
* `type`: "CHEST", `typeid`:id [сундука](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=1763172340)
* `type`: "BATTERY", `typeid`:id [батарейки](https://docs.google.com/spreadsheets/d/1doTNlgvJ00PMs5p5mrQxBEPuylVA7ZXbSfeNk2WpI14/edit#gid=1015279351)

**Результатом** запроса будет письмо, содержащее заданные элементы, которое будет отправлено на почту в игре.
</details>
