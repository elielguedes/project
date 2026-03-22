
```mermaid
erDiagram

  USER {
    STRING id uuid  pk
    VARCHAR email
    VARCHAR senha
    VARCHAR adm
  }

  REGISTROS {
    STRING id UUID  pk
    INT qtd
    INT mes
    INT ano
    INT crime_id fk
    INT location_id fk
    INT user_id fk
  }

  CRIME {
    STRING id uuid  pk
    VARCHAR nome
  }

  LOCATION {
    STRING id uuid pk
    VARCHAR cod_municipio
    VARCHAR risp
    VARCHAR rmbh
    VARCHAR nome_municipio
  }

  USER ||--o{ REGISTROS : POSSUI
  LOCATION ||--o{ REGISTROS : LOCAL
  CRIME ||--o{ REGISTROS : CRIME
```
