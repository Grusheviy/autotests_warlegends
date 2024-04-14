#  DICTIONARY (ОТЛОЖЕНО)

Команды по взаимодействию с механизмом версионинга справочников

### Добавление новой версии справочников

Позволяет добавить новую версию справочника. Предварительно ее нужно заархивировать

Пример:

`DICTIONARY{ "type":"upload", "buildVersionMinor": 0, "buildVersionMajor": 10000, "resourceVersion": 1, "resource": "v1", "protocolMinor": 0, "protocolMajor": 10000}`


Маппинг команды:
`curl -X PUT "http://172.26.0.172:20070/DICTIONARY/upload?buildVersionMinor=25&buildVersionMajor=10000&resourceVersion=3&resource=v3&protocolMinor=0&protocolMajor=10000" -H "accept: */*" -H "Content-Type: multipart/form-data" -F "file=@v3.zip;type=application/x-zip-compressed"`

Как эту команду реализовать через чат, я не представляю.

Потом, почему я не стал делать отправку параметров через json? В Spring есть ограничения на получение файла и json
одновременно. Пришлось остановиться на таком способе. Зато его можно дергать через Swagger

### Удаление заданной версии справочников 

Позволяет удалить заданную версию справочника

`DICTIONARY{ "type":"delete","buildVersionMinor":0, "buildVersionMajor": 10000, "resourceVersion": 1, "resource": "v1", "protocolMinor": 0, "protocolMajor": 10000}`

Маппинг команды:
`-service/DICTIONARY/delete-d "{"buildVersionMinor": 0, "buildVersionMajor": 10000, "resourceVersion": 1, "resource": "v1", "protocolMinor": 0, "protocolMajor": 10000}"`











