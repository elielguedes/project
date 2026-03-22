## API - PUBLICA 

## 🚀 Tecnologias utilizadas
<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/>
  <img src="https://logo.svgcdn.com/logos/fastapi.svg" width="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original.svg" width="40"/>
</p>

```mermaid
erDiagram

  USER {
    UUID id pk
    VARCHAR email
    VARCHAR senha
    VARCHAR adm
  }

  REGISTROS {
    UUID id pk
    INT qtd
    INT mes
    INT ano
    INT crime_id fk
    INT location_id fk
    INT user_id fk
  }

  CRIME {
    UUID id pk
    VARCHAR nome
  }

  LOCATION {
    UUID id pk
    VARCHAR cod_municipio
    VARCHAR risp
    VARCHAR rmbh
    VARCHAR nome_municipio
  }

  USER ||--o{ REGISTROS : POSSUI
  LOCATION ||--o{ REGISTROS : LOCAL
  CRIME ||--o{ REGISTROS : CRIME
```
