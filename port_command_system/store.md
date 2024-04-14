# STORE

**Назначение команд:** Команды для оперирования релизом сборок.

Список всех доступных команд вызываются с помощью запроса `/store h`.

Команды для google работают гораздо быстрее чем для apple. Время выполнение команд для apple вплоть до 2-х минут.

Команда может быть отправлена как из канала, так и из треда в канале.

Если отправили команду, то необходимо дождаться ее выполнения.

<details>
<summary>Команда для запроса состояний сборок в магазине</summary>


```
/store fort app_get_states {"store": "store_name"}
```

`store_name` - название магазина (apple, google)
</details>
<details>
<summary>Команда для передвижения сборки на следующий этап</summary>

```
/store fort app_state_next {"store": "store_name", "version":build_number}
```

`store_name` - название магазина (apple, google)

`build_number` - номер сборки (11345, 11361 и т.д.)

Apple: для перехода ОБТ в PROD сборка должна быть проверена и иметь статус PENDING_DEVELOPER_RELEASE
</details>
<details>
<summary>Команда для передвижения сборки на конкретный этап</summary>

```
/store fort app_state {"store":"store_name", "version":build_number, "state": "state_name", "percent": percent}
```

`store_name` - название магазина (`apple, google`)

`build_number` - номер сборки (11345, 11361 и т.д.)

`state_name` - состояние (ЗБТ, ОБТ, PROD)

`percent` - процент раскатки (от 1 до 100). 100 - полная раскатка. Для Apple можно указывать всегда 0
</details>
<details>
<summary>Команда изменения релизных заметок</summary>

```
/store fort change_rn {"store" : "store_name", "version": build_number, "rn_type": "обт/prod"}
```

`store_name` - название магазина (apple, google)

`build_number` - номер сборки (11345, 11361 и т.д.)

**Состояния сборки в PlayMarket:**

`completed` - сборка раскатана на 100%

`inProgress` - сборка в процессе раскатки (присутствует процент раскатки)

`halted` - раскатка сборки приостановлена

`draft` - сборка не будет доставлена пользователям (черновик)

**Состояния сборки в AppStore:**

`Ready to Submit` - готова к отправке на ревью

`Waiting for Review` - ждет ревью от Apple

`In Review` - находится на ревью

`Rejected` - отклонена Apple

`Ready to Test` - готова к тестированию

`Testing` - в тестировании

`Ready for Review` - готово к отправке на ревью

`Pending Developer Release` - ревью пройдено, сборка ожидает релиза

`Developer Rejected` - проверка отменена разработчиком

`Processing for App Store` - отправлена в релиз

`Ready for Sale` - сборка доступна всем игрокам

`Replaced with new version` - cборка заменена новой версией в PROD

Работает только с Apple
</details>
<details>
<summary>Команда запуска выгрузки shared build по prod/beta ссылке</summary>

```
/store fort upload_shared_build_link{"version": build_number, "linkType": "beta/prod"} 
```

`build_number` - номер сборки (11345, 11361 и т.д.)
</details>












